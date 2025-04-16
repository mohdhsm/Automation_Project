#!/usr/bin/env python3
from rich.console import Console
from rich.table import Table
from typing import Dict, List, Union
from models.task import Task

console = Console()

def render_response(response: Dict) -> None:
    """Render the response from CLI commands"""
    status = response.get("status")
    
    if status == "success":
        if "task" in response:
            render_task(response["task"])
        elif "tasks" in response:
            render_task_list(response["tasks"])
        elif "message" in response:
            console.print(f"✅ {response['message']}", style="success")
    elif status == "error":
        console.print(f"❌ {response['message']}", style="error")
    elif status == "cancelled":
        console.print(f"⚠️ {response['message']}", style="warning")

def render_task(task: Task) -> None:
    """Render a single task"""
    console.print(f"\n[bold]Task Details[/bold]", style="info")
    console.print(f"ID: {task.id}")
    console.print(f"Title: {task.title}")
    console.print(f"Description: {task.description}")
    console.print(f"Deadline: {task.deadline}")
    console.print(f"Assigned To: {task.assigned_to}")
    console.print(f"Status: {task.status}")

def render_task_list(tasks: List[Task]) -> None:
    """Render a table of tasks"""
    table = Table(title="All Tasks")
    table.add_column("ID", style="cyan")
    table.add_column("Title")
    table.add_column("Description")
    table.add_column("Deadline")
    table.add_column("Assigned To")
    table.add_column("Status")
    
    for task in tasks:
        table.add_row(
            str(task.id),
            task.title,
            task.description,
            str(task.deadline),
            task.assigned_to,
            task.status
        )
    console.print(table)
