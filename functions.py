import pymysql
from database import connect
#=================================REGISTRATION MODULE FUNCTIONS==========
class Registration:

    #==================COLLECTING COMBO BOX VALUES FROM THE DATABASE AND DISPLAYING IT ON REGISTRATION RELIGION COMBOBOX===
    def religion_combo(self):
        connection = connect()
        comboList = []
        try:
            with connection.cursor() as cursor:
                sql = "SELECT society_name FROM home_societies"
                cursor.execute(sql)
                #result = cursor.fetchall()
                for row in cursor:
                    for v in row.values():
                        comboList.append(v)
        finally:
            connection.close()
        return comboList
    #======================GETTING THE CLASS COMBO BOX VALUES FROM THE DATABASE============
    def class_combo(self):
        self.connection = connect()
        clsList = []
        try:
            with self.connection.cursor() as cursor:
                sql = "SELECT cls_name FROM home_studentclasses"
                cursor.execute(sql)
                for row in cursor:
                    for v in row.values():
                        clsList.append(v)
        finally:
            self.connection.close()
        return clsList
    #=======================BINDING THE CLASS COMBO BOX TO THE STREAM COMBOBOX===========
    def fill_stream_combo(self,sclass):
        self.connection = connect()
        self.sclass = 'Form one'
        try:
            with self.connection.cursor() as cursor:
                sql = "SELECT cls_id FROM home_studentclasses WHERE cls_name='self.sclass'"
                cursor.execute(sql)
                val = cursor.fetchone()
                print(val)
        finally:
            self.connection.close()