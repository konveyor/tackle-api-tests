import pytest

 
@pytest.mark.credentials
def test_create_source_credential(source_username_credentials, get_api):
    cred_from_db = get_api.identities_id_get(source_username_credentials.id)
    assert source_username_credentials == cred_from_db


@pytest.mark.credentials
def test_create_maven_credential(maven_credential, get_api):
    cred_from_db = get_api.identities_id_get(maven_credential.id)
    assert maven_credential == cred_from_db
