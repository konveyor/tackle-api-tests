import pytest

from conftest import generate_string
from swagger_client.models.api_stakeholder_group import ApiStakeholderGroup


@pytest.fixture(scope="function")
def stakeholder_group(stakeholdergroups_api):

    #   Create a Stakeholder group with name and description
    api_stakeholder_group = ApiStakeholderGroup(
        name=generate_string(start="stakeholder group"), description=generate_string(length=120)
    )
    new_stakeholder_group = stakeholdergroups_api.stakeholdergroups_post(api_stakeholder_group.to_dict())
    yield new_stakeholder_group
    stakeholdergroups_api.stakeholdergroups_id_delete(str(new_stakeholder_group.id))
