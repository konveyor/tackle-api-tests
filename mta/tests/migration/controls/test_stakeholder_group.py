import pytest
from pytest_check import check

from conftest import generate_string


@pytest.mark.sg
def test_stakeholder_group_crud(stakeholder_group, get_api, delete_api, update_api):
    # get stakeholder_group_from_db
    stakeholder_group_from_db = get_api.stakeholdergroups_id_get(stakeholder_group.id)

    # Assertion checking the created stakeholder group's name and description
    check.equal(stakeholder_group_from_db.name, stakeholder_group.name)
    check.equal(stakeholder_group_from_db.description, stakeholder_group.description)

    # Edit the stakeholder group's name and description
    stakeholder_group.name = generate_string(start="update name")
    stakeholder_group.description = generate_string(start="update description")
    update_api.stakeholdergroups_id_put(stakeholder_group.id, stakeholder_group.to_dict())
    update_stakeholder_group_from_db = get_api.stakeholdergroups_id_get(stakeholder_group.id)
    # Assertion checking for the updated stakeholder group's name
    check.equal(update_stakeholder_group_from_db.name, stakeholder_group.name)
    # Assertion checking for the updated stakeholder group's description
    check.equal(update_stakeholder_group_from_db.description, stakeholder_group.description)
