import json

import pytest

# project root conftest.py

pytest_plugins = [
    "mta.fixtures.apis",
    "mta.fixtures.application_inventory",
    "mta.fixtures.credentials",
    "mta.fixtures.tags",
]


@pytest.fixture(scope="session")
def json_defaults():
    with open("mta/data/defaults.json", "r") as file:
        yield json.load(file)
