import json
from contextlib import contextmanager

import pytest

from swagger_client.models.api_application import ApiApplication
from swagger_client.models.api_task import ApiTask


@pytest.fixture(scope="session")
def source_applications_data():
    with open("mta/data/source_application.json", "r") as file:
        yield json.load(file)


@pytest.fixture(scope="session")
def binary_applications_data():
    with open("mta/data/binary_application.json", "r") as file:
        yield json.load(file)


@pytest.fixture(scope="session")
def json_analysis():
    with open("mta/data/analysis.json", "r") as file:
        json_list = json.load(file)
    #  Filter out duplicates
    return {value["app_name"]: value for value in json_list}


@contextmanager
def create_applications(create_api, delete_api, applications_data, credentials: list):
    apps = []
    for app_data in applications_data:
        if "identities" in app_data:
            app_data["identities"] = [{"id": cred["id"]} for cred in credentials]
        api_app = ApiApplication(**app_data)
        new_app = create_api.applications_post(api_app.to_dict())
        apps.append(new_app)
    yield apps
    for app in apps:
        delete_api.applications_id_delete(app.id)


@pytest.fixture(scope="session")
def source_applications(source_applications_data, source_username_credentials, create_api, delete_api):
    creds = [source_username_credentials.to_dict()]
    with create_applications(
        create_api=create_api, delete_api=delete_api, applications_data=source_applications_data, credentials=creds
    ) as source_apps:
        yield source_apps


@pytest.fixture(scope="session")
def binary_applications(binary_applications_data, maven_credential, create_api, delete_api):
    creds = [maven_credential.to_dict()]
    with create_applications(
        create_api=create_api, delete_api=delete_api, applications_data=binary_applications_data, credentials=creds
    ) as binary_apps:
        yield binary_apps


@pytest.fixture()
def tasks(request, json_analysis, create_api, get_api, update_api):
    applications = request.getfixturevalue(request.param)
    tasks_from_db = []
    for app in applications:
        app_id = app.id
        app_name = app.name
        if app_name in json_analysis:
            analysis_data = json_analysis[app_name]
            data = analysis_data["data"]
            data["output"] = "/windup/report"
            application = {"id": app_id, "name": app_name}
            task = ApiTask(addon="windup", application=application, data=data)
            new_task = create_api.tasks_post(task=task.to_dict())
            update_api.tasks_id_submit_put(id=new_task.id, task=new_task)
            tasks_from_db.append(get_api.tasks_id_get(new_task.id))
    return tasks_from_db
