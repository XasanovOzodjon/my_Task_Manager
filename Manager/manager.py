import json
import os
from getpass import getpass
from models import User, Task
from Utils import cheak_name, cheak_password, cheak_username, cheak_admin, make_pas, cheak_title

from datetime import datetime




def clr():
    os.system("cls" if os.name == "nt" else "clear")


class User_manager:
    def __init__(self):
        self.current_user = None
        self.users = self.load_user()
    
    def Register(self):
        clr()
        name = input("Enter your name: ").title()
        if not cheak_name(name):
            return
        
        username = input("Enter your username: ").lower()
        result = cheak_admin(username=username)
        username = result[0]
        if not cheak_username(username, self.users):
            return
        
        password = getpass("Enter your password: ")
        confirm_password = getpass("Confirm your password: ")
        if not cheak_password(password, confirm_password):
            return
        
        new_user = User(name, username, make_pas(password))
        new_user.admin = result[1]

        # Foydalanuvchi uchun task fayl yaratish
        os.makedirs("DataBase", exist_ok=True)
        open(f"DataBase/{new_user.username}_tasks.json", "a").close()

        os.system("clear")
        print(f"Welcome {new_user.name}")
        self.users.append(new_user)
        self.save_user()
        
    def Login(self):
        os.system("clear")
        username = input("Enter your username: ").lower()
        password = getpass("Enter your password: ")
        
        for user in self.users:
            if user.username == username and user.password == make_pas(password):
                self.current_user = user
                os.system("clear")
                print(f"Welcome {user.name}!")
                return True
        os.system("clear")
        print("Invalid username or password.")
        return False
    
    def load_user(self):
        if not os.path.exists("Data/users.json"):
            return []
        with open("Data/users.json", "r") as file:
            try:
                data = json.load(file)
                list_users = []
            except:
                return []
            else:
                for user_data in data:
                    user = User.from_dict(user_data)
                    list_users.append(user)
                return list_users
    
    def save_user(self):
        os.makedirs("Data", exist_ok=True)
        with open("Data/users.json", "w") as file:
            data = [user.to_dict() for user in self.users]
            json.dump(data, file, indent=4)
    
    def get_username(self):
        return self.current_user.username
    def get_id(self):
        return self.current_user.id


class Task_manager(User_manager):
    def __init__(self):
        super().__init__()
        self.tasks = []

    def create_task(self):
        title = input("Task Title: ")
        if not cheak_title(title, self.tasks):
            return
        description = input("Task Description: ")

        while True:
            deadline = input("Task Deadline: ")
            
            try:
                sana = datetime.strptime(deadline, "%d-%m-%Y")
                hozirgi_vaqt = datetime.now()
                
                if sana <= hozirgi_vaqt:
                    os.system("clear")
                    print("Xatolik: Sana hozirgi vaqtdan katta bo‘lishi kerak!")
                else:
                    break
                    
            except ValueError:
                os.system("clear")
                print("Xatolik:(To‘g‘ri format: dd-mm-yyyy)")

        new_task = Task(title, description, deadline, self.get_id())
        self.tasks.append(new_task)
        self.save_tasks()

    def load_tasks(self):
        username = self.get_username()
        path = f"DataBase/{username}_tasks.json"
        if not os.path.exists(path):
            return []

        with open(path, "r") as file:
            try:
                data = json.load(file)
                list_tasks = []
            except:
                return []
            else:
                for task_data in data:
                    task = Task.Task_from_dict(task_data)
                    list_tasks.append(task)
                self.tasks = list_tasks
                return list_tasks

    def save_tasks(self):
        path = f"DataBase/{self.current_user.username}_tasks.json"
        with open(path, "w") as file:
            data = [task.Task_to_dict() for task in self.tasks]
            json.dump(data, file, indent=4)
