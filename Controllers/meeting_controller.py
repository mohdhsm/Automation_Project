#!/usr/bin/env python3
from uuid import UUID
from datetime import datetime
from typing import Optional, Dict, List
from models.meeting import Meeting
import logging

class MeetingController:
    """Controller for managing meeting operations"""
    
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def create_meeting(self, meeting: Meeting) -> Meeting:
        """Create a new meeting with validation"""
        try:
            # Validate required fields
            if not all([meeting.meeting_type, meeting.date, meeting.summary]):
                raise ValueError("All meeting fields are required")
                
            # Store meeting in memory
            Meeting._storage[meeting.id] = meeting
            self.logger.info(f"Created meeting {meeting.id}")
            return meeting
            
        except Exception as e:
            self.logger.error(f"Error creating meeting: {e}")
            raise

    def get_meeting(self, meeting_id: UUID) -> Optional[Meeting]:
        """Retrieve a single meeting by ID"""
        try:
            meeting = Meeting.get(meeting_id)
            if not meeting:
                raise ValueError(f"Meeting {meeting_id} not found")
            self.logger.info(f"Retrieved meeting {meeting_id}")
            return meeting
        except Exception as e:
            self.logger.error(f"Error getting meeting {meeting_id}: {e}")
            raise

    def get_all_meetings(self) -> List[Meeting]:
        """Retrieve all meetings"""
        try:
            meetings = Meeting.get_all()
            self.logger.info(f"Retrieved {len(meetings)} meetings")
            return meetings
        except Exception as e:
            self.logger.error(f"Error getting all meetings: {e}")
            raise

    def update_meeting(self, meeting_id: UUID, updates: Dict) -> Optional[Meeting]:
        """Update an existing meeting"""
        try:
            # Validate updates
            if not updates:
                raise ValueError("No updates provided")
                
            updated_meeting = Meeting.update(meeting_id, updates)
            if not updated_meeting:
                raise ValueError(f"Meeting {meeting_id} not found")
            self.logger.info(f"Updated meeting {meeting_id} with {updates}")
            return updated_meeting
        except Exception as e:
            self.logger.error(f"Error updating meeting {meeting_id}: {e}")
            raise

    def delete_meeting(self, meeting_id: UUID) -> bool:
        """Delete a meeting"""
        try:
            success = Meeting.delete(meeting_id)
            if not success:
                raise ValueError(f"Meeting {meeting_id} not found")
            self.logger.info(f"Deleted meeting {meeting_id}")
            return success
        except Exception as e:
            self.logger.error(f"Error deleting meeting {meeting_id}: {e}")
            raise
