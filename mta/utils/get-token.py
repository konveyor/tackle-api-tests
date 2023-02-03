import argparse

from tackle_api_gateway import TackleClient

parser = argparse.ArgumentParser(description="Konveyor Tackle maintenance tool.")
parser.add_argument("-u", "--user", dest="user", type=str, help="username")
parser.add_argument("-p", "--password", dest="password", type=str, help="password")
parser.add_argument("-l", "--host", dest="host", type=str, help="host")
args = parser.parse_args()


if __name__ == "__main__":
    tackle_client = TackleClient()
    tackle_client.url = args.host
    tackle_client.username = args.user
    tackle_client.password = args.password
    print(f"Bearer {tackle_client.get_access_token()}")
