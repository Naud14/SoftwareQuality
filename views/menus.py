from database.database import get_connection
from database.auth import verify_login
from database.backup import create_backup
from logic.userlogic import update_password, get_user_overview
from logic.memberlogic import add_member, update_member_information, search_member, delete_member
from logic.consultantlogic import add_consultant, edit_consultant, delete_consultant, reset_consultant_password
from database.logging import see_logs
from logic.admin import update_admin, delete_admin, reset_admin_password, create_admin



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
        consultant_menu(username)
    elif role == "system_admin":
        system_admin_menu(username)
    else:
        print("Incorrect login, try again.")
        login()


def super_admin_menu():
    print("Super Admin Menu")
    print("1. User role overview")
    print("2. Add consultant")
    print("3. Edit consultant")
    print("4. Delete consultant")
    print("5. Reset consultant password")
    print("6. Add new admin")
    print("7. Update admin's account")
    print("8. Delete admin's account")
    print("9. Reset admin's password")
    print("10. Make and restore backup of system")
    print("11. See logfiles")
    print("12. Add member")
    print("13. Edit member")
    print("14. Delete member")
    print("15. Search member")
    print("16. Logout")
    choice = input("Enter your choice: ")
    if choice == "1":
        # User overview
        get_user_overview()
    elif choice == "2":
        # Add consultant
        add_consultant()
    elif choice == "3":
        # Edit consultant
        edit_consultant()
    elif choice == "4":
        # Delete consultant
        delete_consultant()
    elif choice == "5":
        # Reset consultant password
        reset_consultant_password()
    elif choice == "6":
        # Add new admin
        create_admin()
    elif choice == "7":
        # Update admin's account
        update_admin()
    elif choice == "8":
        # Delete admin's account
        delete_admin()
    elif choice == "9":
        # reset admin's password
        reset_admin_password()
    elif choice == "10":
        create_backup()
        pass
    elif choice == "11":
        # See logfiles
        see_logs()
    elif choice == "12":
        # Add member
        add_member()
    elif choice == "13":
        # Edit member
        update_member_information()
    elif choice == "14":
        # Delete member
        delete_member()
    elif choice == "15":
        # Search member
        search_member()
    elif choice == "16":
        main_menu()
    else:
        print("Invalid choice. Please try again.")
        super_admin_menu()
    super_admin_menu()


def system_admin_menu(username):
    print("System Admin Menu")
    print("1. Update password")
    print("2. User role overview")
    print("3. Add consultant")
    print("4. Edit consultant")
    print("5. Delete consultant")
    print("6. Reset consultant password")
    print("7. Make and restore backup of system")
    print("8. See logfiles")
    print("9. Add member")
    print("10. Edit member")
    print("11. Delete member")
    print("12. Search member")
    print("13. Logout")
    choice = input("Enter your choice: ")
    if choice == "1":
        # Update password
        update_password(username)
    elif choice == "2":
        # User role overview
        get_user_overview()
    elif choice == "3":
        # Add consultant
        add_consultant()
    elif choice == "4":
        # Edit consultant
        edit_consultant()
    elif choice == "5":
        # Delete consultant
        delete_consultant()
    elif choice == "6":
        # reset consultant password
        reset_consultant_password()
    elif choice == "7":
        # TODO make and restore backup system
        pass
    elif choice == "8":
        # See logfiles
        see_logs()
    elif choice == "9":
        # Add member
        add_member()
    elif choice == "10":
        # Update member information
        update_member_information()
    elif choice == "11":
        # Delete member
        delete_member()
    elif choice == "12":
        # Search member
        search_member()
    elif choice == "13":
        main_menu()
    else:
        print("Invalid choice. Please try again.")
        system_admin_menu()


def consultant_menu(username):
    print("Consultant Menu")
    print("1. Update password")
    print("2. Add new member")
    print("3. Modify/update member information")
    print("4. Search member")
    print("5. Logout")
    choice = input("Enter your choice: ")
    if choice == "1":
        # Update password
        update_password(username)
    elif choice == "2":
        # Add new member
        add_member()
    elif choice == "3":
        # Modify/update member information
        update_member_information()
    elif choice == "4":
        # Search member
        search_member()
    elif choice == "5":
        # Logout
        main_menu()
    else:
        print("Invalid choice. Please try again.")
        consultant_menu(username)
