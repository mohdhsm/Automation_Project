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

@app.command() # The create command will create a meeting object, and then call the controller to create it in the storage. Controller will call the model to create it in the database.
def create( # we use ... to indicates that its a required field.
    meeting_type: str = typer.Option(..., prompt=True, help="Type of meeting (e.g., 'team', 'client')"),
    date: str = typer.Option(..., prompt=True, help="Date of meeting in YYYY-MM-DD format"),
    summary: str = typer.Option(..., prompt=True, help="Summary of the meeting"),
    participants: List[UUID] = typer.Option(..., prompt=True, help="List of participant UUIDs"),
) -> Dict[str, Union[str, Meeting]]: 
    """ CREATE A NEW MEETING"""
    try:
        meeting_date = datetime.strptime(date, "%Y-%m-%d").date() # convert the date string to a date object
        meeting = Meeting( # create a new meeting object
            meeting_type=meeting_type,
            date=meeting_date,
            summary=summary,
            participants=participants
        )
        created_meeting = controller.create_meeting(meeting) # call the controller to create the meeting
        return {"status": "success", "meeting": created_meeting} # return the status and the created meeting object
    except ValueError as e:
        return {"status": "error", "message": str(e)} 

@app.command()
def view(meeting_id:int = typer.Option(...,prompt=True, help="meeting ID")) -> Dict[str, Union[str, Meeting]]:
    """ VIEW A MEETING"""

    try:
        meeting = controller.get_meeting(meeting_id) # call the controller to get the meeting based on its ID 
        if not meeting:
            raise ValueError(f"Meeting {meeting_id} not found")
        return {"status": "success", "meeting": meeting} # return the status and the meeting object
    except ValueError as e:
        return {"status": "error", "message": str(e)}

@app.command()
def view_all() -> Dict[str, Union[str, List[Meeting]]]:
    """ VIEW ALL MEETINGS"""
    try:
        meetings = controller.get_all_meetings() # call the controller to get all meetings
        return {"status": "success", "meetings": meetings} # return the status and the list of meetings
    except Exception as e:
        return {"status": "error", "message": str(e)}

# This function takes in the meeting ID and the updates to be made. It will call the controller to update the meeting in the storage.
@app.command()
def edit_meeting( meeting_id: int = typer.Arguement(...,help="The ID of the meeting to edit")-> None:
    """ EDIT A MEETING"""
 # update this later on TODO 
    # return {"status": "error", "message": str(e)}
    
