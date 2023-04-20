import pytest
from pytest_check import check

from swagger_client.models.api_business_service import ApiBusinessService
from swagger_client.models.api_stakeholder import ApiStakeholder


@pytest.mark.business_service
def test_create_business_service(stakeholder, create_api, get_api, delete_api, update_api):
    #   Create a Stakeholder with email and name
    #         api_stakeholder = ApiStakeholder( email="xyz@gmail.com", name="Api stakeholder")
    #         new_stakeholder = create_api.stakeholders_post(api_stakeholder.to_dict())

    #   Create a BS with name, description and Owner
    api_business_service = ApiBusinessService(name="Api Business", description="Api Testing", owner=stakeholder)
    new_business = create_api.businessservices_post(api_business_service.to_dict())
    new_business_from_db = get_api.businessservices_id_get(new_business.id)

    #   Assertion checking the created business services's name"
    check.equal(new_business_from_db.name, new_business.name)

    #   Edit an BS name and description
    api_business_service.name = "update business name"
    api_business_service.description = "update description"
    update_api.businessservices_id_put(new_business.id, api_business_service.to_dict())

    #   Delete the BS
    delete_api.businessservices_id_delete(str(new_business.id))
    delete_api.stakeholders_id_delete(str(stakeholder.id))
