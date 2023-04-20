# project root conftest.py
import fauxfactory

pytest_plugins = [
    "mta.fixtures.apis",
    "mta.fixtures.application_inventory",
    "mta.fixtures.credentials",
    "mta.fixtures.tags",
    "mta.fixtures.stakeholder",
]


def generate_name(length=20, start=None, separator="-"):
    """Generate a random credential name."""
    return fauxfactory.gen_alphanumeric(length=length, start=start + "-creds", separator=separator)


def generate_email():
    """Generate a random credential name."""
    return fauxfactory.gen_email()
