from rich.console import Console
from rich.table import Table
from typing import List, Dict

console = Console()

def display_deals_table(deals: List[Dict], title: str = "Deals"):
    """Display deals in a rich table"""
    table = Table(title=title, show_header=True, header_style="bold magenta")
    
    # Define columns
    table.add_column("ID", style="cyan")
    table.add_column("Title", style="green")
    table.add_column("Value", style="yellow")
    table.add_column("Status", style="blue")
    table.add_column("Stage", style="magenta")
    table.add_column("Owner", style="cyan")
    table.add_column("Created", style="green")
    
    # Add rows
    for deal in deals:
        table.add_row(
            str(deal.get('id', '')),
            deal.get('title', 'N/A'),
            str(deal.get('value', 0)),
            deal.get('status', 'N/A'),
            deal.get('stage_id', 'N/A'),
            str(deal.get('owner_id', 'N/A')),
            deal.get('created', 'N/A')
        )
    
    console.print(table)

def display_sales_report(report_data: Dict):
    """Display sales report summary"""
    table = Table(title="Sales Report Summary", show_header=True, header_style="bold blue")
    
    table.add_column("Metric", style="cyan")
    table.add_column("Current", style="green")
    table.add_column("Previous", style="yellow")
    table.add_column("Change", style="magenta")
    
    for metric, values in report_data.items():
        current = values.get('current', 0)
        previous = values.get('previous', 0)
        change = current - previous
        change_pct = (change / previous * 100) if previous != 0 else float('inf')
        
        table.add_row(
            metric,
            str(current),
            str(previous),
            f"{change} ({change_pct:.1f}%)"
        )
    
    console.print(table)

def display_salesperson_report(person_data: Dict):
    """Display detailed report for a salesperson"""
    console.rule(f"[bold green]Salesperson Report: {person_data.get('name', '')}")
    
    # Summary table
    summary_table = Table(show_header=True, header_style="bold blue")
    summary_table.add_column("Metric", style="cyan")
    summary_table.add_column("Value", style="green")
    
    for metric, value in person_data.get('summary', {}).items():
        summary_table.add_row(metric, str(value))
    
    console.print(summary_table)
    
    # Recent deals table
    if person_data.get('recent_deals'):
        display_deals_table(person_data['recent_deals'], "Recent Deals")
    
    # Stalled deals table
    if person_data.get('stalled_deals'):
        display_deals_table(person_data['stalled_deals'], "Stalled Deals")
