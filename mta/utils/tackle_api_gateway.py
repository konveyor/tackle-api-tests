import os

from keycloak import KeycloakOpenID

import swagger_client


# Borg Pattern
# https://github.com/faif/python-patterns/blob/master/patterns/creational/borg.py
class TackleClient:
    __shared_state = {}

    def __init__(self):
        if not TackleClient.__shared_state:
            TackleClient.__shared_state = self.__dict__
            self.realm_name = "tackle"
            self.client_id = "tackle-ui"
            self.url = os.environ.get("TACKLE_URL")
            self.username = os.environ.get("TACKLE_USER")
            self.password = os.environ.get("TACKLE_PASSWORD")
            self.keycloak_openid = None

        else:
            self.__dict__ = TackleClient.__shared_state

    def get_access_token(self):
        # Configure client if not exist
        if not self.keycloak_openid:
            self.keycloak_openid = KeycloakOpenID(
                server_url=f"{self.url}/auth/", client_id=self.client_id, realm_name=self.realm_name, verify=False
            )
        return self.keycloak_openid.token(self.username, self.password)["access_token"]


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
        self.update_api = swagger_api.update_api.UpdateApi()
        self.clients.extend([self.get_api, self.create_api, self.delete_api, self.update_api])  # noqa: E501
        self.tackle_client = TackleClient()

        # common config
        for cl in self.clients:
            c = cl.api_client.configuration
            c.host = f"{os.environ.get('TACKLE_URL')}/hub"
            c.api_key_prefix["Authorization"] = "Bearer"
            c.api_key["Authorization"] = self.__getattribute__("api_token")

    def refresh_api_token(self):
        """
        Refresh the API Token and update all clients.
        """
        for cl in self.clients:
            c = cl.api_client.configuration
            c.api_key["Authorization"] = self.api_token

    @property
    def api_token(self):
        """
        Get a Refreshed API token by sending another authentication request to keycloak.
        """
        t = TackleClient()
        return t.get_access_token()
