import pytest

from conftest import generate_email, generate_string
from swagger_client.models.api_stakeholder import ApiStakeholder


@pytest.fixture(scope="function")
def stakeholder(stakeholder_group, job_function, stakeholders_api):

    #   Create a Stakeholder with email and name
    api_stakeholder = ApiStakeholder(
        email=generate_email(),
        name=generate_string(start="stakeholder"),
        job_function=job_function,
        stakeholder_groups=stakeholder_group,
    )
    new_stakeholder = stakeholders_api.stakeholders_post(api_stakeholder.to_dict())

    yield new_stakeholder
    stakeholders_api.stakeholders_id_delete(str(new_stakeholder.id))
