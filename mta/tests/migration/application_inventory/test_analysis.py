import pytest
from wait_for import wait_for

from mta.fixtures.application_inventory import json_analysis, json_application
from swagger_client.models.api_task import ApiTask


@pytest.mark.parametrize("application", json_application(), indirect=True)
@pytest.mark.parametrize("analysis_item", json_analysis(), ids=[item.get("source") for item in json_analysis()])
@pytest.mark.analysis
def test_analysis(application, analysis_item, tasks_api):
    """
    This function uses functions to provide input parameters representing an application for analysis and an analysis
    item to be run on the application. The function starts by checking if the app and analysis item match by comparing
    their names. If they do not match, the test is skipped.

    If the app and analysis item match, a new task is created for the analysis to be run.
    The function waits for the task to complete by periodically checking its state until the state changes to
    "Succeeded".
    """

    app = application
    analysis_info = analysis_item
    if app.name != analysis_info["app_name"]:
        pytest.skip("The analysis item should not run using the current app. Skipping test")
    task_data = {"mode": analysis_info.get("mode"), "targets": analysis_info.get("targets"), "output": "/windup/report"}
    api_task = ApiTask(addon="windup", application={"id": app.id, "name": app.name}, data=task_data)
    new_task = tasks_api.tasks_post(task=api_task.to_dict())

    # Start the analysis by calling the submit method
    tasks_api.tasks_id_submit_put(id=new_task.id, task=new_task)
    wait_for(lambda: tasks_api.tasks_id_get(str(new_task.id)).state == "Succeeded", delay=5, timeout=180)
