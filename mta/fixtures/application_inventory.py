import json

import pytest

from swagger_client.models.api_application import ApiApplication
from swagger_client.models.api_task import ApiTask


@pytest.fixture(scope="session")
def json_application():
    with open("mta/data/application.json", "r") as file:
        yield json.load(file)


@pytest.fixture(scope="session")
def analyses_data():
    with open("mta/data/analysis.json", "r") as file:
        return json.load(file)


@pytest.fixture(scope="session")
def applications(source_username_credentials, json_application, create_api, delete_api):
    apps = []
    for app in json_application:
        application_data = {}
        for key, value in app.items():
            application_data[key] = value
        if "identities" in application_data:
            application_data["identities"] = [{"id": source_username_credentials.id}]
        api_app = ApiApplication(**application_data)
        new_app = create_api.applications_post(api_app.to_dict())
        apps.append(new_app)
    yield apps
    for app in apps:
        delete_api.applications_id_delete(app.id)


@pytest.fixture()
def tasks(applications, analyses_data, create_api, get_api, update_api):
    tasks_from_db = []
    for app in applications:
        app_id = app.id
        app_name = app.name
        if app_name in analyses_data:
            analysis_info = analyses_data[app_name]
            task_data = {"targets": analysis_info["targets"], "output": "/windup/report"}
            application = {"id": app_id, "name": app_name}
            task = ApiTask(addon="windup", application=application, data=task_data)
            new_task = create_api.tasks_post(task=task.to_dict())
            update_api.tasks_id_submit_put(id=new_task.id, task=new_task)
            tasks_from_db.append(get_api.tasks_id_get(new_task.id))
    return tasks_from_db
