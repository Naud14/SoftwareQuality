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

        if first_name.isalpha() and last_name.isalpha(): break
        else: print("Invalid name(s), please try again!")
        
    # add new consultant to database
    try: 
        password_hash = hash_password(password)
        registration_date = datetime.now()

        query = ''' INSERT INTO users (username, password_hash, role, first_name, last_name, registration_date) VALUES (?, ?, ?, ?, ?, ?)'''
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
    print("Edit consultant details!")
    
    # Validate username
    while True:
        username = input("Enter the username of the consultant to edit: ")
        if not username:
            print("Username cannot be empty. Please try again.")
            return

        encrypted_username = encrypt_data(username)
        
        # Check if username exists and role is consultant
        try:
            conn = get_connection()
            if conn is not None:
                query = "SELECT role FROM users WHERE username = ?"
                cursor = conn.cursor()
                cursor.execute(query, (encrypted_username,))
                result = cursor.fetchone()
                
                if result:
                    role = result[0]
                    if role == encrypt_data("consultant") or "consultant":
                        print("Consultant found!")
                        break
                    else:
                        print("This user is not a consultant. Access denied.")
                        return  
                else:
                    print("Username not found. Please try again.")
                
                conn.close()
        except Exception as e:
            print("Failed to retrieve consultant details.")
            print("Error:", e)
            return  
    
    # Display options
    print("What would you like to edit?")
    print("1. First Name")
    print("2. Last Name")
    print("3. Password")
    print("4. Role")
    choice = input("Choose an option (1-4): ")
    
    update_field = None
    update_value = None
    
    if choice == '1':
        first_name = input("Enter new first name: ")
        if first_name.isalpha():
            update_field = "first_name"
            update_value = encrypt_data(first_name)
        else:
            print("Invalid first name, please try again.")
            return
    
    elif choice == '2':
        last_name = input("Enter new last name: ")
        if last_name.isalpha():
            update_field = "last_name"
            update_value = encrypt_data(last_name)
        else:
            print("Invalid last name, please try again.")
            return
    
    elif choice == '3':
        password = input("Enter new password: ")
        if validate_password(password):
            update_field = "password_hash"
            update_value = hash_password(password)
        else:
            print("Invalid password. Must be at least 8 characters.")
            return
    
    elif choice == '4':
        role = input("Enter new role (e.g., consultant): ")
        if role.isalpha():
            update_field = "role"
            update_value = encrypt_data(role)
        else:
            print("Invalid role, please try again.")
            return
    
    else:
        print("Invalid option, please select from 1-4.")
        return 
    
    # Update consultant in the database 
    if update_field and update_value:
        try:
            conn = get_connection()
            if conn is not None:
                query = ''' UPDATE users SET {update_field} = ? WHERE username = ? '''
                params = (update_value, encrypted_username)
                
                send_query(conn, query, params)
                print("Consultant details updated successfully!")
                conn.close()
        except Exception as e:
            print("Failed to update consultant details.")
            print("Error:", e)
    else:
        print("No updates were made.")
    

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