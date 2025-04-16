#!/usr/bin/env python3
from uuid import UUID
from datetime import datetime
from typing import Optional, Dict, List
from .base import BaseModel

class SyncLog(BaseModel):
    """SyncLog model representing API sync history"""
    
    def __init__(
        self,
        source: str,
        last_checked: datetime,
        id: Optional[UUID] = None,
    ):
        self.id = id or uuid4()
        self.source = source
        self.last_checked = last_checked

    @classmethod
    def create(cls, data: Dict) -> 'SyncLog':
        """Create a new sync log entry"""
        return cls(**data)

    @classmethod
    def get(cls, id: UUID) -> Optional['SyncLog']:
        """Get a sync log by ID"""
        # Implementation depends on database backend
        raise NotImplementedError

    @classmethod
    def get_all(cls) -> List['SyncLog']:
        """Get all sync logs"""
        # Implementation depends on database backend
        raise NotImplementedError

    @classmethod
    def update(cls, id: UUID, updates: Dict) -> Optional['SyncLog']:
        """Update a sync log"""
        # Implementation depends on database backend
        raise NotImplementedError

    @classmethod
    def delete(cls, id: UUID) -> bool:
        """Delete a sync log"""
        # Implementation depends on database backend
        raise NotImplementedError

    def is_stale(self, threshold_minutes: int = 15) -> bool:
        """Check if sync is stale based on threshold"""
        return (datetime.now() - self.last_checked).total_seconds() > threshold_minutes * 60
