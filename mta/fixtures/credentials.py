from contextlib import contextmanager
from xml.etree import ElementTree as ET

import pytest
from pytest_testconfig import config

from conftest import generate_string
from swagger_client.models.api_identity import ApiIdentity


@contextmanager
def create_credentials(credential_data, identities_api):
    api_identity = ApiIdentity(**credential_data)
    new_cred = identities_api.identities_post(api_identity)
    yield new_cred
    identities_api.identities_id_delete(str(new_cred.id))


@pytest.fixture(scope="session")
def source_username_credentials(identities_api):
    credential_data = {
        "name": generate_string(start="source-git-creds"),
        "kind": "source",
        "password": config.get("cred_git_token"),
        "user": config.get("cred_git_username"),
    }
    with create_credentials(credential_data=credential_data, identities_api=identities_api) as source_creds:
        yield source_creds


@pytest.fixture(scope="session")
def xml_maven_settings():
    # Parsing XML with Namespaces
    # For more information see:
    # https://docs.python.org/3/library/xml.etree.elementtree.html#parsing-xml-with-namespaces

    xml_origin = "mta/data/settings.xml"
    namespaces = {
        "parent_ns": "http://maven.apache.org/SETTINGS/1.2.0",
    }

    # Register the prefix and the namespace before reading the xml,
    # To avoid the default namespace prefixes (like ns0 and ns1, etc.)
    for key, value in namespaces.items():
        ET.register_namespace("", value)
    xml_tree = ET.parse(xml_origin)
    xml_tree.find(".//parent_ns:username", namespaces=namespaces).text = config.get("cred_git_username")
    xml_tree.find(".//parent_ns:password", namespaces=namespaces).text = config.get("cred_git_token")

    root = xml_tree.getroot()
    # convert to string
    yield ET.tostring(root, encoding="utf-8", method="xml").decode()


@pytest.fixture(scope="session")
def maven_credential(xml_maven_settings, identities_api):
    credential_data = {"name": generate_string(start="maven-creds"), "kind": "maven", "settings": xml_maven_settings}
    with create_credentials(credential_data=credential_data, identities_api=identities_api) as maven_creds:
        yield maven_creds
