import random
from datetime import datetime
from hashlib import sha256
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.exceptions import InvalidSignature

from database.database import get_connection, send_query

# Define roles
roles = ["super_admin", "system_admin", "consultant"]


# Generate key for program
def generate_key_pair():
    key_size = 2048
    privkey = rsa.generate_private_key(
        public_exponent=65537,
        key_size=key_size,
    )

    publkey = privkey.public_key()
    return privkey, publkey


private_key, public_key = generate_key_pair()


def encrypt_data(data):
    # Encrypt the data
    data_bytes = data.encode('utf-8')

    return public_key.encrypt(
        data_bytes,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )


def decrypt_data(encrypted_text):
    try:
        message_decrypted = private_key.decrypt(
            encrypted_text,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return message_decrypted
    except ValueError:
        print("Failed to decrypt data")


# Add a user function
def hash_password(password):
    print("Password hashed!")
    return sha256(password.encode('utf-8')).hexdigest()


# Send encrypted user in database
def add_user(username, password, role, first_name, last_name):
    try:
        password_hash = hash_password(password)
        registration_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        query = '''
            INSERT INTO users (username, password_hash, role, first_name, last_name, registration_date)
            VALUES (?, ?, ?, ?, ?, ?)
        '''
        encrypted_username = encrypt_data(username)
        encrypted_role = encrypt_data(role)
        encrypted_first_name = encrypt_data(first_name)
        encrypted_last_name = encrypt_data(last_name)
        encrypted_registration_date = encrypt_data(registration_date)

        cursor = get_connection()

        if cursor is not None:
            send_query(cursor, query, (encrypted_username, password_hash, encrypted_role, encrypted_first_name, encrypted_last_name, encrypted_registration_date))
            print("Added user to database!")
    except Exception as e:
        print("Add user failure")
        print(e)


def check_password(hashed_password, password):
    return hashed_password == hash_password(password)


# Verify user login
def verify_login(conn, username, password):
    try:
        c = conn.cursor()
        c.execute('SELECT username, password_hash, role FROM users')
        for row in c.fetchall():
            if decrypt_data(row[0]) == username:
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
