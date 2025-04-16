#!/usr/bin/env python3
from uuid import UUID, uuid4
from datetime import datetime
from typing import Optional, Dict, List
from .base import BaseModel

class Task(BaseModel):
    """Task model representing a work item"""
    
    def __init__(
        self,
        title: str,
        description: str,
        deadline: datetime,
        assigned_to: UUID,
        follow_up_count: int = 0,
        status: str = "pending",
        id: Optional[UUID] = None,
        created_at: Optional[datetime] = None
    ):
        self.id = id or uuid4()
        self.title = title
        self.description = description
        self.created_at = created_at or datetime.now()
        self.deadline = deadline
        self.assigned_to = assigned_to
        self.follow_up_count = follow_up_count
        self.status = status

    @classmethod
    def create(cls, data: Dict) -> 'Task':
        """Create a new task"""
        return cls(**data)

    _storage: Dict[UUID, 'Task'] = {}

    @classmethod
    def get(cls, id: UUID) -> Optional['Task']:
        """Get a task by ID"""
        return cls._storage.get(id)

    @classmethod
    def get_all(cls) -> List['Task']:
        """Get all tasks"""
        return list(cls._storage.values())

    @classmethod
    def update(cls, id: UUID, updates: Dict) -> Optional['Task']:
        """Update a task"""
        task = cls._storage.get(id)
        if not task:
            return None
            
        for key, value in updates.items():
            setattr(task, key, value)
        return task

    @classmethod
    def delete(cls, id: UUID) -> bool:
        """Delete a task"""
        if id in cls._storage:
            del cls._storage[id]
            return True
        return False

    def increment_follow_up(self) -> None:
        """Increment the follow-up counter"""
        self.follow_up_count += 1

    def update_status(self, new_status: str) -> None:
        """Update task status"""
        valid_statuses = ["pending", "in_progress", "blocked", "done"]
        if new_status not in valid_statuses:
            raise ValueError(f"Invalid status. Must be one of: {valid_statuses}")
        self.status = new_status
