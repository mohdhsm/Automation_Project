#!/usr/bin/env python3
from uuid import UUID
from datetime import datetime
from typing import Optional, Dict, List
from .base import BaseModel

class Meeting(BaseModel):
    """Meeting model representing a scheduled meeting"""
    
    def __init__(
        self,
        meeting_type: str,
        date: datetime,
        summary: str,
        participants: List[UUID],
        id: Optional[UUID] = None,
        created_at: Optional[datetime] = None
    ):
        self.id = id #consider changing this because supabase will be using UUIDs.
        self.meeting_type = meeting_type
        self.date = date
        self.summary = summary
        self.participants = participants
        self.created_at = created_at or datetime.now()
    # 
    @classmethod
    def create(cls, data: Dict) -> 'Meeting':
        """Create a new meeting"""
        return cls(**data)

    @classmethod
    def get(cls, id: UUID) -> Optional['Meeting']:
        """Get a meeting by ID"""
        # Implementation depends on database backend
        raise NotImplementedError

    @classmethod
    def get_all(cls) -> List['Meeting']:
        """Get all meetings"""
        # Implementation depends on database backend
        raise NotImplementedError

    @classmethod
    def update(cls, id: UUID, updates: Dict) -> Optional['Meeting']:
        """Update a meeting"""
        # Implementation depends on database backend
        raise NotImplementedError

    @classmethod
    def delete(cls, id: UUID) -> bool:
        """Delete a meeting"""
        # Implementation depends on database backend
        raise NotImplementedError

    def is_one_on_one(self) -> bool:
        """Check if meeting is one-on-one"""
        return self.meeting_type == "one_on_one"

    def is_group(self) -> bool:
        """Check if meeting is group"""
        return self.meeting_type == "group"
