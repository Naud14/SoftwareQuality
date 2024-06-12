from datetime import datetime
from database.database import send_query

def see_logs():
    print("TODO")

def log_activity(username, description, additional_info=None, suspicious=0):
    date = datetime.now().strftime("%Y-%m-%d")
    time = datetime.now().strftime("%H:%M:%S")

    send_query(f'''
    INSERT INTO logs (date, time, username, description, additional_info, suspicious)
    VALUES ({date}, {time}, {username}, {description}, {additional_info}, {suspicious})
    ''')
