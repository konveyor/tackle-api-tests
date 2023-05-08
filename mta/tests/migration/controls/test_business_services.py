import pytest
from pytest_check import check

from conftest import generate_string


@pytest.mark.bs
def test_business_service_crud(business_service, stakeholder, get_api, delete_api, update_api):
    # get business_service_from_db
    business_service_from_db = get_api.businessservices_id_get(business_service.id)

    # Assertion checking the created business services's name
    check.equal(business_service_from_db.name, business_service.name)

    # Edit the BS name and description
    business_service.name = generate_string(start="update name")
    business_service.description = generate_string(length=120, start="update description")
    update_api.businessservices_id_put(business_service.id, business_service.to_dict())
    update_business_service_from_db = get_api.businessservices_id_get(business_service.id)
    # Assertion checking for the updated business services's name
    check.equal(update_business_service_from_db.name, business_service.name)
    # Assertion checking for the updated business services's description
    check.equal(update_business_service_from_db.description, business_service.description)
