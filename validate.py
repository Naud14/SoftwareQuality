import re
cities = ["Rotterdam", "Oldenzaal", "Budapest", "Kathmandu", "Moskou", "Lelystad", "Stockholm", "Ruinerwold", "Liverpool", "Penemunde"]


def check_first_name(name):
    return name.isalpha()


def validate_age(age):
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

def validate_username(username):
    # check if username is unique and no distinquish between lowercase or uppercase letters

    # no longer than 10 characters
    if len(username) > 10: return False

    # start with a letter or unerscore
    if not username[0].isalpha() and username[0] != '_': return False

    # can contain letters (a-z), numbers (0-9), underscores (_), apostrophes ('), and periods (.)
    if not all(char.isalpha() or char.isdigit() or char in ['_', "'", '.'] for char in username): return False
    
def validate_password(password):
    return False