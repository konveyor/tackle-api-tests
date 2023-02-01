# tackle-api-tests
API tests for TACKLE

Using Swagger client for API testing.
Will cover basic API test to run sanity or smoke tests against a new build of TACKLE.

PR Reviewer :sshveta@redhat.com

Maintained by: mguetta@redhat.com

## Code of Conduct
Refer to Konveyor's Code of Conduct [here](https://github.com/konveyor/community/blob/main/CODE_OF_CONDUCT.md).

## Run Tests

> **_NOTE:_** You should have minikube/Openshift cluster with Tackle installed

```bash
git clone https://github.com/konveyor/tackle-api-tests.git
cd tackle-api-tests
```

### Using Virtual Environment
```bash
# Create the Virtual Environment
python3 -m venv ./venv/

# Activate the Virtual Environment just created
source venv/bin/activate

# Install required packages
pip install -r requirements.txt

export TACKLE_USER=?

export TACKLE_PASSWORD=?

export TACKLE_URL=? # including http:// Or https:// and without no closing /

# Run tests which marked with @pytest.mark.analysis
python3 -m pytest -v -m analysis
```

### Using Container
```bash
# If needed, remove existing container
podman rm tests-run

# If needed, remove locally stored image
podman rmi tackle-api-tests

podman build -f Dockerfile -t tackle-api-tests

podman run --name tests-run -e TACKLE_USER=? -e TACKLE_PASSWORD=? -e TACKLE_URL=http://x.x.x.x tackle-api-tests [PYTEST OPTIONS]

# for example:
# podman run --name tests-run -e TACKLE_USER=user -e TACKLE_PASSWORD=pass -e TACKLE_URL=https://1.1.1.1 tackle-api-tests -m tags
```

## Utils

### Get keycloak API token
```bash
python3 utils/get-token.py --user=? --password=? --host=?
# Note: host (tackle url) should include http:// Or https:// without no closing /
```

## Generate swagger_client library
1. Download current stable 2.x.x swagger-codegen-cli tool
    ```bash
    # Download current stable 2.x.x branch (Swagger and OpenAPI version 2)
    wget https://repo1.maven.org/maven2/io/swagger/swagger-codegen-cli/2.4.29/swagger-codegen-cli-2.4.29.jar -O swagger-codegen-cli.jar
    ```
2. Download [swagger.yaml](https://raw.githubusercontent.com/konveyor/tackle2-hub/main/docs/swagger.yaml) from konveyor/tackle2-hub
3. Edit swagger.yaml file with info and security sections. See example [here](swagger.yaml#L2352)
4. Generate a Python client library
   ```bash
   java -jar swagger-codegen-cli.jar generate -i swagger.yaml -l python
    ```
5. Make sure that `swagger_client.configuration.verify_ssl = False` in order not to verify the SSL/TLS request
6. For more information see: [Swagger Codegen](https://github.com/swagger-api/swagger-codegen#readme)
