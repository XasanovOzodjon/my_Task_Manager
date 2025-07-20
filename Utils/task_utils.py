import os

def clr(aa):
    os.system("cls" if os.name == "nt" else "clear")

def print_task_menu():
    print("___________ Task Menu ___________")
    print("1. Show Tasks")
    print("2. Create Tasks")
    print("3. Logout")
    