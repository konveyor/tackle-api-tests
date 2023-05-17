import os
from urllib.parse import urlparse

from keycloak import KeycloakOpenID

import swagger_client


# Borg Pattern
# https://github.com/faif/python-patterns/blob/master/patterns/creational/borg.py
class KeycloakClient:
    __shared_state = {}

    def __init__(self):
        if not KeycloakClient.__shared_state:
            KeycloakClient.__shared_state = self.__dict__
            self.username = os.environ.get("TACKLE_USER")
            self.password = os.environ.get("TACKLE_PASSWORD")
            self.url = os.environ.get("TACKLE_URL")

            parsed_url = urlparse(self.url)
            if parsed_url.netloc.startswith("mta"):
                self.realm_name = "mta"
                self.client_id = "mta-ui"
                self.keycloak_openid = KeycloakOpenID(
                    server_url=f"{self.url}/auth/", client_id=self.client_id, realm_name=self.realm_name, verify=False
                )
            else:
                self.realm_name = "tackle"
                self.client_id = "tackle-ui"

        else:
            self.__dict__ = KeycloakClient.__shared_state

    def get_access_token(self):
        if self.realm_name == "mta":
            return self.keycloak_openid.token(self.username, self.password)["access_token"]


class TackleApiGateway:
    """
    Gateway for API operations.
    """

    def __init__(self):
        # swagger api clients
        swagger_api = swagger_client.api
        self.clients = {}
        self.clients["get_api"] = swagger_api.get_api.GetApi()
        self.clients["create_api"] = swagger_api.create_api.CreateApi()
        self.clients["delete_api"] = swagger_api.delete_api.DeleteApi()
        self.clients["update_api"] = swagger_api.update_api.UpdateApi()

        # common config
        api_token = self.api_token
        for cl in self.clients.values():
            c = cl.api_client.configuration
            c.host = f"{os.environ.get('TACKLE_URL')}/hub"
            c.api_key_prefix["Authorization"] = "Bearer"
            c.api_key["Authorization"] = api_token

    @property
    def api_token(self):
        """
        Get an API token by sending authentication request to keycloak.
        """
        keycloak_client = KeycloakClient()
        return keycloak_client.get_access_token()
