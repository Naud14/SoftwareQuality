from logic.validate import validate_password
from database.database import get_connection, send_query
from database.auth import check_password, hash_password, decrypt_data

def update_password(username):
    old_password = input("Enter old password: ")
    
    # check in DB if correct 
    conn = get_connection()
    if(conn is None) : 
        print("Failed to connect to database!")
        return False
    c = conn.cursor()
    c.execute('SELECT username, password_hash FROM users ')
    result = c.fetchall()
    found_users = [row[0] for row in result if row[1] == hash_password(old_password)]

    if(len(found_users) == 0):
        print("Not valid, please try again") 
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
    conn.close()
    print("Password updated successfully!")
    return True

def get_user_overview():
    try:
        conn = get_connection()
        if conn is None:
            print("Failed to connect to database!")
            return False
        
        query = 'SELECT username, role, first_name, last_name, registration_date FROM users'
        users = send_query(conn, query)

        if not users:
            print("No users found!")
            return False
        
        # print user overview
        print("User Overview:")
        for user in users:
            username = decrypt_data(user[0])
            role = decrypt_data(user[1])
            first_name = decrypt_data(user[2])
            last_name = decrypt_data(user[3])
            registration_date = decrypt_data(user[4])

            print(f"Username: {username}")
            print(f"Role: {role}")
            print(f"Name: {first_name} {last_name}")
            print(f"Registration Date: {registration_date}")
            print("-"*50)
        conn.close()
        return True
    except Exception as e:
        print("Failed to fetch user overview")
        print(e)
        return False