from datetime import datetime

class Task:
    def __init__(self, title, description, deadline, user_id, created_at=None,status = False):
        self.title = title
        self.description = description
        self.created_at = created_at or datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        self.deadline = deadline
        self.user_id = user_id
        self.status = status
        
    def to_dict(self):
        return {
            "title": self.title,
            "description": self.description,
            "deadline": self.deadline,
            "user_id": self.user_id,
            "created_at": self.created_at,
            "status": self.status
        }
    
    @staticmethod
    def from_dict(data):
        return Task(
            title=data["title"],
            description=data["description"],
            deadline=data["deadline"],
            user_id=data["user_id"],
            created_at=data["created_at"],
            status=data["status"]
        )
