#!/usr/bin/env python3
from uuid import UUID, uuid4
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
        self.id = id or uuid4()
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

    _storage: Dict[UUID, 'Meeting'] = {}

    @classmethod
    def get(cls, id: UUID) -> Optional['Meeting']:
        """Get a meeting by ID"""
        return cls._storage.get(id)

    @classmethod
    def get_all(cls) -> List['Meeting']:
        """Get all meetings"""
        return list(cls._storage.values())

    @classmethod
    def update(cls, id: UUID, updates: Dict) -> Optional['Meeting']:
        """Update a meeting"""
        meeting = cls._storage.get(id)
        if not meeting:
            return None
            
        for key, value in updates.items():
            setattr(meeting, key, value)
        return meeting

    @classmethod
    def delete(cls, id: UUID) -> bool:
        """Delete a meeting"""
        if id in cls._storage:
            del cls._storage[id]
            return True
        return False

    def is_one_on_one(self) -> bool:
        """Check if meeting is one-on-one"""
        return self.meeting_type == "one_on_one"

    def is_group(self) -> bool:
        """Check if meeting is group"""
        return self.meeting_type == "group"
