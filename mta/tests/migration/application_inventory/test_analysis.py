import pytest
from wait_for import wait_for

from mta.fixtures.application_inventory import json_application
from swagger_client.models.api_task import ApiTask


@pytest.mark.parametrize("application", json_application(), indirect=True)
@pytest.mark.analysis
def test_source_analysis(application, analysis_item, create_api, get_api, update_api):
    app = application
    analysis_info = analysis_item
    if app.name != analysis_info["app_name"]:
        pytest.skip("The analysis item should not run using the current app. Skipping test")
    task_data = {"targets": analysis_info["targets"], "output": "/windup/report"}
    api_task = ApiTask(addon="windup", application={"id": app.id, "name": app.name}, data=task_data)
    new_task = create_api.tasks_post(task=api_task.to_dict())

    # Start the analysis by calling the submit method
    update_api.tasks_id_submit_put(id=new_task.id, task=new_task)
    wait_for(lambda: get_api.tasks_id_get(str(new_task.id)).state == "Succeeded", delay=5, timeout=180)
