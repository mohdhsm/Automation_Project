#!/usr/bin/env python3
from uuid import UUID
from datetime import datetime
from typing import Optional, Dict, List, Union
from models.task import Task
import logging

class TaskController:
    """Controller for managing task operations"""
    
    def __init__(self):
        self.logger = logging.getLogger(__name__) # instantiate the logger

    def create_task(self, task: Task) -> Task: # it will take in type Task, and return a task, after it performs 
        """Create a new task with validation"""
        try:
            # Validate required fields
            if not all([task.title, task.description, task.deadline, task.assigned_to]):
                raise ValueError("All task fields are required")
                
            # Validate deadline is in future
            if task.deadline < datetime.now():
                raise ValueError("Deadline must be in the future")
            # Store task in memory
            Task._storage[task.id] = task
            self.logger.info(f"Created task {task.id}")
            return task
            
    
        except Exception as e:
            self.logger.error(f"Error creating task: {e}")
            raise

    def get_task(self, task_id: Union[UUID, int]) -> Optional[Task]:
        """Retrieve a single task by ID (UUID or sequential ID)"""
        try:
            task = Task.get(task_id)
            if not task:
                raise ValueError(f"Task {task_id} not found")
            self.logger.info(f"Retrieved task {task_id} (UUID: {task.id})")
            return task
        except Exception as e:
            self.logger.error(f"Error getting task {task_id}: {e}")
            raise

    def get_all_tasks(self) -> List[Task]:
        """Retrieve all tasks"""
        try:
            # Creating a list of tasks manually for testing purposes
            tasks = [Task("This is the first task", "This is the first task description", datetime(2023, 10, 1), "mohammed"),
                     Task("This is the second task", "This is the second task description", datetime(2023, 10, 2), "Jane whatever")]
            # Render the task list using the view
            # Store tasks in memory
            
            self.logger.info(f"Retrieved {len(tasks)} tasks")
            return tasks
        except Exception as e:
            self.logger.error(f"Error getting all tasks: {e}")
            raise

    def update_task(self, task_id: Union[UUID, int], updates: Dict) -> Optional[Task]:
        """Update an existing task"""
        try:
            # Validate updates
            if not updates:
                raise ValueError("No updates provided")
                
            updated_task = Task.update(task_id, updates)
            if not updated_task:
                raise ValueError(f"Task {task_id} not found")
            self.logger.info(f"Updated task {task_id} (UUID: {updated_task.id}) with {updates}")
            return updated_task
        except Exception as e:
            self.logger.error(f"Error updating task {task_id}: {e}")
            raise

    def delete_task(self, task_id: Union[UUID, int]) -> bool:
        """Delete a task"""
        try:
            success = Task.delete(task_id)
            if not success:
                raise ValueError(f"Task {task_id} not found")
            self.logger.info(f"Deleted task {task_id}")
            return success
        except Exception as e:
            self.logger.error(f"Error deleting task {task_id}: {e}")
            raise
