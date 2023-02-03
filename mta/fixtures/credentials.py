import pytest
from pytest_testconfig import config

from swagger_client.models.api_identity import ApiIdentity


@pytest.fixture(scope="session")
def source_username_credentials(create_api, delete_api):
    credential_data = {
        "name": config.get("cred_git_name"),
        "kind": "source",
        "password": config.get("cred_git_token"),
        "user": config.get("cred_git_username"),
    }
    api_identity = ApiIdentity(**credential_data)
    new_cred = create_api.identities_post(api_identity.to_dict())
    yield new_cred
    delete_api.identities_id_delete(new_cred.id)
