from Utils import print_main_menu, print_task_menu, print_task_edit_menu
from Manager import Task_manager
import os

def clr(aa = "clear"):
    os.system("cls" if os.name == "nt" else aa)


def login_or_register() -> None:
    clr("clear")
    manager = Task_manager()
    while True:
        print_main_menu()
        choice = input()
        
        if choice == '1':
            if manager.Login():
                Task_menu(manager)
        elif choice == '2':
            manager.Register()
        elif choice == '3':
            return
        else:
            clr("clear")        


def Task_menu(manager: Task_manager) -> None:
    clr()
    manager.load_tasks()
    while True:
        print_task_menu()
        choice = input()
        
        if choice == '1':
            manager.show_task()
        elif choice == '2':
            manager.create_task()
        elif choice == '3':
            Edit_menu(manager)
        elif choice == '4':
            manager.Logout()
            login_or_register()
        else:
            print("Xato Buyruq!")
            clr("clear")
            
def Edit_menu(manager: Task_manager) -> None:
    clr()
    manager.load_tasks()
    while True:
        print_task_edit_menu()
        choice = input()
        
        if choice == '1':
            manager.edit_title()
        elif choice == '2':
            manager.edit_discraption()
        elif choice == '3':
            manager.edit_deatline()
        elif choice == '4':
            manager.delete_task()
        elif choice == '5':
            Task_menu(manager)
            return
        else:
            print("Xato Buyruq!")
            clr("clear")


if __name__ == "__main__":
    login_or_register()
