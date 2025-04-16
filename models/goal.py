#!/usr/bin/env python3
from uuid import UUID
from datetime import datetime
from typing import Optional, Dict, List
from .base import BaseModel

class Goal(BaseModel):
    """Goal model representing organizational objectives"""
    
    def __init__(
        self,
        title: str,
        description: str,
        deadline: datetime,
        progress: int = 0,
        progress_summary: str = "",
        next_checkup: Optional[datetime] = None,
        notes: Optional[List[UUID]] = None,
        contributors: Optional[List[UUID]] = None,
        id: Optional[UUID] = None,
        created_at: Optional[datetime] = None
    ):
        self.id = id or uuid4()
        self.title = title
        self.description = description
        self.created_at = created_at or datetime.now()
        self.deadline = deadline
        self.progress = progress
        self.progress_summary = progress_summary
        self.next_checkup = next_checkup or datetime.now()
        self.notes = notes or []
        self.contributors = contributors or []

    @classmethod
    def create(cls, data: Dict) -> 'Goal':
        """Create a new goal"""
        return cls(**data)

    @classmethod
    def get(cls, id: UUID) -> Optional['Goal']:
        """Get a goal by ID"""
        # Implementation depends on database backend
        raise NotImplementedError

    @classmethod
    def get_all(cls) -> List['Goal']:
        """Get all goals"""
        # Implementation depends on database backend
        raise NotImplementedError

    @classmethod
    def update(cls, id: UUID, updates: Dict) -> Optional['Goal']:
        """Update a goal"""
        # Implementation depends on database backend
        raise NotImplementedError

    @classmethod
    def delete(cls, id: UUID) -> bool:
        """Delete a goal"""
        # Implementation depends on database backend
        raise NotImplementedError

    def update_progress(self, new_progress: int, summary: str) -> None:
        """Update goal progress with validation"""
        if not 0 <= new_progress <= 100:
            raise ValueError("Progress must be between 0 and 100")
        self.progress = new_progress
        self.progress_summary = summary

    def add_contributor(self, employee_id: UUID) -> None:
        """Add a contributor to the goal"""
        if employee_id not in self.contributors:
            self.contributors.append(employee_id)
