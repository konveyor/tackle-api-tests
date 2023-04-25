import pytest

from conftest import generate_email, generate_string
from swagger_client.models.api_stakeholder import ApiStakeholder


@pytest.fixture(scope="session")
def stakeholder(create_api, get_api):

    #   Create a Stakeholder with email and name
    api_stakeholder = ApiStakeholder(email=generate_email(), name=generate_string(start="stakeholder"))
    new_stakeholder = create_api.stakeholders_post(api_stakeholder.to_dict())

    return new_stakeholder
