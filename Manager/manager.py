import json
import os
from getpass import getpass
from models import User, Task
from Utils import cheak_name, cheak_password, cheak_username, cheak_admin, make_pas, cheak_title, search_user

from datetime import datetime




def clr(aa = "clear"):
    os.system("cls" if os.name == "nt" else aa)


class User_manager:
    def __init__(self):
        self.current_user = None
        self.users = self.load_user()
    
    def Register(self):
        clr()
        name = input("Enter your name: ").title()
        while not cheak_name(name):
            name = input("Enter your name again: ").title()
            
        clr()
        username = input("Enter your username: ").lower()
        result = cheak_admin(username=username)
        username = result[0]
        while not cheak_username(username, self.users):
            username = input("Enter your username again: ").lower()
        
        clr()
        password = getpass("Enter your password: ")
        confirm_password = getpass("Confirm your password: ")
        while not cheak_password(password, confirm_password):
            password = getpass("Enter your password: ")
            confirm_password = getpass("Confirm your password: ")
        
        new_user = User(name, username, make_pas(password))
        new_user.admin = result[1]
        
        open(f"DataBase/{new_user.username}_tasks.json", "a").close()

        clr()
        print(f"Welcome {new_user.name}")
        self.users.append(new_user)
        self.users = sorted(self.users, key=lambda user: user.username)
        self.save_user()
        
    def Login(self):
        clr()
        username = input("Enter your username: ").lower()
        password = getpass("Enter your password: ")
        
        
        user = search_user(username, self.users)
        
        if user != -1:
            if user.password == make_pas(password):
                self.current_user = user
                os.system("clear")
                print(f"Welcome {user.name}!")
                return True
            else:
                os.system("clear")
                print("Invalid password.")
                return False
        else:
            os.system("clear")
            print("Invalid username or password.")
            return False

        # for user in self.users:
        #     if user.username == username and user.password == make_pas(password):
        #         self.current_user = user
        #         os.system("clear")
        #         print(f"Welcome {user.name}!")
        #         return True
        # os.system("clear")
        # print("Invalid username or password.")
        # return False
    
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
                list_users = sorted(list_users, key=lambda user: user.username)
                return list_users
    
    def save_user(self):
        with open("Data/users.json", "w") as file:
            data = [user.to_dict() for user in self.users]
            json.dump(data, file, indent=4)
    
    def get_username(self):
        return self.current_user.username
    
    def get_id(self):
        return self.current_user.id

    def Logout(self):
        self.current_user = None




class Task_manager(User_manager):
    def __init__(self):
        super().__init__()
        self.tasks = []

    def show_task(self):
        clr()
        self.retry()
        print("___________ My Tasks ___________")
        if len(self.tasks) != 0:
            for i, task in enumerate(self.tasks):
                print(f"{i+1}. {task.title}")
        else:
            print("Sizda Tasklar mavjud emas!\n")
        print(f"{len(self.tasks)+1}. Exit")

        try:
            choise = int(input("> "))
        except ValueError:
            clr()
            print("Xatolik: Raqam kiriting")
            return

        if choise == len(self.tasks) + 1:
            clr()
            return

        if 1 <= choise <= len(self.tasks):
            clr()
            task = self.tasks[choise - 1]
            print(f"___________ {task.title} ___________")
            print(f"Description: {task.description}")
            print(f"Created_at: {task.created_at}")
            print(f"Deadline: {task.deadline}")
            print(f"Satatus: {"Bajarilgan" if task.status else "Bajarilmagan"}")
            
            print(f"\n1 - Bajarilgan qilish!")
            ch = input("[Enter] — ortga qaytish\n>>")
            if ch == "1":
                self.tasks[choise - 1].status = True
                self.save_tasks()
                self.retry()
            clr()
        else:
            print("Siz noto‘g‘ri tanlov kiritdingiz!")
        
        
    def create_task(self):
        self.retry()
        clr()
        title = input("Task Title: ")
        if not cheak_title(title, self.tasks):
            return
        description = input("Task Description: ")

        while True:
            deadline = input("Task Deadline (dd-mm-yyyy): ")
            try:
                sana = datetime.strptime(deadline, "%d-%m-%Y")
                hozirgi_vaqt = datetime.now()
                if sana <= hozirgi_vaqt:
                    clr()
                    print("Xatolik: Sana hozirgi vaqtdan katta bo‘lishi kerak!")
                else:
                    break
            except ValueError:
                clr()
                print("Xatolik:(To‘g‘ri format: dd-mm-yyyy)")

        new_task = Task(title, description, deadline, self.get_id())
        self.tasks.append(new_task)
        self.save_tasks()
        self.retry()

    def delete_task(self):
        clr()
        self.retry()
        print("___________ My Tasks ___________")
        if len(self.tasks) != 0:
            for i, task in enumerate(self.tasks):
                print(f"{i+1}. {task.title}")
        else:
            print("Sizda Tasklar mavjud emas!\n")
        print(f"{len(self.tasks)+1}. Exit")

        try:
            choise = int(input("> "))
        except ValueError:
            clr()
            print("Xatolik: Raqam kiriting")
            return

        if choise == len(self.tasks) + 1:
            clr()
            return

        if 1 <= choise <= len(self.tasks):
            clr()
            dell = self.tasks.pop(choise - 1)
            print(f"{dell.title} Task o'chirildi.")
            self.save_tasks()
            self.retry
        else:
            print("Siz noto‘g‘ri tanlov kiritdingiz!")
    
    def edit_title(self):
        clr()
        self.retry()
        print("___________ My Tasks ___________")
        if len(self.tasks) != 0:
            for i, task in enumerate(self.tasks):
                print(f"{i+1}. {task.title}")
        else:
            print("Sizda Tasklar mavjud emas!\n")
        print(f"{len(self.tasks)+1}. Exit")

        try:
            choise = int(input("> "))
        except ValueError:
            clr()
            print("Xatolik: Raqam kiriting")
            return

        if choise == len(self.tasks) + 1:
            clr()
            return

        if 1 <= choise <= len(self.tasks):
            clr()
            title = input("New Task Title: ")
            self.tasks[choise - 1].title = title
            print(f"Task nomi {title} ga o'zgartirildi")
            self.save_tasks()
            self.retry
        else:
            print("Siz noto‘g‘ri tanlov kiritdingiz!")
    
    def edit_discraption(self):
        clr()
        self.retry()
        print("___________ My Tasks ___________")
        if len(self.tasks) != 0:
            for i, task in enumerate(self.tasks):
                print(f"{i+1}. {task.title}")
        else:
            print("Sizda Tasklar mavjud emas!\n")
        print(f"{len(self.tasks)+1}. Exit")

        try:
            choise = int(input("> "))
        except ValueError:
            clr()
            print("Xatolik: Raqam kiriting")
            return

        if choise == len(self.tasks) + 1:
            clr()
            return

        if 1 <= choise <= len(self.tasks):
            clr()
            description = input("New Task Description: ")
            self.tasks[choise - 1].description = description
            print(f"Task descriptioni: {description} ga o'zgartirildi")
            self.save_tasks()
            self.retry
        else:
            print("Siz noto‘g‘ri tanlov kiritdingiz!")
            
    
    def edit_deatline(self):
        clr()
        self.retry()
        print("___________ My Tasks ___________")
        if len(self.tasks) != 0:
            for i, task in enumerate(self.tasks):
                print(f"{i+1}. {task.title}")
        else:
            print("Sizda Tasklar mavjud emas!\n")
        print(f"{len(self.tasks)+1}. Exit")

        try:
            choise = int(input("> "))
        except ValueError:
            clr()
            print("Xatolik: Raqam kiriting")
            return

        if choise == len(self.tasks) + 1:
            clr()
            return

        if 1 <= choise <= len(self.tasks):
            clr()
            while True:
                deadline = input("Task Deadline (dd-mm-yyyy): ")
                try:
                    sana = datetime.strptime(deadline, "%d-%m-%Y")
                    hozirgi_vaqt = datetime.now()
                    if sana <= hozirgi_vaqt:
                        clr()
                        print("Xatolik: Sana hozirgi vaqtdan katta bo‘lishi kerak!")
                    else:
                        break
                except ValueError:
                    clr()
                    print("Xatolik:(To‘g‘ri format: dd-mm-yyyy)")
            self.tasks[choise - 1].deadline = deadline
            print(f"Task deatlinesi: {deadline} ga o'zgartirildi")
            self.save_tasks()
            self.retry
        else:
            print("Siz noto‘g‘ri tanlov kiritdingiz!")
    
    def load_tasks(self):
        username = self.get_username()
        path = f"DataBase/{username}_tasks.json"
        if not os.path.exists(path):
            return []
        with open(path, "r") as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError:
                return []
            else:
                list_tasks = []
                for task_data in data:
                    task = Task.from_dict(task_data)
                    list_tasks.append(task)
                return list_tasks
        path = f"DataBase/{username}_tasks.json"
            
    def retry(self):
        self.tasks = self.load_tasks()

    def save_tasks(self):
        path = f"DataBase/{self.current_user.username}_tasks.json"
        data = [task.to_dict() for task in self.tasks]
        with open(path, "w") as file:
            json.dump(data, file, indent=4)
