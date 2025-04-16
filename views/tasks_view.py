#!/usr/bin/env python3
from rich.console import Console
from rich.table import Table
from typing import Dict, List, Union
from models.task import Task

console = Console()
# This is the console object that will be used to print messages to the console. It contains
# The main function here is render_responses, which will call the two others functions to render (1)the task and (2)task list.
# The console object is initialized with a custom theme for better readability.
# The render_response function takes a response dictionary and checks its status. Depending on the status, it will call either render_task or render_task_list to display the task details or a list of tasks.
# The render_task function takes a single task object and prints its details to the console.
# The render_task_list function takes a list of task objects and prints them in a table format for better readability.
# This is the main function that will be called to render the response from the CLI commands.


def render_response(response: Dict) -> None: #This function will take the response from the CLI commands and render it to the console. So this encapsulates the rendering of the response.
    """Render the response from CLI commands"""
    status = response.get("status")
   #Status of the response after request 
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
    console.print(f"\n[bold]Task Details[/bold]", style="red")
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
