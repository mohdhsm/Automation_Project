#!/usr/bin/env python3
from typing import List
from models.meeting import Meeting
from datetime import datetime

class MeetingView:
    """View for displaying meeting information"""
    
    @staticmethod
    def display_meeting(meeting: Meeting) -> None:
        """Display single meeting details"""
        print(f"\nMeeting ID: {meeting.id}")
        print(f"Type: {meeting.meeting_type}")
        print(f"Date: {meeting.date}")
        print(f"Summary: {meeting.summary}")
        print(f"Participants: {len(meeting.participants)}")
        print(f"Created: {meeting.created_at}")

    @staticmethod
    def display_meetings(meetings: List[Meeting]) -> None:
        """Display list of meetings"""
        print("\nMeetings:")
        for i, meeting in enumerate(meetings, 1):
            print(f"{i}. {meeting.meeting_type} meeting on {meeting.date}")

    @staticmethod
    def display_meeting_created(meeting: Meeting) -> None:
        """Display meeting creation confirmation"""
        print(f"\nCreated new meeting: {meeting.meeting_type} on {meeting.date}")

    @staticmethod
    def display_meeting_updated(meeting: Meeting) -> None:
        """Display meeting update confirmation"""
        print(f"\nUpdated meeting: {meeting.meeting_type} on {meeting.date}")

    @staticmethod
    def display_meeting_deleted(meeting_id: str) -> None:
        """Display meeting deletion confirmation"""
        print(f"\nDeleted meeting with ID: {meeting_id}")

    @staticmethod
    def display_error(message: str) -> None:
        """Display error message"""
        print(f"\nError: {message}")
