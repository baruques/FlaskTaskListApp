from datetime import datetime
import uuid
class Task:
    def __init__(self, description, priority=0, completed=False):
        self.id = uuid.uuid4()  
        self.description = description
        self.priority = priority
        self.created_at = datetime.now()
        self.completed = completed

    def mark_complete(self):
        self.completed = True
        self.completed_at = datetime.now() - self.created_at

    def __repr__(self):
        status = "Completed" if self.completed else "Not completed"
        return f"Task: {self.description} <> Status: {status} <> Priority: {self.priority}"
    
    