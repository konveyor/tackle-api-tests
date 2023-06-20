import pytest
from pytest_check import check

from conftest import generate_string


@pytest.mark.stakeholder_groups
def test_stakeholder_group_crud(stakeholder_group, stakeholdergroups_api):
    # get stakeholder_group_from_db
    stakeholder_group_from_db = stakeholdergroups_api.stakeholdergroups_id_get(str(stakeholder_group.id))

    # Assertion checking the created stakeholder group's name and description
    check.equal(stakeholder_group_from_db.name, stakeholder_group.name)
    check.equal(stakeholder_group_from_db.description, stakeholder_group.description)

    # Edit the stakeholder group's name and description
    stakeholder_group.name = generate_string(start="update name")
    stakeholder_group.description = generate_string(start="update description")
    stakeholdergroups_api.stakeholdergroups_id_put(id=str(stakeholder_group.id), stakeholder_group=stakeholder_group)
    updated_stakeholder_group_from_db = stakeholdergroups_api.stakeholdergroups_id_get(str(stakeholder_group.id))
    # Assertion checking for the updated stakeholder group's name
    check.equal(updated_stakeholder_group_from_db.name, stakeholder_group.name)
    # Assertion checking for the updated stakeholder group's description
    check.equal(updated_stakeholder_group_from_db.description, stakeholder_group.description)
