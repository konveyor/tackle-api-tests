import json

import pytest

from swagger_client.models.api_application import ApiApplication


def json_application():
    with open("mta/data/application.json", "r") as file:
        return json.load(file)


@pytest.fixture(scope="session")
def applications_data():
    return json_application()


def json_analysis():
    with open("mta/data/analysis.json", "r") as file:
        return json.load(file)


@pytest.fixture(scope="session")
def application(source_username_credentials, applications_data, create_api, delete_api, request):
    app_name = request.param
    app_data = applications_data[app_name]
    if "identities" in app_data:
        app_data["identities"] = [{"id": source_username_credentials.id}]
    api_app = ApiApplication(**app_data)
    new_app = create_api.applications_post(api_app.to_dict())
    yield new_app
    delete_api.applications_id_delete(new_app.id)
