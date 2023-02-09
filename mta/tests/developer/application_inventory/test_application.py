import pytest


@pytest.mark.app
def test_create_source_app(source_applications, get_api):
    for app in source_applications:
        app_from_db = get_api.applications_id_get(app.id)
        assert app == app_from_db


@pytest.mark.app
def test_create_binary_app(binary_applications, get_api):
    for app in binary_applications:
        app_from_db = get_api.applications_id_get(app.id)
        assert app == app_from_db
