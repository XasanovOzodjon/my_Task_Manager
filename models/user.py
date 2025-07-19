from uuid import uuid1

class User:
    def __init__(self, name: str, username: str, password: str):
        self.name = name
        self.username = username
        self.password = password
        self.id = str(uuid1())
        self.admin = False

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "username": self.username,
            "password": self.password,
            "admin": self.admin
        }
    
    @classmethod
    def from_dict(cls, data: dict):
        temp_user = cls(data["name"], data["username"], data["password"])
        temp_user.id = data["id"]
        temp_user.admin = data["admin"]
        return temp_user