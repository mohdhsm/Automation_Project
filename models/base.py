#!/usr/bin/env python3
from typing import Any, Dict, List, Optional, Type, TypeVar
from uuid import UUID, uuid4
from datetime import datetime

T = TypeVar('T', bound='BaseModel')

class BaseModel:
    """Base model with common CRUD operations"""
    
    @classmethod
    def create(cls: Type[T], data: Dict[str, Any]) -> T:
        """Create a new record"""
        raise NotImplementedError
        
    @classmethod
    def get(cls: Type[T], id: UUID) -> Optional[T]:
        """Get a record by ID"""
        raise NotImplementedError
        
    @classmethod
    def get_all(cls: Type[T]) -> List[T]:
        """Get all records"""
        raise NotImplementedError
        
    @classmethod #In this method, it will take the id of the record and the updates to be made)
    def update(cls: Type[T], id: UUID, updates: Dict[str, Any]) -> Optional[T]:
        """Update a record"""
        raise NotImplementedError
        
    @classmethod #In this method, it will take the id of the record to be deleted)
    def delete(cls: Type[T], id: UUID) -> bool:
        """Delete a record"""
        raise NotImplementedError
        
    def to_dict(self) -> Dict[str, Any]: #Will convert the model to a dictionary, for which purpose? this allows it for API, and can be converted to JSON in the future for API use. 
        """Convert model to dictionary"""
        return {k: v for k, v in self.__dict__.items() if not k.startswith('_')}
