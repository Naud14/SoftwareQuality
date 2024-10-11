from logic.validate import validate_weight, validate_phone, validate_address, validate_email, validate_gender, validate_age
from logic.validate import cities
from database.database import get_connection, send_query
from database.auth import create_unique_id
from datetime import datetime 

def add_member():
    while(True):
        first_name = input("Enter your first name: ")
        last_name = input("Enter your last name: ")

        if first_name.isalpha() and last_name.isalpha(): break
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
    # print("Member added successfully!")
    print("Your new membership ID is: ", membership_id)
    return True

def update_member_information():
    print("TODO")

def search_member():
    print("Search member")
    membership_id = input("Enter the membership ID of the member to search: ")

    try:
        conn = get_connection()
        if conn is not None:
            query = "SELECT * FROM members WHERE membership_id = ?"
            result = send_query(conn, query, (membership_id))
            print(result)
            input()
    except Exception as e:
        print("Failed to find member.")
        print(e)

def delete_member():
    print("Delete member")
    membership_id = input("Enter the membership ID of the member to delete: ")

    try:
        conn = get_connection()
        if conn is not None:
            # Check if the provided membership ID exists in the database
            query = "SELECT * FROM members WHERE membership_id = ?"
            result = send_query(conn, query, (membership_id,))
            
            if result:
                # If the membership ID exists, proceed with the deletion
                delete_query = "DELETE FROM members WHERE membership_id = ?"
                send_query(conn, delete_query, (membership_id,))
                print("Member deleted successfully!")
            else:
                print("No member found with the provided membership ID.")
            
            conn.close()
        else:
            print("Failed to connect to the database.")
    except Exception as e:
        print("Failed to delete member.")
        print(e)