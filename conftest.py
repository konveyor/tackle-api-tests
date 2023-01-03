import pytest
import json
from datetime import datetime

# project root conftest.py

pytest_plugins = [
    "fixtures.apis",
    "fixtures.application_inventory",
    "fixtures.credentials",
    "fixtures.tags"
]


@pytest.fixture(scope="session")
def module_uuid():
    return f"api-resource-{datetime.now().strftime('%y-%d-%m-%H-%M-%S')}"


@pytest.fixture(scope="session")
def json_defaults():
    with open('data/defaults.json', 'r') as file:
        yield json.load(file)


@pytest.fixture(scope="session")
def json_application():
    with open('data/application.json', 'r') as file:
        yield json.load(file)

