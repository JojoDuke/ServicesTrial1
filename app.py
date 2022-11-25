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


# Adding inputs
regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

# Input user email
input_userEmail = input("Input your email: ")
if (re.search(regex, input_userEmail)):
    print(input_userEmail, " is a valid email address")
else:
    raise Exception("ERROR ID 2, email is invalid")
    
# Input user country code
input_userCountryCode = input("Input your country code: ")
if len(input_userCountryCode) >= 3:
    raise Exception("ERROR, invalid, country code cannot be more than 2")
elif len(input_userCountryCode) < 2:
    raise Exception("ERROR, invalid, country code must have 2")

# Input user presenter ID
input_userPresenterID =  input("Input your presenter ID: ")
if input_userPresenterID != user_presenterID:
    raise Exception("ERROR ID 6")

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
        query = "select user_mail from db001_registro.user where user_mail = '{input_userEmail}'".format(input_userEmail=input_userEmail)
        cursor.execute(query)
        records = cursor.fetchall()
        
        if len(records) < 1:
            print("Value does not exist in database")
        else:
            #print(records)
            if user_status > 5:
                raise Exception("ERROR ID 4")
            else:
                raise Exception("ERROR ID 3, User already exists")
            
        print(f"{len(records)} row(s) returned")

except Error as e:
    print("Error: ", e)

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
    