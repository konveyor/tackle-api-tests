import pytest
from wait_for import wait_for


@pytest.mark.analysis
def test_source_analysis(tasks, get_api):
    for task in tasks:
        wait_for(lambda: get_api.tasks_id_get(str(task.id)).state == "Succeeded", delay=5, timeout=180)
