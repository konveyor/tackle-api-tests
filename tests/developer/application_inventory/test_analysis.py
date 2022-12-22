import pytest
from fixtures.application_inventory import *


@pytest.mark.analysis
def test_create_app_git(git_application, get_api):
    app_from_db = get_api.applications_id_get(git_application.id)
    assert git_application == app_from_db
