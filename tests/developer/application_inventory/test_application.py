import pytest


@pytest.mark.app
def test_create_app(applications, get_api):
    for app in applications:
        app_from_db = get_api.applications_id_get(app.id)
        assert app == app_from_db
