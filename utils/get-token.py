import argparse

from utils.helpers import get_key_cloak_token

parser = argparse.ArgumentParser(description='Konveyor Tackle maintenance tool.')
parser.add_argument('-u', '--user', dest='user', type=str, help='username')
parser.add_argument('-p', '--password', dest='password', type=str, help='password')
parser.add_argument('-l', '--host', dest='host',  type=str, help='host')
args = parser.parse_args()


if __name__ == "__main__":
    print(get_key_cloak_token(host=args.host, username=args.user, password=args.password))
