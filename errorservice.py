# Modules
import re
import maskpass
import mysql.connector
from mysql.connector import Error


errorInput = input("Input Error: ")
if errorInput == "":
    raise Exception("No input")

languageInput = input("Input the language: ")
if errorInput == "":
    raise Exception("No input")



try:
    # Connector to the DB
        connection = mysql.connector.connect(host='ne-mysqldb-dev.mysql.database.azure.com',
                                            database='db001_registro',
                                            user='mysqladmin',
                                            password='Wlachain$2022')
        
        if connection.is_connected:
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            cursor = connection.cursor()
            checkErrorQuery = """select err_desc from db001_registro.error where err_id = {errorInput} and err_language = '{languageInput}'""".format(errorInput=errorInput, languageInput=languageInput)

            cursor.execute(checkErrorQuery)
            record = cursor.fetchall()
            
            #print(record)
            
            if(len(record) < 1):
                raise Exception("Does not exist in database")
            else:
                print(record)
            
            cursor.close
            
        
except Error as e:
        print("Error: ", e)

finally:
        if connection.is_connected():
                connection.close()