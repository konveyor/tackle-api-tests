import pytest
from pytest_check import check


@pytest.mark.tags
def test_default_tags(json_defaults, tag_names):
    assert set(json_defaults["tags"]).issubset(tag_names), "Default tags check FAILED! (found : expected)"  # noqa: E501


@pytest.mark.tags
def test_default_tag_types(json_defaults, tag_types_names):
    assert set(json_defaults["tag_types"]).issubset(tag_types_names), "Default tag types check FAILED!"


@pytest.mark.xfail  # TODO: Remove once related bug is fixed, Jira: TACKLE-893
@pytest.mark.tags
def test_create_tag(tag_types_ids, create_api, get_api, delete_api):
    for tagtype_id in tag_types_ids:
        tag_data = {"name": "Api Tag", "tagType": {"id": tagtype_id}}
        new_tag = create_api.tags_post(tag_data)
        new_tag_from_db = get_api.tags_id_get(new_tag.id)
        check.equal(new_tag_from_db, new_tag, "Checking the created tag")
        delete_api.tags_id_delete(str(new_tag.id))
