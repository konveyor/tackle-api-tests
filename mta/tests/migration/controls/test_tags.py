import pytest
from pytest_check import check

from swagger_client.models.api_tag import ApiTag


@pytest.mark.tags
def test_create_tag(tagcategories_ids, create_api, get_api, delete_api):
    for tag_category_id in tagcategories_ids:
        tag_category = {"id": tag_category_id}
        api_tag = ApiTag(category=tag_category, name="Api Tag")
        new_tag = create_api.tags_post(api_tag.to_dict())
        new_tag_from_db = get_api.tags_id_get(new_tag.id)
        check.equal(new_tag_from_db.name, new_tag.name, "Checking the created tag's name")
        delete_api.tags_id_delete(str(new_tag.id))
