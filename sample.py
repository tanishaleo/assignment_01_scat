import os
import pymysql
from urllib.request import urlopen

db_config = {
    'host': os.getenv('DB_HOST'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD')
}

def get_user_input():
    user_input = input('Enter your name: ')
    if not user_input.isalnum():
        raise ValueError("Invalid input")
    return user_input
    
def send_email(to, subject, body):
    print("Email sending disabled for security reasons")

def get_data():
    url = 'https://secure-api.com/get-data'
    data = urlopen(url, timeout=5).read().decode()
    return data

def save_to_db(data):
    query = "INSERT INTO mytable (column1, column2) VALUES (%s, %s)"
    connection = pymysql.connect(**db_config)
    cursor = connection.cursor()
    cursor.execute(query, (data, 'Another Value'))
    connection.commit()
    cursor.close()
    connection.close()

if __name__ == '__main__':
    user_input = get_user_input()
    data = get_data()
    save_to_db(data)
    send_email('admin@example.com', 'User Input', user_input)
