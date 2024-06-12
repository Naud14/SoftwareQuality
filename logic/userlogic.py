from validate import validate_password
from database.database import get_connection
from database.auth import check_password, hash_password

def update_password(username):
    old_password = input("Enter old password")
    
    # check in DB if correct 
    conn = get_connection()
    if(conn is None) : 
        print("Failed to connect to database!")
        return False
    c = conn.cursor()
    c.execute('SELECT password_hash FROM users WHERE username = ?', username)
    result = c.fetchone()
    
    if(result is None):
        print("Username not found") 
        return False
    
    old_password_hash = result[0]
    if not check_password(old_password_hash, old_password):
        print("Incorrect password. Try again!")
        return False

    # ask, validate and hash new password
    while(True):
        new_password = input("Enter new password")
        if not(validate_password(new_password)):
            print("New password does not meet criteria")
        else: break
    
    new_password_hash = hash_password(new_password)
    c.execute('UPDATE users SET password_hash = ? WHERE username = ?', (new_password_hash, username))
    conn.commit()

    print("Password updated successfully!")
    return True

def get_user_overview():
    print("TODO")