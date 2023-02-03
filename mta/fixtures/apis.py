import pytest

from mta.utils.tackle_api_gateway import TackleApiGateway

tackle_api_gateway = TackleApiGateway()


@pytest.fixture(scope="session")
def get_api():
    return tackle_api_gateway.get_api


@pytest.fixture(scope="session")
def create_api():
    return tackle_api_gateway.create_api


@pytest.fixture(scope="session")
def delete_api():
    return tackle_api_gateway.delete_api


@pytest.fixture(scope="session")
def update_api():
    return tackle_api_gateway.update_api
