from database import get_connection
from auth import verify_login

def main_menu():
    print("Unique Meal Membership Management System")
    print("1. Login")
    print("2. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        login()
    elif choice == "2":
        exit()
    else:
        print("Invalid choice. Please try again.")
        main_menu()


def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    
    conn = get_connection()
    role = verify_login(conn, username, password)
    
    if role == "super_admin":
        super_admin_menu()
    elif role == "consultant":
        consultant_menu()
    elif role == "system_admin":
        system_admin_menu()
    else:
        print("Incorrect login, try again.")
        login()

def super_admin_menu():
    print("Super Admin Menu")
    print("1. Add System Admin")
    print("2. Add Consultant")
    print("3. View Logs")
    print("4. Backup System")
    print("5. Logout")
    choice = input("Enter your choice: ")
    if choice == "1":
        # Add system admin
        pass
    elif choice == "2":
        # Add consultant
        pass
    elif choice == "3":
        # View logs
        pass
    elif choice == "4":
        # Backup system
        pass
    elif choice == "5":
        main_menu()
    else:
        print("Invalid choice. Please try again.")
        super_admin_menu()


def system_admin_menu():
    print("System Admin Menu")
    print("1. Add Member")
    print("2. Edit Member")
    print("3. Delete Member")
    print("4. View Member")
    print("5. Logout")
    choice = input("Enter your choice: ")
    if choice == "1":
        # Add member
        pass
    elif choice == "2":
        # Edit member
        pass
    elif choice == "3":
        # Delete member
        pass
    elif choice == "4":
        # View member
        pass
    elif choice == "5":
        main_menu()
    else:
        print("Invalid choice. Please try again.")
        system_admin_menu()


def consultant_menu():
    print("Consultant Menu")
    print("1. View Member")
    print("2. Logout")
    choice = input("Enter your choice: ")
    if choice == "1":
        # View member
        pass
    elif choice == "2":
        main_menu()
    else:
        print("Invalid choice. Please try again.")
        consultant_menu()
