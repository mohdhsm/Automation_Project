import sys
from rich.console import Console
from rich.table import Table
from services.pipedrive_services import PipedriveService

console = Console()
# This is a general list to produce the result.
def display_results(title: str, data: list):
    """Display API results in a rich table"""
    if not data:
        console.print(f"[yellow]No {title} found[/yellow]")
        return

    table = Table(title=title, show_header=True, header_style="bold magenta")
    
    # Create columns based on first item's keys
    for key in data[0].keys():
        table.add_column(key, style="cyan")
    
    for item in data:
        row = []
        for key in data[0].keys():
            value = item.get(key, '')
            if isinstance(value, dict):
                # Format nested dictionaries
                formatted = []
                for k, v in value.items():
                    formatted.append(f"[bold]{k}[/bold]: {v}")
                row.append("\n".join(formatted))
            else:
                row.append(str(value))
        table.add_row(*row)
    
    console.print(table)

def main():
    """Test all Pipedrive API methods"""
    pd = PipedriveService()
    
    console.print("[bold]Testing Pipedrive API Methods[/bold]\n")
    
    # Test all main API methods
    # Here he added all the API's method in a list of tuples, for each of use.
    methods = [
        ("All Deals", pd.get_all_deals),
        ("All Persons", pd.get_all_persons),
        ("Deals Updated Today", pd.get_deals_updated_today),
        ("Deals Updated This Week", pd.get_deals_updated_this_week),
        ("Deals Updated This Month", pd.get_deals_updated_this_month),
        ("Stalled Deals", pd.get_stalled_deals),
        ("Inactive Deals", pd.get_inactive_deals),
        ("Recently Won Deals", pd.get_recently_won_deals),
        ("Aramco Projects", pd.get_aramco_projects),
        ("Deals by Stages", pd.get_deals_by_stages),
        ("New Deals Today", pd.get_new_deals_today),
        ("New Deals This Week", pd.get_new_deals_this_week),
        ("New Deals This Month", pd.get_new_deals_this_month),
    ]
    
    for name, method in methods:
        console.print(f"[bold blue]Testing: {name}[/bold blue]")
        try:
            data = method()
            display_results(name, data)
        except Exception as e:
            console.print(f"[red]Error testing {name}: {str(e)}[/red]")
        console.print()  # Add spacing between tests

if __name__ == "__main__":
    main()
