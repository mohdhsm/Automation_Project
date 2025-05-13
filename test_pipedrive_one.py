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

    def format_nested(value, indent=0):
        """Recursively format nested dictionaries"""
        if not isinstance(value, dict):
            return str(value)
        
        lines = []
        for k, v in value.items():
            if isinstance(v, dict):
                lines.append(f"[bold]{'  '*indent}{k}:[/bold]")
                lines.append(format_nested(v, indent+1))
            else:
                lines.append(f"[bold]{'  '*indent}{k}:[/bold] {v}")
        return "\n".join(lines)

    for item in data:
        row = []
        for key in data[0].keys():
            value = item.get(key, '')
            row.append(format_nested(value))
        table.add_row(*row)
    
    console.print(table)

def main():
    """Test all Pipedrive API methods"""
    pd = PipedriveService()
    data = pd.get_all_deals() 
    console.print("[bold]Testing Pipedrive API Methods[/bold]\n")
    display_results("Testing ALL API",data)# Test all main API methods
    # Here he added all the API's method in a list of tuples, for each of use.
   

if __name__ == "__main__":
    main()
