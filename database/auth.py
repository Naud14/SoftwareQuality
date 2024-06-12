import random
from datetime import datetime
from hashlib import sha256
from cryptography.fernet import Fernet

from database.database import send_query

# Define roles
roles = ["super_admin", "system_admin", "consultant"]


# Generate key for program
key = Fernet.generate_key()
cipher_suite = Fernet(key)


def encrypt_data(data):
    # Encrypt the data
    encrypted_text = cipher_suite.encrypt(data.encode('utf-8'))
    return encrypted_text


def decrypt_data(encrypted_text):
    # Decrypt the user information
    decrypted_text = cipher_suite.decrypt(encrypted_text).decode('utf-8')
    # Split the decrypted text back into its components
    return decrypted_text


# Add a user function
def hash_password(password):
    return sha256(password.encode('utf-8')).hexdigest()


# Send encrypted user in database
def add_user(username, password, role, first_name, last_name):
    try:
        password_hash = hash_password(password)
        registration_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        send_query(f'''
            INSERT INTO users (username, password_hash, role, first_name, last_name, registration_date)
            VALUES ({encrypt_data(username)}, {password_hash}, {encrypt_data(role)}, {encrypt_data(first_name)}, 
            {encrypt_data(last_name)}, {encrypt_data(registration_date)})
        ''')

    except Exception as e:
        print(e)


def check_password(hashed_password, password):
    return hashed_password == hash_password(password)


# Verify user login
def verify_login(conn, username, password):
    try:
        c = conn.cursor()
        c.execute('SELECT username, password_hash, role FROM users')
        for row in c.fetchall():
            if decrypt_data(decrypt_data(row[0])) == username:
                if row[1] == hash_password(password):
                    return decrypt_data(row[2])
                    # Could also return all data from row by using return row.
                    # You'd probably need to decrypt it all first though.
    except Exception as e:
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
