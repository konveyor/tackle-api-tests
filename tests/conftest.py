import os
import pytest
import json
from datetime import datetime
import swagger_client
from utils.helpers import get_key_cloak_token
from pytest_testconfig import config


@pytest.fixture(scope="session")
def module_uuid():
    return f"api-resource-{datetime.now().strftime('%y-%d-%m-%H-%M-%S')}"


def api_call(function):
    """
    Decorator for api calls.
    """

    def wrapper(*args):
        args[0].refresh_api_token()
        return function(*args)

    return wrapper


class TackleApiGateway:
    """
    Gateway for API operations.
    """

    def __init__(self):
        # swagger api clients
        swagger_api = swagger_client.api
        self.clients = []
        self.get_api = swagger_api.get_api.GetApi()
        self.create_api = swagger_api.create_api.CreateApi()
        self.delete_api = swagger_api.delete_api.DeleteApi()
        self.clients.extend([self.get_api, self.create_api, self.delete_api])  # noqa: E501

        # common config
        for cl in self.clients:
            c = cl.api_client.configuration
            c.host = f"{os.environ.get('TACKLE_URL')}/hub"
            c.api_key_prefix['Authorization'] = 'Bearer'

    def refresh_api_token(self):
        """
        Refresh the API Token and update all clients.
        """
        for cl in self.clients:
            c = cl.api_client.configuration
            c.api_key['Authorization'] = self.api_token

    @api_call
    def get_tag_names(self):
        """
        Tag Controller Names.
        """
        api = self.get_api.tags_get()
        return [tag.name for tag in api]

    @property
    def api_token(self):
        """
        Get a Refreshed API token by sending another authentication request to keycloak.
        """
        return get_key_cloak_token(username=os.environ.get("TACKLE_USER"),
                                   password=os.environ.get("TACKLE_PASSWORD"),
                                   host=os.environ.get("TACKLE_URL"))


@pytest.fixture(scope="session")
def tackle_api_gateway():
    return TackleApiGateway()


@pytest.fixture(scope="session")
def get_api(tackle_api_gateway):
    return tackle_api_gateway.get_api


@pytest.fixture(scope="session")
def create_api(tackle_api_gateway):
    return tackle_api_gateway.create_api


@pytest.fixture(scope="session")
def delete_api(tackle_api_gateway):
    return tackle_api_gateway.delete_api


@pytest.fixture(scope="session")
def json_defaults():
    with open('data/defaults.json', 'r') as file:
        yield json.load(file)


@pytest.fixture(scope="session")
def json_application():
    with open('data/application.json', 'r') as file:
        yield json.load(file)

