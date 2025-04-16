#!/usr/bin/env python3
from uuid import uuid4
from datetime import datetime, timedelta
from models.task import Task
from Controllers.task_controller import TaskController
from views import tasks_view
import rich
from rich.console import Console
from rich.table import Table

def main():
    # Create controller
    controller = TaskController()
    console = Console()
    # Create sample tasks
    task1 = Task(
        title="Complete project",
        description="Finish the automation project",
        deadline=datetime.now() + timedelta(days=7),
        assigned_to=uuid4()
    )
    
    task2 = Task(
        title="Review code",
        description="Review team member's pull request",
        deadline=datetime.now() + timedelta(days=2),
        assigned_to=uuid4()
    )

    # Test create
    created1 = controller.create_task(task1)
    created2 = controller.create_task(task2)
    print(f"Created tasks: {created1.id}, {created2.id}")
    # Test view single
    tasks_view.render_task(created1)
    # Test get all
    all_tasks = controller.get_all_tasks()
    print(f"\nAll tasks ({len(all_tasks)}):")
    for task in all_tasks:
        print(f"- {task.title} (status: {task.status})")

    # Test get single
    single_task = controller.get_task(created1.id)
    print(f"\nSingle task: {single_task.title}")

    # Test update
    updated = controller.update_task(created2.id, {
        "status": "in_progress",
        "description": "Urgent code review needed"
    })
    print(f"\nUpdated task: {updated.description} (new status: {updated.status})")

    # Test delete
    deleted = controller.delete_task(created1.id)
    print(f"\nDeleted task {created1.id}: {deleted}")

    # Verify deletion
    remaining = controller.get_all_tasks()
    print(f"\nRemaining tasks ({len(remaining)}):")
    for task in remaining:
        print(f"- {task.title}")

if __name__ == "__main__":
    main()
