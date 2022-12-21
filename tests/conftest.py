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


@pytest.fixture()
def tag_types_names(get_api):
    return [tag.name for tag in get_api.tagtypes_get()]


@pytest.fixture()
def tag_types_ids(get_api):
    return [tag.id for tag in get_api.tagtypes_get()]


@pytest.fixture(scope="session")
def source_username_credentials(module_uuid, create_api, delete_api):
    credential_data = {"name": f"source-{module_uuid}", "kind": "source",
                       "password": config.get("cred_git_token"),
                       "user": config.get("cred_git_username")}
    new_cred = create_api.identities_post(credential_data)
    yield new_cred
    delete_api.identities_id_delete(new_cred.id)


@pytest.fixture(scope="session")
def git_application(source_username_credentials, json_application, module_uuid, create_api, get_api, delete_api):
    application_data = {"name": f"app-{module_uuid}",
                        "identities": [{"id": source_username_credentials.id}]}
    for key, value in json_application[0].items():
        application_data[key] = value
    new_app = create_api.applications_post(application_data)
    yield new_app
    delete_api.applications_id_delete(new_app.id)
