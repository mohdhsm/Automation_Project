#!/usr/bin/env python3
import typer
from typing import Optional, List, Dict,Union
from Controllers.sales_controller import SalesController
from views.sales_view import display_deals_table, display_sales_report, display_salesperson_report

app = typer.Typer(help="Pipedrive sales integration")
controller = SalesController()

@app.command()
def deals(
    timeframe: Optional[str] = typer.Option(
        None, 
        "--timeframe", 
        "-t", 
        help="Timeframe filter (today/week/month)"
    )
) -> Dict[str, Union[str, List[Dict]]]:
    """View deals with optional timeframe filter"""
    try:
        if timeframe:
            deals = controller.get_deals_by_timeframe(timeframe)
        else:
            deals = controller.get_all_deals()
        
        display_deals_table(deals, f"Deals{f' ({timeframe})' if timeframe else ''}")
        return {"status": "success", "deals": deals}
    except Exception as e:
        return {"status": "error", "message": str(e)}

@app.command()
def stalled() -> Dict[str, Union[str, List[Dict]]]:
    """View deals not updated in 30+ days"""
    try:
        deals = controller.get_stalled_deals()
        display_deals_table(deals, "Stalled Deals (30+ days)")
        return {"status": "success", "deals": deals}
    except Exception as e:
        return {"status": "error", "message": str(e)}

@app.command()
def inactive() -> Dict[str, Union[str, List[Dict]]]:
    """View deals not updated in 60+ days"""
    try:
        deals = controller.get_inactive_deals()
        display_deals_table(deals, "Inactive Deals (60+ days)")
        return {"status": "success", "deals": deals}
    except Exception as e:
        return {"status": "error", "message": str(e)}

@app.command()
def won() -> Dict[str, Union[str, List[Dict]]]:
    """View deals won in last 30 days"""
    try:
        deals = controller.get_recently_won_deals()
        display_deals_table(deals, "Recently Won Deals")
        return {"status": "success", "deals": deals}
    except Exception as e:
        return {"status": "error", "message": str(e)}

@app.command()
def aramco() -> Dict[str, Union[str, List[Dict]]]:
    """View Aramco projects deals"""
    try:
        deals = controller.get_aramco_projects()
        display_deals_table(deals, "Aramco Projects")
        return {"status": "success", "deals": deals}
    except Exception as e:
        return {"status": "error", "message": str(e)}

@app.command()
def stages() -> Dict[str, Union[str, List[Dict]]]:
    """View deals in specific stages (Awaiting MDD/GR)"""
    try:
        deals = controller.get_deals_by_stages()
        display_deals_table(deals, "Deals in Specific Stages")
        return {"status": "success", "deals": deals}
    except Exception as e:
        return {"status": "error", "message": str(e)}

@app.command()
def person(
    name: str = typer.Argument(..., help="Sales person name")
) -> Dict[str, Union[str, Dict]]:
    """View deals by sales person"""
    try:
        deals = controller.get_deals_by_sales_person(name)
        display_deals_table(deals, f"Deals for {name}")
        return {"status": "success", "deals": deals}
    except Exception as e:
        return {"status": "error", "message": str(e)}

@app.command()
def summary() -> Dict[str, Union[str, Dict]]:
    """View sales summary report"""
    try:
        report = controller.get_sales_summary_report()
        display_sales_report(report)
        return {"status": "success", "report": report}
    except Exception as e:
        return {"status": "error", "message": str(e)}

@app.command()
def report(
    name: str = typer.Argument(..., help="Sales person name")
) -> Dict[str, Union[str, Dict]]:
    """View detailed salesperson report"""
    try:
        report = controller.get_salesperson_report(name)
        display_salesperson_report(report)
        return {"status": "success", "report": report}
    except Exception as e:
        return {"status": "error", "message": str(e)}
