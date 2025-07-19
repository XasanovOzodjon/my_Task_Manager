from datetime import datetime

class Task:
    def __init__(self, title , description, deadline, idd):
        self.title = title,
        self.description = description,
        self.created_at = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        self.deadline = deadline
        self.user_id = idd
        
        
    def Task_to_dict(self):
        return {
                "title": self.title,
                "description": self.description,
                "created_at": self.created_at,
                "deadline": self.deadline,
                "user_id": self.user_id
        }
    
    @classmethod
    def Task_from_dict(cls, data: dict):
        temp_user = cls(data["title"], data["description"], data["user_id"])
        temp_user.user_id = data["user_id"]
        return temp_user