
from hashlib import sha256
import os

def clr(aa = "clear") -> None:
    os.system("cls" if os.name == "nt" else aa)

def print_main_menu() -> None:
    print("___________ Main Menu ___________")
    print("1. Login")
    print("2. Register")
    print("3. Exit")
    
    
def cheak_name(name: str) -> bool:
    if not name.isalpha():
        clr("clear")
        print("Ismingizda faqat harflar bo'lishi kerak.\n")
        return False
    if len(name) > 20:
        clr("clear")
        print("Ismingiz 20 ta xarfdan uzun bo'lmasligi kerak.\n")
        return False
    if len(name) < 3:
        clr("clear")
        print("Ismingiz 3 ta xarfdan uzun bo'lishi kerak.\n")
        return False
    return True
    
def cheak_username(username: str, users: list) -> bool:
    if username in [user.username for user in users]:
        clr("clear")
        print("Bu foydalanuvchi nomi allaqachon mavjud.\n")
        return False
    if username == "":
        clr("clear")
        print("Foydalanuvchi nomi bo'sh bo'lmasligi kerak.\n")
        return False
    if not username.isalnum():
        clr("clear")
        print("Foydalanuvchi nomi faqat harflar va raqamlardan iborat bo'lishi kerak.\n")
        return False
    if len(username) > 15:
        clr("clear")
        print("Foydalanuvchi nomi 15 ta belgidan uzun bo'lmasligi kerak.\n")
        return False
    if len(username) < 4:
        clr("clear")
        print("Foydalanuvchi nomi 4 ta belgidan uzun bo'lishi kerak.\n")
        return False
    return True

def cheak_password(password, confom) -> bool:
    if password != confom:
        clr("clear")
        print("Password va confirm password bir xil emas\n")
        return False
    if len(password) < 8:
        clr("clear")
        print("Parol kamida 8 ta belgidan iborat bulsin\n")
        return False
    if len(password) > 32:
        clr("clear")
        print("Parolingiz juda uzun\n")
        return False
        
    return True

def cheak_admin(username:str) -> list:
    if username.startswith("admin::08="):
        username.replace("admin::08=", "")
        return [username.replace("admin::08=", ""), True]

    return [username, False]

def search_user(username: str, users: list):
    min_s = 0
    max_s = len(users) - 1

    while min_s <= max_s:
        curent_s = (min_s + max_s) // 2
        current_username = users[curent_s].username

        if username == current_username:
            print("Foydalanuvchi topildi")
            return users[curent_s]
        elif username < current_username:
            max_s = curent_s - 1
        else:
            min_s = curent_s + 1

    print("Topilmadi")
    return -1

    
    
    

def make_pas(password: str) -> str:
    return sha256(password.encode()).hexdigest()


def cheak_title(title: str, tasks: list) -> bool:
    if title in [user.title for user in tasks]:
        clr("clear")
        print("Bu foydalanuvchi nomi allaqachon mavjud.\n")
        return False
    if title == "":
        clr("clear")
        print("Task Title bo'sh bo'lmasligi kerak.\n")
        return False
    if len(title) > 25:
        clr("clear")
        print("Title 25 ta belgidan uzun bo'lmasligi kerak.\n")
        return False
    if len(title) < 2:
        clr("clear")
        print("Title 2 ta belgidan uzun bo'lishi kerak.\n")
        return False
    return True