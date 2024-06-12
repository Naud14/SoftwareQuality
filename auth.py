import random
from datetime import datetime

# Define roles
roles = ["super_admin", "system_admin", "consultant"]


# Add a user function
def add_user(conn, username, password, role, first_name, last_name):
    try:
        c = conn.cursor()
        password_hash = hash_password(password)
        registration_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        c.execute('''
            INSERT INTO users (username, password_hash, role, first_name, last_name, registration_date)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (username, password_hash, role, first_name, last_name, registration_date))
        conn.commit()
    except Exception as e:
        print(e)

# Verify user login
def verify_login(conn, username, password):
    try:
        c = conn.cursor()
        c.execute('SELECT password_hash, role FROM users WHERE username=?', (username,))
        user = c.fetchone()
        if user and check_password(user[0], password):
            return user[1]  # Return role
        else:
            return None
    except Error as e:
        print(e)
    return None

def create_unique_id():
    # get current year and convert to 2 digit string
    current_year = str(datetime.now().year)[-2:]

    # generate seven random digits
    random_digits = [random.randint(0, 9) for _ in range(7)]

    # combine year and seven random digits
    first_nine = [int(digit) for digit in current_year] + random_digits

    # calculate checksum 
    checksum = sum(first_nine) % 10

    return ''.join(map(str, first_nine)) + str(checksum)
