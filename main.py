#!/usr/bin/env python3
import typer
import rich
from rich.console import Console
from rich.theme import Theme
import logging
from dotenv import load_dotenv

# Import CLI command groups
from CLI.tasks import app as tasks_app
from CLI.meeting import app as meetings_app
# from CLI.sales import app as sales_app
# from CLI.reports import app as reports_app

# Initialize rich console with custom theme
custom_theme = Theme({
    "success": "green",
    "error": "bold red",
    "warning": "yellow",
    "info": "blue",
    "highlight": "bold cyan"
})
console = Console(theme=custom_theme)
def check():
    """Check if the CLI is running correctly"""
    console.print("CLI is running correctly!", style="success")
# Load environment variables
load_dotenv()

# Create main Typer app
app = typer.Typer(
    name="Automation CLI",
    help="Automation tool for tasks, meetings, sales and reporting",
    rich_markup_mode="rich"
)

# Add command groups 
app.add_typer(tasks_app, name="tasks", help="Manage tasks") # added commands from group tasks
app.add_typer(meetings_app, name="meetings", help="Manage meetings and transcripts") #added from meetings app
# app.add_typer(sales_app, name="sales", help="Pipedrive sales integration")
# app.add_typer(reports_app, name="reports", help="Generate reports")

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

def main():
    """Entry point for the CLI application"""
    try:
        console.rule("[bold red]MOHAMMED ALHASHIM AUTOMATION APP", style="highlight")
        console.print("[bold red]Automation CLI - Starting up...", style="info")
        app()
    except Exception as e:
        console.print(f"Error: {e}", style="error")
        raise typer.Exit(code=1)

if __name__ == "__main__":
    main()
