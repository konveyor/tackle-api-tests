import pytest

from conftest import generate_string
from swagger_client.models.api_business_service import ApiBusinessService


@pytest.fixture(scope="function")
def business_service(stakeholder, businessservices_api):
    api_business_service = ApiBusinessService(
        name=generate_string(start="business service"), description=generate_string(length=120), owner=stakeholder
    )
    new_business_service = businessservices_api.businessservices_post(api_business_service.to_dict())

    yield new_business_service
    businessservices_api.businessservices_id_delete(str(new_business_service.id))
