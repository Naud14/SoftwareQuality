from logic.validate import validate_weight, validate_phone, validate_address, validate_email, validate_gender, validate_age
from logic.validate import cities
from database.database import get_connection, send_query
from database.auth import create_unique_id
from datetime import datetime 

def add_member():
    while(True):
        first_name = input("Enter your first name: ")
        last_name = input("Enter your last name: ")

        if first_name.isalpha and last_name.isalpha: break
        else: print("Invalid name(s), please try again!")
    while(True):
        age = input("Enter your age in years: ")
        if validate_age(age): break
        else: print("Invalid age, please try again!")
    while(True):
        gender = input("Enter your gender male/female: ")
        if validate_gender(gender): break
        else: print("Invalid gender, please try again!")
    while(True):
        weight = input("Enter your weight in kg: ")
        if(validate_weight(weight)) : break
        else: print("Invalid weight, please try again!")
    while(True):
        email = input("Enter your email-address: ")
        if(validate_email(email)) : break
        else: print("Invalid email, please try again!")
    while(True):
        street_name = input("Enter your street name: ")
        house_number = input("Enter your house number: ")
        zip_code = input("Enter your zipcode (DDDDXX): ")
        for place in cities: print(place)
        city = input("Enter one of those cities: ")
        if (validate_address(street_name, house_number, zip_code, city)) : break 
        else: print("Invalid address, please try again!")
    while(True):
        phone = input("Enter your phone number without +31 6: ")
        if(validate_phone(phone)) : break
        else:  print("Invalid phone number, please try again!")

    # add member to the database
    membership_id = create_unique_id()
    registration_date = datetime.now()
    address = f"{street_name} {house_number}, {zip_code} {city}"
    phone = f"+31-6-{phone}"

    conn =get_connection()
    if conn is None:
        print("Failed to connect to database")
        return False

    query = '''
            INSERT INTO members (membership_id, first_name, last_name, age, gender, weight, address, email, phone, registration_date)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        '''
    send_query(conn, query, (membership_id, first_name, last_name, age, gender, weight, address, email, phone, registration_date))
    conn.close()
    print("Member added successfully!")
    return True

def update_member_information():
    print("TODO")

def search_member():
    print("TODO")

def delete_member():
    print("TODO")