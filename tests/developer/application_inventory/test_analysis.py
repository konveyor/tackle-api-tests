import pytest
from wait_for import wait_for


@pytest.mark.analysis
def test_analysis(task_groups, get_api):
    for task_group in task_groups:
        tasks = task_group.tasks
        for task in tasks:
            wait_for(lambda: get_api.tasks_id_get(str(task.id)).state == "Succeeded", delay=5, timeout=120)

