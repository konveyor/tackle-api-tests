import pytest


@pytest.fixture()
def tag_types_names(get_api):
    # Note: tag type name is unique
    return {tag_type.name for tag_type in get_api.tagtypes_get()}


@pytest.fixture()
def tag_types_ids(get_api):
    # Note: tag type ID is unique
    return {tag_type.id for tag_type in get_api.tagtypes_get()}


@pytest.fixture()
def tag_names(get_api):
    # Note: tag name is unique
    return {tag.name for tag in get_api.tags_get()}
