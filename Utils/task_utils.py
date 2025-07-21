import os

def clr(aa):
    os.system("cls" if os.name == "nt" else "clear")

def print_task_menu():
    print("___________ Task Menu ___________")
    print("1. Show Tasks")
    print("2. Create Tasks")
    print("3. Edit Task")
    print("4. Logout")

def print_task_edit_menu():
    print("___________ Task Edit Menu ___________")
    print("1. Edit title")
    print("2. Edit Discription")
    print("3. Edit Deadline")
    print("4. Delete Task")
    print("5. go Back")
    