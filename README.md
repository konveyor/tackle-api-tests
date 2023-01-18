# tackle-api-tests
API tests for TACKLE

Using Swagger client for API testing.
Will cover basic API test to run sanity or smoke tests against a new build of TACKLE.

PR Reviewer :sshveta@redhat.com

Maintained by: mguetta@redhat.com

## Run Tests

### Using podman or docker (running in a container is recommended)
$ podman rmi tackle-integration-tests # if needed

$ podman build -f Dockerfile -t tackle-integration-tests

$ podman run -e TACKLE_USER=? -e TACKLE_PASSWORD=? -e TACKLE_URL='http://x.x.x.x' tackle-integration-tests [PYTEST OPTIONS] [TEST FOLDER]


from example:

$ podman run -e TACKLE_USER=user -e TACKLE_PASSWORD=pass -e TACKLE_URL='https://4.4.4.4' tackle-integration-tests -m smoke tests


### Virtual Environment
$ python3.9 -m venv ./venv/ # Create the Virtual Environment.

$ source venv/bin/activate # Activate the Virtual Environment Just Created.

$ pip install -r requirements.txt

$ export TACKLE_USER=?

$ export TACKLE_PASSWORD=?

$ export =? # including http:// Or https:// and without no closing /

$ python3.9 -m pytest /home/amos/git/tackle-integration-tests/tests/test_tags.py

### Utils

#### Get keycloak API token
$ python3.9 utils/get-token.py --user=? --password=? --host=?

##### Note: tackle url should include http:// Or https:// without no closing /