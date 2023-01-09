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
def json_defaults():
    with open('data/defaults.json', 'r') as file:
        yield json.load(file)


