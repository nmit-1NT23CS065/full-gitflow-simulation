
"""A small JSON-backed task manager for the Full Gitflow Simulation project."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

DEFAULT_STORE = Path("tasks.json")


class TaskManager:
    """Create, list, and complete tasks stored in a JSON file."""

    def __init__(self, store_path: Path = DEFAULT_STORE) -> None:
        self.store_path = Path(store_path)

    def _read(self) -> list[dict[str, Any]]:
        if not self.store_path.exists():
            return []
        try:
            data = json.loads(self.store_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            raise ValueError(
                f"Task store is not valid JSON: {self.store_path}"
            ) from exc
        if not isinstance(data, list):
            raise ValueError("Task store must contain a JSON list.")
        return data

    def _write(self, tasks: list[dict[str, Any]]) -> None:
        self.store_path.parent.mkdir(parents=True, exist_ok=True)
        self.store_path.write_text(
            json.dumps(tasks, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )

    def add_task(self, title: str, priority: str = "normal") -> dict[str, Any]:
        """Add a task and return it."""
        clean_title = title.strip()
        if not clean_title:
            raise ValueError("Task title cannot be empty.")
        if priority not in {"low", "normal", "high"}:
            raise ValueError("Priority must be low, normal, or high.")

        tasks = self._read()
        task = {
            "id": max((item.get("id", 0) for item in tasks), default=0) + 1,
            "title": clean_title,
            "priority": priority,
            "completed": False,
        }
        tasks.append(task)
        self._write(tasks)
        return task

    def list_tasks(self) -> list[dict[str, Any]]:
        """Return all tasks in ID order."""
        return sorted(self._read(), key=lambda item: item["id"])

    def complete_task(self, task_id: int) -> dict[str, Any]:
        """Mark a task as complete."""
        tasks = self._read()
        for task in tasks:
            if task.get("id") == task_id:
                task["completed"] = True
                self._write(tasks)
                return task
        raise KeyError(f"No task found with ID {task_id}.")

    def delete_task(self, task_id: int) -> None:
        """Delete a task by ID."""
        tasks = self._read()
        remaining = [task for task in tasks if task.get("id") != task_id]
        if len(remaining) == len(tasks):
            raise KeyError(f"No task found with ID {task_id}.")
        self._write(remaining)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="A simple command-line task manager.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    add_parser = subparsers.add_parser("add", help="Add a task.")
    add_parser.add_argument("title", help="Task title.")
    add_parser.add_argument(
        "--priority",
        choices=("low", "normal", "high"),
        default="normal",
    )

    subparsers.add_parser("list", help="List all tasks.")

    complete_parser = subparsers.add_parser("complete", help="Complete a task.")
    complete_parser.add_argument("task_id", type=int)

    delete_parser = subparsers.add_parser("delete", help="Delete a task.")
    delete_parser.add_argument("task_id", type=int)
    return parser


def main() -> int:
    args = build_parser().parse_args()
    manager = TaskManager()

    try:
        if args.command == "add":
            task = manager.add_task(args.title, args.priority)
            print(
                f"Added task #{task['id']}: {task['title']} "
                f"(priority: {task['priority']})"
            )
        elif args.command == "list":
            tasks = manager.list_tasks()
            if not tasks:
                print(
                    "No tasks yet. Add one with: "
                    'python task_manager.py add "Task title"'
                )
            for task in tasks:
                status = "x" if task["completed"] else " "
                print(f"[{status}] #{task['id']} [{task['priority']}] {task['title']}")
        elif args.command == "complete":
            task = manager.complete_task(args.task_id)
            print(f"Completed task #{task['id']}: {task['title']}")
        elif args.command == "delete":
            manager.delete_task(args.task_id)
            print(f"Deleted task #{args.task_id}")
    except (ValueError, KeyError) as exc:
        print(f"Error: {exc}")
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
