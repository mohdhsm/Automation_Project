#!/usr/bin/env python3
from uuid import UUID, uuid4
from datetime import datetime
from typing import Optional, Dict, List, Union
from .base import BaseModel

class Task(BaseModel):
    """Task model representing a work item"""
    
    _next_id: int = 1
    
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
        self.task_id = self.__class__._next_id
        self.__class__._next_id += 1
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
        task = cls(**data)
        cls._storage[task.id] = task
        cls._id_map[task.task_id] = task.id
        return task

    _storage: Dict[UUID, 'Task'] = {}
    _id_map: Dict[int, UUID] = {}

    @classmethod
    def get(cls, id: Union[UUID, int]) -> Optional['Task']:
        """Get a task by ID (UUID or sequential ID)"""
        if isinstance(id, int):
            id = cls._id_map.get(id)
            if not id:
                return None
        return cls._storage.get(id)

    @classmethod
    def get_all(cls) -> List['Task']:
        """Get all tasks"""
        return list(cls._storage.values())

    @classmethod
    def update(cls, id: Union[UUID, int], updates: Dict) -> Optional['Task']:
        """Update a task"""
        if isinstance(id, int):
            id = cls._id_map.get(id)
            if not id:
                return None
                
        task = cls._storage.get(id)
        if not task:
            return None
            
        for key, value in updates.items():
            setattr(task, key, value)
        return task

    @classmethod
    def delete(cls, id: Union[UUID, int]) -> bool:
        """Delete a task"""
        if isinstance(id, int):
            id = cls._id_map.get(id)
            if not id:
                return False
                
        if id in cls._storage:
            task = cls._storage[id]
            del cls._storage[id]
            del cls._id_map[task.task_id]
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
