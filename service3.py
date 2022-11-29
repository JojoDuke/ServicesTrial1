# Modules
import re
import mysql.connector
from mysql.connector import Error

# User Variables
user_status = 1
user_mail = 'jojo@gmail.com'
user_countrycode = 'GH'
user_name = 'Jojo'
user_surname = 'Duke'
user_phonenumber = '0240369071'
user_language = 'EN'
user_presenterID = '2'
psw_password = 'pass'


# Add Inputs

# Input name
input_userName = input("Input your name: ")
if input_userName == "":
    raise Exception("ERROR")

# Input surname
input_userSurname = input("Input your surname: ")
if input_userSurname == "":
    raise Exception("ERROR")

# Input phonenumber
input_userPhoneNumber = input("Input your phone number: ")
if input_userPhoneNumber.isalpha():
    raise ValueError("ERROR this is not a value")
elif input_userPhoneNumber == "":
    raise Exception("ERROR")

# Input user progr
input_userProgr = input("Input your user progr/ID: ")
if input_userProgr.isalpha():
    raise ValueError("ERROR, This is not a value")

# Input user email
regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

input_userEmail = input("Input your email: ")
if (re.search(regex, input_userEmail)):
    print(input_userEmail, " is a valid email address")
else:
    raise Exception("ERROR ID 2, email is invalid")

try:
    # Connector to the DB
    connection = mysql.connector.connect(host='ne-mysqldb-dev.mysql.database.azure.com',
                                         database='db001_registro',
                                         user='mysqladmin',
                                         password='Wlachain$2022')
    
    # Check if DB is connected and perform certain tasks
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        select_query = """select user_mail from db001_registro.user where user_progr = {input_userProgr} and user_mail = '{input_userEmail}'""".format(input_userProgr=input_userProgr, input_userEmail=input_userEmail)
        
        update_query = """update db001_registro.user set 
            user_status = 3, 
            user_name = '{input_userName}', 
            user_surname = '{input_userSurname}', 
            user_phonenumber = '{input_userPhoneNumber}'
            where user_mail = '{input_userEmail}'""".format(input_userName=input_userName, input_userSurname=input_userSurname, input_userPhoneNumber=input_userPhoneNumber, input_userEmail=input_userEmail)
        
        cursor.execute(select_query)
        record = cursor.fetchone()
        
        # Check if record from select_query exists
        if len(record) < 1:
            raise Exception("ERROR ID 4")
        else:
            print(record)
        
        
        cursor.execute(update_query)
        connection.commit()
        print("User Email matches and status has been updated!")
        
        cursor.close()

except Error as e:
    print("Error: ", e)

finally:
    if connection.is_connected():
        connection.close()
        print("MySQL connection is closed")
    