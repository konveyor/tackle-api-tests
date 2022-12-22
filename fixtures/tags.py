import pytest


@pytest.fixture()
def tag_types_names(get_api):
    return [tag.name for tag in get_api.tagtypes_get()]


@pytest.fixture()
def tag_types_ids(get_api):
    return [tag.id for tag in get_api.tagtypes_get()]
