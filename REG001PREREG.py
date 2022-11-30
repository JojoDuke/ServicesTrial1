# Modules
import re
import maskpass
import mysql.connector
from mysql.connector import Error

# Service Functions
def service1():  
    # Adding inputs
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

    # Input user email
    print("\nCREATING USER")
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
    if input_userPresenterID != '2':
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
            query2 = """insert into db001_registro.user (user_mail, user_countrycode, user_presenterID, user_status) 
                        VALUES 
                        ('{input_userEmail}', '{input_userCountryCode}', '{input_userPresenterID}', 1)""".format(input_userEmail=input_userEmail, input_userCountryCode=input_userCountryCode, input_userPresenterID=input_userPresenterID)
            #cursor.execute(query)
            cursor.execute(query2)
            connection.commit()
            print(cursor.rowcount, "Record inserted successfully into table")
            
            cursor.close()

    except Error as e:
        print("Error: ", e)

    finally:
        if connection.is_connected():
            connection.close()
            print("\n REG007MAILVAL: Mail has been validated \n")
def service2():
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
            cursor = connection.cursor()
            select_query = """select user_mail from db001_registro.user where user_progr = {input_userProgr} and user_mail = '{input_userEmail}'""".format(input_userProgr=input_userProgr, input_userEmail=input_userEmail)
            update_query = """update db001_registro.user set user_status = 2 where user_mail = '{input_userEmail}'""".format(input_userEmail=input_userEmail)
            
            cursor.execute(select_query)
            record = cursor.fetchone()
            
            # Check if record from select_query exists
            if len(record) < 1:
                raise Exception("ERROR ID 4")
            else:
                print(record)
            
            
            cursor.execute(update_query)
            connection.commit()
            print("User Email matches and status has been updated! \n")
            
            cursor.close()

    except Error as e:
        print("Error: ", e)

    finally:
        if connection.is_connected():
            connection.close()
def service3():
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
            print("MySQL connection is closed \n")
            print("\n REG008PHONEVAL: Phone Number has been validated \n")
def service5():
    # Input username
    input_userUserName = input("Input your username: ")
    if input_userUserName == "":
        raise Exception("ERROR")

    # Input password
    #input_userPwd = input("Input your password: ")
    pwd = maskpass.askpass(prompt="Input your password: ", mask="*") 

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

    # Input App ID
    input_appID = input("Input your app ID: ")
    if input_appID == "":
        raise Exception("ERROR")

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
            check_email_query = """select user_mail from db001_registro.user where user_progr = {input_userProgr} and user_mail = '{input_userEmail}'""".format(input_userProgr=input_userProgr, input_userEmail=input_userEmail)
            check_appid_query = """select app_appid from db001_registro.app where app_appid = '{input_appID}'""".format(input_appID=input_appID)
            
            update_query = """update db001_registro.user set 
                user_status = 5
                where user_mail = '{input_userEmail}'""".format(input_userEmail=input_userEmail)
            
            #cursor.execute(check_email_query)
            cursor.execute(check_appid_query)
            record = cursor.fetchone()
            
            # Check if record from select_query exists
            if len(record) < 1:
                raise Exception("ERROR ID 4")
            else:
                print(record)
            
            
            cursor.execute(update_query)
            connection.commit()
            print("Updated! Email and AppID match")
            
            cursor.close()

    except Error as e:
        print("Error: ", e)

    finally:
        if connection.is_connected():
            connection.close()
            print("MySQL connection is closed")
            print("\n REG010PSWMNG: Password Management Process \n")

service1() 
service2()    
service3()   
service5() 