
import json

import pytest

from task_manager import TaskManager


def test_add_task_creates_store_and_assigns_id(tmp_path):
    manager = TaskManager(tmp_path / "tasks.json")

    task = manager.add_task("  Study Gitflow  ", "high")

    assert task == {
        "id": 1,
        "title": "Study Gitflow",
        "priority": "high",
        "completed": False,
    }
    assert manager.list_tasks() == [task]


def test_task_ids_increment_after_existing_tasks(tmp_path):
    manager = TaskManager(tmp_path / "tasks.json")
    first = manager.add_task("First")
    second = manager.add_task("Second")

    assert first["id"] == 1
    assert second["id"] == 2


@pytest.mark.parametrize("title", ["", "   ", "\n"])
def test_empty_title_is_rejected(tmp_path, title):
    manager = TaskManager(tmp_path / "tasks.json")

    with pytest.raises(ValueError, match="cannot be empty"):
        manager.add_task(title)


def test_invalid_priority_is_rejected(tmp_path):
    manager = TaskManager(tmp_path / "tasks.json")

    with pytest.raises(ValueError, match="Priority must be"):
        manager.add_task("A task", "urgent")


def test_complete_task_marks_task_completed(tmp_path):
    manager = TaskManager(tmp_path / "tasks.json")
    manager.add_task("Finish project")

    completed = manager.complete_task(1)

    assert completed["completed"] is True


def test_missing_task_cannot_be_completed(tmp_path):
    manager = TaskManager(tmp_path / "tasks.json")

    with pytest.raises(KeyError, match="No task found"):
        manager.complete_task(99)


def test_delete_task_removes_task(tmp_path):
    manager = TaskManager(tmp_path / "tasks.json")
    manager.add_task("Remove me")

    manager.delete_task(1)

    assert manager.list_tasks() == []


def test_corrupt_json_is_reported(tmp_path):
    store = tmp_path / "tasks.json"
    store.write_text("{broken", encoding="utf-8")
    manager = TaskManager(store)

    with pytest.raises(ValueError, match="not valid JSON"):
        manager.list_tasks()


def test_store_is_valid_json(tmp_path):
    store = tmp_path / "tasks.json"
    manager = TaskManager(store)
    manager.add_task("Persisted")

    assert json.loads(store.read_text(encoding="utf-8"))[0]["title"] == "Persisted"


def test_empty_title_does_not_create_store(tmp_path):
    store = tmp_path / "tasks.json"
    manager = TaskManager(store)

    with pytest.raises(ValueError, match="cannot be empty"):
        manager.add_task("   ")

    assert not store.exists()
