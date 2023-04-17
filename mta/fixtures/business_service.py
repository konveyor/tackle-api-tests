import pytest

from conftest import generate_string
from swagger_client.models.api_business_service import ApiBusinessService


@pytest.fixture(scope="session")
def business_service(stakeholder, create_api, get_api):
    api_business_service = ApiBusinessService(
        name=generate_string(start="business service"), description=generate_string(length=120), owner=stakeholder
    )
    new_business_service = create_api.businessservices_post(api_business_service.to_dict())

    return new_business_service
