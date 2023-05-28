import pytest


@pytest.fixture()
def tagcategories_names(tagcategories_api):
    # Note: tag type name is unique
    return {tag_category.name for tag_category in tagcategories_api.tagcategories_get()}


@pytest.fixture()
def tagcategories_ids(tagcategories_api):
    # Note: tag type ID is unique
    return {tag_category.id for tag_category in tagcategories_api.tagcategories_get()}


@pytest.fixture()
def tag_names(tags_api):
    # Note: tag name is unique
    return {tag.name for tag in tags_api.tags_get()}
