# project root conftest.py
import fauxfactory

pytest_plugins = [
    "mta.fixtures.apis",
    "mta.fixtures.application_inventory",
    "mta.fixtures.credentials",
    "mta.fixtures.tags",
    "mta.fixtures.stakeholder",
    "mta.fixtures.business_service",
    "mta.fixtures.stakeholder_group",
    "mta.fixtures.job_function",
]


def generate_string(length=20, start=None, separator="-"):
    """Generate a random string"""
    return fauxfactory.gen_alphanumeric(length=length, start=start, separator=separator)


def generate_email():
    """Generate a random email"""
    return fauxfactory.gen_email()
