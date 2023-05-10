import pytest
from pytest_check import check

from conftest import generate_string


@pytest.mark.jf
def test_job_function_crud(job_function, get_api, update_api):
    # get job_function_from_db
    job_function_from_db = get_api.jobfunctions_id_get(job_function.id)

    # Assertion checking the created job function name
    check.equal(job_function_from_db.name, job_function.name)

    # Edit the job function name
    job_function.name = generate_string(start="update name")
    update_api.jobfunctions_id_put(job_function.id, job_function.to_dict())
    update_job_function_from_db = get_api.jobfunctions_id_get(job_function.id)
    # Assertion checking for the updated job function name
    check.equal(update_job_function_from_db.name, job_function.name)
