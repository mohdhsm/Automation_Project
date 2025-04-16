#!/usr/bin/env python3
from uuid import UUID
from datetime import datetime
from typing import Optional, Dict, List
from .base import BaseModel

class Employee(BaseModel):
    """Employee model representing a team member"""
    
    def __init__(
        self,
        name: str,
        email: str,
        id: Optional[UUID] = None,
        created_at: Optional[datetime] = None
    ):
        self.id = id or uuid4()
        self.name = name
        self.email = email
        self.created_at = created_at or datetime.now()

    @classmethod
    def create(cls, data: Dict) -> 'Employee':
        """Create a new employee"""
        return cls(**data)

    @classmethod
    def get(cls, id: UUID) -> Optional['Employee']:
        """Get an employee by ID"""
        # Implementation depends on database backend
        raise NotImplementedError

    @classmethod
    def get_all(cls) -> List['Employee']:
        """Get all employees"""
        # Implementation depends on database backend
        raise NotImplementedError

    @classmethod
    def update(cls, id: UUID, updates: Dict) -> Optional['Employee']:
        """Update an employee"""
        # Implementation depends on database backend
        raise NotImplementedError

    @classmethod
    def delete(cls, id: UUID) -> bool:
        """Delete an employee"""
        # Implementation depends on database backend
        raise NotImplementedError

    def validate_email(self) -> bool:
        """Validate the email format"""
        return '@' in self.email and '.' in self.email.split('@')[-1]
