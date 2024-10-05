from logic.validate import validate_username, validate_password
from database.auth import hash_password, encrypt_data
from database.database import get_connection, send_query
from datetime import datetime

def add_consultant():
    print("Enter consultant details!")
    while True:
        username = input("Username: ")
        if(validate_username(username)) : break
        else : print("Invalid username, please try again!")
    while True:
        password = input("Password: ")
        if(validate_password(password)) : break
        else : print("Invalid password, please try again!")
    role = "consultant"
    while(True):
        first_name = input("Enter your first name: ")
        last_name = input("Enter your last name: ")

        if first_name.isalpha and last_name.isalpha: break
        else: print("Invalid name(s), please try again!")
        
    # add new consultant to database
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
            print("Consultant added to the database!")
            conn.close()
    except Exception as e:
        print("Failed to add consultant to the database")
        print(e)

def edit_consultant():
    print("TODO")

def delete_consultant():
    print("Delete consultant")
    username = input("Enter username of consultant to delete: ")
    try: 
        conn = get_connection()
        if(conn is not None):
            query = "SELECT role FROM users WHERE username = ?"
            result = send_query(conn, query, (username,))
            if result and result[0][0] == "consultant":
                query = "DELETE FROM users WHERE username = ?"
                send_query(conn, query, (username,))
                print("Consultant deleted successfully")
            else: 
                print("User is not a consultant or does not exist")
            conn.close()
        else:
            print("Failed to connect to database")
    except Exception as e:
        print("Failed to delete consultant")
        print(e)

def reset_consultant_password():
    print("Reset consultant password")
    username = input("Enter the username of the consultant whose password you want to reset: ")

    try:
        conn = get_connection()
        if conn is not None:

            query = "SELECT * FROM users WHERE username = ? AND role = ?"
            result = send_query(conn, query, (username, "consultant"))
            if result:
                while True:
                    new_password = input("Enter new password: ")
                    confirm_password = input("Confirm new password: ")
                    
                    if new_password != confirm_password:
                        print("No match! Try again.")
                    else:
                        if validate_password(new_password):
                            hashed_password = hash_password(new_password)
                            
                            # Update password in DB
                            update_query = "UPDATE users SET password_hash = ? WHERE username = ? AND role = ?"
                            send_query(conn, update_query, (hashed_password, username, "consultant"))
                            print("Password updated successfully.")
                        else:
                            print("Invalid password!")
            else:
                print("No system admin found")
            conn.close()
        else:
            print("Failed to connect to the database.")
    except Exception as e:
        print("Failed to reset consultant password.")
        print(e)