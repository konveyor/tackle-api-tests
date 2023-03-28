import pytest


@pytest.fixture()
def tagcategories_names(get_api):
    # Note: tag type name is unique
    return {tag_category.name for tag_category in get_api.tagcategories_get()}


@pytest.fixture()
def tagcategories_ids(get_api):
    # Note: tag type ID is unique
    return {tag_category.id for tag_category in get_api.tagcategories_get()}


@pytest.fixture()
def tag_names(get_api):
    # Note: tag name is unique
    return {tag.name for tag in get_api.tags_get()}
