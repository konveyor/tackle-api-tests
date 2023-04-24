import pytest

from conftest import generate_string
from swagger_client.models.api_job_function import ApiJobFunction


@pytest.fixture(scope="function")
def job_function(create_api, get_api, delete_api):

    #   Create a job function with name
    api_job_function = ApiJobFunction(name=generate_string(start="job function"))
    new_job_function = create_api.jobfunctions_post(api_job_function.to_dict())

    yield new_job_function
    delete_api.jobfunctions_id_delete(str(new_job_function.id))
