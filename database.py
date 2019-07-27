import pymysql
#from functions import RegistrationFunctions
def connect():
    connection = pymysql.connect("localhost", "root", "","smis",charset="utf8mb4",cursorclass=pymysql.cursors.DictCursor)
    return connection



"""class RegistrationData(functions.RegistrationFunctions):
    def save_registration_data(self):
        print ('Hey')"""
