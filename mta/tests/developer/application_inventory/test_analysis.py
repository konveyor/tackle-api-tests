import pytest
from wait_for import wait_for


@pytest.mark.analysis
@pytest.mark.parametrize("tasks", ["source_applications"], indirect=True)
def test_source_analysis(tasks, get_api):
    for task in tasks:
        wait_for(lambda: get_api.tasks_id_get(str(task.id)).state == "Succeeded", delay=5, timeout=300)


@pytest.mark.analysis
@pytest.mark.parametrize("tasks", ["binary_applications"], indirect=True)
def test_binary_analysis(tasks, get_api):
    for task in tasks:
        wait_for(lambda: get_api.tasks_id_get(str(task.id)).state == "Succeeded", delay=5, timeout=300)


@pytest.mark.analysis
@pytest.mark.parametrize("tasks", ["source_binary_apps"], indirect=True)
def test_source_with_deps_analysis(tasks, get_api):
    for task in tasks:
        wait_for(lambda: get_api.tasks_id_get(str(task.id)).state == "Succeeded", delay=5, timeout=300)
