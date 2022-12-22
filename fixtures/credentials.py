import pytest
from pytest_testconfig import config


@pytest.fixture(scope="session")
def source_username_credentials(module_uuid, create_api, delete_api):
    credential_data = {"name": f"source-{module_uuid}", "kind": "source",
                       "password": config.get("cred_git_token"),
                       "user": config.get("cred_git_username")}
    new_cred = create_api.identities_post(credential_data)
    yield new_cred
    delete_api.identities_id_delete(new_cred.id)
