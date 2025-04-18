#!/usr/bin/env python3
from uuid import UUID
from datetime import datetime
from Controllers.meeting_controller import MeetingController
from views.meeting_view import MeetingView
from models.meeting import Meeting
from typing import Optional, Dict, List, Union
import typer

controller = MeetingController()
view = MeetingView()

app = typer.Typer(help="Manage meetings")

@app.command()
def create(
    meeting_type: str = typer.Option(..., prompt=True, help="Type of meeting (e.g., 'team', 'client')"),
    date: str = typer.Option(..., prompt=True, help="Date of meeting in YYYY-MM-DD format"),
    summary: str = typer.Option(..., prompt=True, help="Summary of the meeting"),
    participants: List[UUID] = typer.Option(..., prompt=True, help="List of participant UUIDs"),
) -> Dict[str, Union[str, Meeting]]: 
    """CREATE A NEW MEETING"""
    try:
        meeting_date = datetime.strptime(date, "%Y-%m-%d").date()
        meeting = Meeting(
            meeting_type=meeting_type,
            date=meeting_date,
            summary=summary,
            participants=participants
        )
        created_meeting = controller.create_meeting(meeting)
        return {"status": "success", "meeting": created_meeting}
    except ValueError as e:
        return {"status": "error", "message": str(e)} 

@app.command()
def view(meeting_id: UUID = typer.Option(..., prompt=True, help="meeting ID")) -> Dict[str, Union[str, Meeting]]:
    """VIEW A MEETING"""
    try:
        meeting = controller.get_meeting(meeting_id)
        if not meeting:
            raise ValueError(f"Meeting {meeting_id} not found")
        return {"status": "success", "meeting": meeting}
    except ValueError as e:
        return {"status": "error", "message": str(e)}

@app.command()
def view_all() -> Dict[str, Union[str, List[Meeting]]]:
    """VIEW ALL MEETINGS"""
    try:
        meetings = controller.get_all_meetings()
        return {"status": "success", "meetings": meetings}
    except Exception as e:
        return {"status": "error", "message": str(e)}

@app.command()
def edit_meeting(meeting_id: UUID = typer.Argument(..., help="The ID of the meeting to edit")) -> Dict[str, Union[str, Meeting]]:
    """Edit a meeting interactively"""
    try:
        # Get existing meeting
        meeting = controller.get_meeting(meeting_id)
        if not meeting:
            return {"status": "error", "message": f"Meeting {meeting_id} not found"}
        
        # Show current meeting details
        typer.echo("\nCurrent meeting details:")
        view.display_meeting(meeting)
        
        # Prompt for updates
        updates = {}
        new_type = typer.prompt(
            f"\nMeeting type (current: {meeting.meeting_type})", 
            default=meeting.meeting_type,
            show_default=False
        )
        if new_type != meeting.meeting_type:
            updates["meeting_type"] = new_type
            
        new_date = typer.prompt(
            f"Meeting date (YYYY-MM-DD) (current: {meeting.date})",
            default=meeting.date.strftime("%Y-%m-%d"),
            show_default=False
        )
        if new_date != meeting.date.strftime("%Y-%m-%d"):
            updates["date"] = datetime.strptime(new_date, "%Y-%m-%d").date()
            
        new_summary = typer.prompt(
            f"Summary (current: {meeting.summary})",
            default=meeting.summary,
            show_default=False
        )
        if new_summary != meeting.summary:
            updates["summary"] = new_summary
            
        # Only update if changes were made
        if updates:
            updated_meeting = controller.update_meeting(meeting_id, updates)
            return {"status": "success", "meeting": updated_meeting}
        return {"status": "success", "message": "No changes made"}
        
    except ValueError as e:
        return {"status": "error", "message": str(e)}
