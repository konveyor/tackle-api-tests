from tackle_api_gateway import TackleClient

if __name__ == "__main__":
    tackle_client = TackleClient()
    print(f"Bearer {tackle_client.get_access_token()}")
