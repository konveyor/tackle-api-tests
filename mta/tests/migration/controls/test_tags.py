import pytest
from pytest_check import check

from conftest import generate_string
from swagger_client.models.api_ref import ApiRef
from swagger_client.models.api_tag import ApiTag


@pytest.mark.tags
def test_create_tag(tagcategories_ids, tags_api):
    for tag_category_id in tagcategories_ids:
        tag_category = ApiRef(id=tag_category_id)
        api_tag = ApiTag(category=tag_category, name=generate_string(start="Api Tag"))
        new_tag = tags_api.tags_post(api_tag)
        new_tag_from_db = tags_api.tags_id_get(str(new_tag.id))
        check.equal(new_tag_from_db.name, new_tag.name, "Checking the created tag's name")
        tags_api.tags_id_delete(str(new_tag.id))
