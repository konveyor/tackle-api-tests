import pytest
from pytest_check import check

from conftest import generate_email, generate_string


@pytest.mark.stakeholder
def test_stakeholder_crud(stakeholder, get_api, delete_api, update_api):
    # get stakeholder_from_db
    stakeholder_from_db = get_api.stakeholders_id_get(stakeholder.id)

    # Assertion checking the created stakeholders name
    check.equal(stakeholder_from_db.name, stakeholder.name)

    # Edit the stakeholder name and description
    stakeholder.name = generate_string(start="update name")
    stakeholder.email = generate_email()
    update_api.stakeholders_id_put(stakeholder.id, stakeholder.to_dict())
    update_stakeholder_from_db = get_api.stakeholders_id_get(stakeholder.id)
    # Assertion checking for the updated stakeholders name
    check.equal(update_stakeholder_from_db.name, stakeholder.name)
    # Assertion checking for the updated stakeholders email
    check.equal(update_stakeholder_from_db.email, stakeholder.email)
