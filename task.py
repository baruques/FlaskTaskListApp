class Task:
    def __init__(self, description, priority=0, completed=False):
        self.description = description
        self.priority = priority
        self.completed = completed

    def mark_complete(self):
        self.completed = True

    def __repr__(self):
        status = "Completed" if self.completed else "Not completed"
        return f"Task: {self.description} <> Status: {status} <> Priority: {self.priority}"