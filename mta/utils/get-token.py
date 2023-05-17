from tackle_api_gateway import KeycloakClient

if __name__ == "__main__":
    keycloak_client = KeycloakClient()
    print(f"Bearer {keycloak_client.get_access_token()}")
