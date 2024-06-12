from validate.py import validate_weight, validate_phone, validate_address, validate_email, validate_gender, validate_age

def add_member():
    while(true):
        first_name = input("Enter your first name: ")
        last_name = input("Enter your last name: ")
        
        if first_name.isalpha and last_name.isalpha: break
        else: print("Invalid name(s), please try again!")
    while(true):
        age = input("Enter your age in years: ")
        if validate_age(age): break
        else: print("Invalid age, please try again!")
    while(true):
        gender = input("Enter your gender male/female: ")
        if validate_gender(gender): break
        else: print("Invalid gender, please try again!")
    while(true):
        weight = input("Enter your weight in kg: ")
        if(validate_weight(weight)) : break
        else: print("Invalid weight, please try again!")
    while(true):
        email = input("Enter your email-address: ")
        if(validate_email(email)) : break
        else: print("Invalid email, please try again!")
    while(true):
        phone = input("Enter your phone number without +31 6: ")
        if(validate_phone(phone)) : break
        else:  print("Invalid phone number, please try again!")