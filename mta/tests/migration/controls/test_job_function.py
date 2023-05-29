import pytest
from pytest_check import check

from conftest import generate_string


@pytest.mark.job_function
def test_job_function_crud(job_function, jobfunctions_api):
    # get job_function_from_db
    job_function_from_db = jobfunctions_api.jobfunctions_id_get(job_function.id)

    # Assertion checking the created job function name
    check.equal(job_function_from_db.name, job_function.name)

    # Edit the job function name
    job_function.name = generate_string(start="update name")
    jobfunctions_api.jobfunctions_id_put(job_function.id, job_function.to_dict())
    updated_job_function_from_db = jobfunctions_api.jobfunctions_id_get(job_function.id)
    # Assertion checking for the updated job function name
    check.equal(updated_job_function_from_db.name, job_function.name)
