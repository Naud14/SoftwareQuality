from logic.validate import validate_username, validate_password
from database.auth import hash_password, encrypt_data
from database.database import get_connection, send_query
from datetime import datetime

def create_admin():
    print("Enter admin details!")
    while True:
        username = input("Username: ")
        if(validate_username(username)) : break
        else : print("Invalid username, please try again!")
    while True:
        password = input("Password: ")
        if(validate_password(password)) : break
        else : print("Invalid password, please try again!")
    role = "system_admin"
    while(True):
        first_name = input("Enter your first name: ")
        last_name = input("Enter your last name: ")

        if first_name.isalpha and last_name.isalpha: break
        else: print("Invalid name(s), please try again!")
        
    # add new system admin to database
    try: 
        password_hash = hash_password(password)
        registration_date = datetime.now()

        query = ''' INSERT INTO users (username, password_hash, role, first_name, last_name, registration_date, VALUES (?, ?, ?, ?, ?, ?))'''
        encrypted_username = encrypt_data(username)
        encrypted_role = encrypt_data(role)
        encrypted_first_name = encrypt_data(first_name)
        encrypted_last_name = encrypt_data(last_name)
        encrypted_registration_date = encrypt_data(registration_date)

        conn = get_connection()
        if(conn is not None):
            send_query(conn, query, (encrypted_username, password_hash, encrypted_role, encrypted_first_name, encrypted_last_name, encrypted_registration_date))
            print("System admin added to the database!")
            conn.close()
    except Exception as e:
        print("Failed to add system admin to the database")
        print(e)

def update_admin():
    print("TODO")


def delete_admin():
    print("Delete system admin")
    username = input("Enter username of system admin to delete: ")
    try: 
        conn = get_connection()
        if(conn is not None):
            # First check if user exists and is a system admin
            query = "SELECT role FROM users WHERE username = ?"
            result = send_query(conn, query, (username,))
            if result and result[0][0] == "system_admin":
                delete_query = "DELETE FROM users WHERE username = ?"
                send_query(conn, delete_query, (username,))
                print("System admin deleted successfully")
            else:
                print("User is not a system admin or does not exist!")
            conn.close()
        else:
            print("Failed to connect to database")
    except Exception as e:
        print("Failed to delete system admin")
        print(e)


def reset_admin_password():
    print("TODO")