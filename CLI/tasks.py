#!/usr/bin/env python3
import typer
from typing import Optional, List, Dict, Union
from datetime import datetime
from models.task import Task
from controllers.task_controller import TaskController

app = typer.Typer(help="Manage tasks and goals")
controller = TaskController()

@app.command()
def create(
    title: str = typer.Option(..., prompt=True, help="Title of the task"),
    description: str = typer.Option(..., prompt=True, help="Description of the task"),
    deadline: str = typer.Option(..., prompt=True, help="Deadline in YYYY-MM-DD format"),
    assigned_to: str = typer.Option(..., prompt=True, help="Name of person assigned")
) -> Dict[str, Union[str, Task]]:
    """Create a new task"""
    try:
        deadline_date = datetime.strptime(deadline, "%Y-%m-%d").date()
        task = Task(
            title=title,
            description=description,
            deadline=deadline_date,
            assigned_to=assigned_to
        )
        created_task = controller.create_task(task)
        return {"status": "success", "task": created_task}
    except ValueError as e:
        return {"status": "error", "message": str(e)}
## THESE ARE THE COMMAND
@app.command()
def view(
    task_id: Optional[str] = typer.Argument(None, help="ID of task to view"),
    all: bool = typer.Option(False, "--all", help="View all tasks")
) -> Dict[str, Union[str, Task, List[Task]]]: #Why we used union? Because it gives the option of using a String, icnase of error, or a task or list of tasks.
    """View task(s)"""
    try:
        if all:
            tasks = controller.get_all_tasks()
            return {"status": "success", "tasks": tasks}
        elif task_id:
            task = controller.get_task(task_id)
            return {"status": "success", "task": task}
        else:
            return {"status": "error", "message": "Please specify either --all or a task ID"}
    except Exception as e:
        return {"status": "error", "message": str(e)}

@app.command()
def edit(
    task_id: str = typer.Argument(..., help="ID of task to edit"),
    title: Optional[str] = typer.Option(None, help="New title"),
    description: Optional[str] = typer.Option(None, help="New description"),
    deadline: Optional[str] = typer.Option(None, help="New deadline in YYYY-MM-DD format"),
    status: Optional[str] = typer.Option(None, help="New status (pending, in_progress, completed)")
) -> Dict[str, Union[str, Task]]:
    """Edit an existing task"""
    try:
        updates = {}
        if title:
            updates["title"] = title
        if description:
            updates["description"] = description
        if deadline:
            updates["deadline"] = datetime.strptime(deadline, "%Y-%m-%d").date()
        if status:
            updates["status"] = status
            
        if not updates:
            return {"status": "error", "message": "No updates provided"}
            
        updated_task = controller.update_task(task_id, updates)
        return {"status": "success", "task": updated_task}
    except Exception as e:
        return {"status": "error", "message": str(e)}

@app.command()
def delete(
    task_id: str = typer.Argument(..., help="ID of task to delete"),
    force: bool = typer.Option(False, "--force", help="Skip confirmation")
) -> Dict[str, str]:
    """Delete a task"""
    try:
        if not force:
            confirm = typer.confirm(f"Are you sure you want to delete task {task_id}?")
            if not confirm:
                return {"status": "cancelled", "message": "Deletion cancelled"}
                
        controller.delete_task(task_id)
        return {"status": "success", "message": f"Task {task_id} deleted"}
    except Exception as e:
        return {"status": "error", "message": str(e)}
