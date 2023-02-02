import json

import pytest

from swagger_client.models.api_application import ApiApplication
from swagger_client.models.api_task_group import ApiTaskGroup


@pytest.fixture(scope="session")
def json_application():
    with open("mta/data/application.json", "r") as file:
        yield json.load(file)


@pytest.fixture(scope="session")
def json_analysis():
    with open("mta/data/analysis.json", "r") as file:
        json_list = json.load(file)
    #  Filter out duplicates
    return {value["app_name"]: value for value in json_list}


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
def task_groups(applications, json_analysis, create_api, get_api, update_api):
    tg_from_db = []
    for app in applications:
        app_id = app.id
        app_name = app.name
        if app_name in json_analysis:
            analysis_data = json_analysis[app_name]
            data = {"targets": analysis_data["targets"], "output": "/windup/report"}
            tasks = [
                {
                    "addon": "windup",
                    "name": f"app{app_id}.{app_id}.windup",
                    "data": {},
                    "application": {"id": app_id, "name": app_name},
                }
            ]
            task_group = ApiTaskGroup(addon="windup", data=data, tasks=tasks)
            new_taskgroup = create_api.taskgroups_post(taskgroup=task_group.to_dict())
            update_api.taskgroups_id_submit_put(id=new_taskgroup.id, taskgroup=new_taskgroup)
            tg_from_db.append(get_api.taskgroups_id_get(new_taskgroup.id))
    return tg_from_db
