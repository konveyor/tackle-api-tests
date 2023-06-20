import pytest


@pytest.mark.credentials
def test_create_source_credential(source_username_credentials, identities_api):
    cred_from_db = identities_api.identities_id_get(str(source_username_credentials.id))
    assert source_username_credentials == cred_from_db


@pytest.mark.credentials
def test_create_maven_credential(maven_credential, identities_api):
    cred_from_db = identities_api.identities_id_get(str(maven_credential.id))
    assert maven_credential == cred_from_db
