import pytest

from mta.utils.tackle_api_gateway import TackleApiGateway

tackle_api_gateway = TackleApiGateway()


@pytest.fixture(scope="session")
def identities_api():
    return tackle_api_gateway.clients.get("IdentitiesApi")


@pytest.fixture(scope="session")
def applications_api():
    return tackle_api_gateway.clients.get("ApplicationsApi")


@pytest.fixture(scope="session")
def tasks_api():
    return tackle_api_gateway.clients.get("TasksApi")


@pytest.fixture(scope="session")
def get_api():
    return tackle_api_gateway.clients.get("get_api")


@pytest.fixture(scope="session")
def create_api():
    return tackle_api_gateway.clients.get("create_api")


@pytest.fixture(scope="session")
def delete_api():
    return tackle_api_gateway.clients.get("delete_api")


@pytest.fixture(scope="session")
def update_api():
    return tackle_api_gateway.clients.get("update_api")


@pytest.fixture(autouse=True)
def refresh_token():
    """
    Refresh the API Token and update all clients.
    """
    api_token = tackle_api_gateway.api_token
    for cl in tackle_api_gateway.clients.values():
        client_configuration = cl.api_client.configuration
        client_configuration.api_key["Authorization"] = api_token
