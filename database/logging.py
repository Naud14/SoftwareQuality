from datetime import datetime
from database.database import send_query
from database.auth import decrypt_data, encrypt_data


def see_logs():
    logs = send_query('''SELECT * FROM logs''')
    for row in logs:
        print(', '.join([decrypt_data(cell) for cell in row]))


def log_activity(username, description, additional_info=None, suspicious=0):
    date = datetime.now().strftime("%Y-%m-%d")
    time = datetime.now().strftime("%H:%M:%S")

    send_query(f'''
    INSERT INTO logs (date, time, username, description, additional_info, suspicious)
    VALUES ({encrypt_data(date)}, {encrypt_data(time)}, {encrypt_data(username)}, 
    {encrypt_data(description)}, {encrypt_data(additional_info)}, {encrypt_data(suspicious)})
    ''')
