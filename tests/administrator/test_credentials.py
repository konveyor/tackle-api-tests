import pytest
from fixtures.credentials import source_username_credentials


@pytest.mark.credentials
def test_create_credential(source_username_credentials, get_api):
    cred_from_db = get_api.identities_id_get(source_username_credentials.id)
    assert source_username_credentials == cred_from_db
