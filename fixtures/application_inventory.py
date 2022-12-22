import pytest
from fixtures.credentials import source_username_credentials


@pytest.fixture(scope="session")
def git_application(source_username_credentials, json_application, module_uuid, create_api, get_api, delete_api):
    application_data = {"name": f"app-{module_uuid}",
                        "identities": [{"id": source_username_credentials.id}]}
    for key, value in json_application[0].items():
        application_data[key] = value
    new_app = create_api.applications_post(application_data)
    yield new_app
    delete_api.applications_id_delete(new_app.id)
