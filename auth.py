import random
from datetime import datetime
import re
# Define roles
roles = ["super_admin", "system_admin", "consultant"]
cities = ["Rotterdam", "Oldenzaal", "Budapest", "Kathmandu", "Moskou", "Lelystad", "Stockholm", "Ruinerwold", "Liverpool", "Penemunde"]


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


# Add hardcoded super admin
add_user(conn, "super_admin", "Admin_123?", "super_admin", "Super", "Admin")


# Example login verification
role = verify_login(conn, "super_admin", "Admin_123?")
if role:
    print(f"Login successful. Role: {role}")
else:
    print("Invalid username or password.")

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

def check_first_name(name):
    return name.isalpha()

def validate_(age):
    return age.isdigit() and 0 < int(age) <= 125

def validate_gender(gender):
    return gender.lower() in ['male', 'female']

def validate_weight(weight):
    return weight.replace('.', '', 1).isdigit() and 0 < int(weight) <= 700

def validate_address(street, house_number, zip_code, city):
    validate_zipcode = re.match(r'^\d{4}[A-Z]{2}$', zip_code)
    validate_city = city.capitalize() in cities
    return validate_zipcode and validate_city

def validate_email(email):
    return re.match(r'^\S+@\S+\.\S+$', email) is not None

def validate_phone(phone):
    return re.match(r'^\d{8}$', phone) is not None
