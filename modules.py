from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import time
import datetime
import main
from database import connect
import pymysql
import functions
#from tkcalendar import calendar
#=======LOGIN CLASS FUNCTION OBJECTS===
class LoginFunctions:
    def fn_login(self):
        self.run = main.MainPanel()
        self.run()

    #========CLOSING THE LOGIN WINDOW WHEN THE MAIN WINDOW IS OPENED===
    def exit_login(self):
        self.master.destroy()
#========REGISTRATION FUNCTIONS OBJECT==
class RegistrationFunctions:
    connection = connect()
    #===========REGISTER SECTION===========
    def display_new_tplvlwndw(self):
        new_tplvl = Toplevel()
        new_tplvl.title("Student Registration")
        new_tplvl.wm_attributes("-topmost",1)
        #==================Personal details frame===========================
        personal_details_frame = ttk.LabelFrame(new_tplvl, text="Personal Details")
        personal_details_frame.pack(fill=X)
        lblSName = ttk.Label(personal_details_frame, text="Sir name:")
        lblSName.grid(row=0,column=0, sticky="E")
        entrySName = ttk.Entry(personal_details_frame)
        entrySName.grid(row=0,column=1)

        sname = StringVar()
        fname = StringVar()
        lname = StringVar()
        # dob = StringVar()
        gender = StringVar()
        religion = StringVar()
        gfname = StringVar()
        glname = StringVar()
        gcontact = StringVar()
        admnno = StringVar()
        # doa = StringVar()
        hostel = StringVar()
        stclass = StringVar()
        stream = StringVar()
        pschool = StringVar()
        kcpe = StringVar()
        # dob.set(time.strftime("%d/%m/%Y"))
        # doa.set(time.strftime("%d/%m/%Y"))
        #======================INPUT FIELDS VALUES==========
        sclass = stclass.get()

        lblFName = ttk.Label(personal_details_frame, text="First name:")
        lblFName.grid(row=0,column=2, sticky="E")
        entryFName = ttk.Entry(personal_details_frame)
        entryFName.grid(row=0,column=3)

        lblLName = ttk.Label(personal_details_frame, text="Last name:")
        lblLName.grid(row=0,column=4, sticky="E")
        entryLName = ttk.Entry(personal_details_frame)
        entryLName.grid(row=0,column=5)

        lblGender = ttk.Label(personal_details_frame, text="Gender:").grid(row=1, column=0)
        comboGender = ttk.Combobox(personal_details_frame, textvariable=gender)
        comboGender.grid(row=1, column=1)
        comboGender.config(values=('Male','Female'))

        lblDoB = ttk.Label(personal_details_frame, text="Date of Birth:")
        lblDoB.grid(row=1,column=2, sticky="E")
        entryDoB = ttk.Entry(personal_details_frame)
        entryDoB.grid(row=1,column=3)

        lblReligion = ttk.Label(personal_details_frame, text="Religion:")
        lblReligion.grid(row=1,column=4, sticky="E")
        #values = []
        comboValues = functions.Registration().religion_combo()
        """for v in comboValues.values():
            values.append(v)
        print(values)"""
        #print(comboValues)
        comboReligion = ttk.Combobox(personal_details_frame, textvariable=religion)
        comboReligion.grid(row=1,column=5)
        comboReligion['values'] = comboValues

        lblGFName = ttk.Label(personal_details_frame, text="Guardian First name:")
        lblGFName.grid(row=2,column=0, sticky="E")
        entryGFName = ttk.Entry(personal_details_frame)
        entryGFName.grid(row=2,column=1)

        lblGLName = ttk.Label(personal_details_frame, text="Guardian Last name:")
        lblGLName.grid(row=2,column=2, sticky="E")
        entryGLName = ttk.Entry(personal_details_frame)
        entryGLName.grid(row=2,column=3)

        lblGContact = ttk.Label(personal_details_frame, text="Guardian contacts:")
        lblGContact.grid(row=2,column=4, sticky="E")
        entryGContact = ttk.Entry(personal_details_frame)
        entryGContact.grid(row=2,column=5)
        #================School details=================
        school_details_frame = ttk.LabelFrame(new_tplvl, text="Institution Details")
        school_details_frame.pack(fill=X)
        lblAdmnNo = ttk.Label(school_details_frame, text="Admission No:")
        lblAdmnNo.grid(row=0,column=0, sticky="E")
        entryAdmnNo = ttk.Entry(school_details_frame)
        entryAdmnNo.grid(row=0,column=1)

        lblDoA = ttk.Label(school_details_frame, text="Date of Admission:")
        lblDoA.grid(row=0,column=2, sticky="E")
        entryDoA = ttk.Entry(school_details_frame)
        entryDoA.grid(row=0,column=3)

        lblHostel = ttk.Label(school_details_frame, text="Hostel name:")
        lblHostel.grid(row=0,column=4, sticky="E")
        entryHostel = ttk.Entry(school_details_frame)
        entryHostel.grid(row=0,column=5)

        lblClass = ttk.Label(school_details_frame, text="Class:")
        lblClass.grid(row=1,column=0, sticky="E")
        comboClass = ttk.Combobox(school_details_frame, textvariable="stclass")
        comboClass.grid(row=1,column=1)
        comboClass['values'] = functions.Registration().class_combo()
        comboClass.bind('<<ComboboxSelected>>', lambda e: functions.Registration().fill_stream_combo(sclass))

        lblStream = ttk.Label(school_details_frame, text="Stream:")
        lblStream.grid(row=1,column=2, sticky="E")
        entryStream = ttk.Entry(school_details_frame)
        entryStream.grid(row=1,column=3)

        lblPSchool = ttk.Label(school_details_frame, text="Primary school:")
        lblPSchool.grid(row=1,column=4, sticky="E")
        entryPSchool = ttk.Entry(school_details_frame)
        entryPSchool.grid(row=1,column=5)

        lblKcpe = ttk.Label(school_details_frame, text="KCPE Marks:")
        lblKcpe.grid(row=2,column=0, sticky="E")
        entryKcpe = ttk.Entry(school_details_frame)
        entryKcpe.grid(row=2,column=1)
        #================================Saving new data to the database====
        def save_data():
            connection = connect()


            sname = entrySName.get()
            fname = entryFName.get()
            lname = entryLName.get()
            #dob = entryDoB.get()
            #gender = rdoGender.get()
            #religion = entryReligion.get()
            gfname = entryGFName.get()
            glname = entryGLName.get()
            gcontact = entryGContact.get()
            admnno = entryAdmnNo.get()
            #doa = entryDoA.get()
            hostel = entryHostel.get()
            sclass = comboClass.get()
            stream = entryStream.get()
            pschool = entryPSchool.get()
            #kcpe = entryKcpe.get()
            try:
                with connection.cursor() as cursor:
                    sql = "INSERT INTO home_students(s_name,f_name,l_name,gender,g_fname,g_lname,g_contact,admn_no,hostel,clss,stream,primary_school) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                    cursor.execute(sql, (sname,fname,lname,gender,gfname,glname,gcontact,admnno,hostel,sclass,stream,pschool))
                    connection.commit()
                    print("Successfully commited")
            finally:
                connection.close()



        #=============================Buttons===================
        btnsFrame = Frame(new_tplvl)
        btnsFrame.pack(fill=X, expand=True)
        svBtn = ttk.Button(btnsFrame, text="Save", command=save_data)
        svBtn.grid(row=0, column=0)
        clrBtn = ttk.Button(btnsFrame, text="Reset")
        clrBtn.grid(row=0, column=1)
        cnclBtn = ttk.Button(btnsFrame, text="Cancel")
        cnclBtn.grid(row=0, column=2)
    #=========CLASS SETTINGS=====
    def class_settings(self):
        connection = connect()
        tplvl = Toplevel()
        tplvl.title("Class settings")
        clsFrame = ttk.Frame(tplvl)
        clsFrame.pack()
        clsTable = ttk.Treeview(clsFrame)
        clsTable['columns'] = ('Class','Total')
        clsTable.heading('#0', text='No')
        clsTable.heading('#1', text='Class')
        clsTable.heading('#2', text='Total')
        try:
            with connection.cursor() as cursor:
                sql = "SELECT * FROM home_studentclasses"
                cursor.execute(sql)
                result = cursor.fetchall()
                i = 0
                for row in result:
                    i += 1
                    clsTable.insert('','end',text=i,values=row['cls_name'])
        finally:
            connection.close()
        clsTable.pack()
        inputFrame = ttk.Frame(tplvl)
        inputFrame.pack(side=LEFT)
        lblClass = ttk.Label(inputFrame, text="Class name")
        lblClass.grid(row=0, column=0)

        entryClass = ttk.Entry(inputFrame)
        entryClass.grid(row=0, column=1)
        #==========SAVE CLASS FUNCTION
        def save_class():
            connection = connect()
            clsName = StringVar()
            clsName = entryClass.get()
            try:
                with connection.cursor() as cursor:
                    sql = "INSERT INTO home_studentclasses (cls_name) VALUES (%s)"
                    cursor.execute(sql, (clsName))
                    connection.commit()
                    print('Success')
            finally:
                connection.close()

        btnSave = ttk.Button(inputFrame, text="Save", command=save_class)
        btnSave.grid(row=0, column=2)
    #===========DEPARTMENT SETTINGS=========
    def departments_settings(self):
        connection = connect()
        depTplvl = Toplevel()
        depTplvl.title("Departments settings")
        depFrame= ttk.Frame(depTplvl)
        depFrame.pack()
        tblDep = ttk.Treeview(depFrame)
        tblDep['columns'] = ('No')
        tblDep.heading('#0', text='No')
        tblDep.heading('#1', text='Department name')
        #===============DISPLAYING TABLES CONTENTS=========
        try:
            with connection.cursor() as cursor:
                sql = "SELECT * FROM home_departments"
                cursor.execute(sql)
                result = cursor.fetchall()
                i = 0
                for row in result:
                    i += 1
                    tblDep.insert('',0,text=i, values=row['dep_name'])
        finally:
            connection.close()
        tblDep.pack()
        #==============Buttons sections============
        inputFrame = ttk.Frame(depTplvl)
        inputFrame.pack(side=LEFT)
        lblName = ttk.Label(inputFrame, text="Department name")
        lblName.grid(row=0, column=0)
        entryName = StringVar()
        entryName = ttk.Entry(inputFrame)
        entryName.grid(row=0, column=1)
        #==================SAVE DEPARTMENT FUNCTION===========
        def save_department():
            depName = entryName.get()
            try:
                with connection.cursor() as cursor:
                    sql = "INSERT INTO home_departments(dep_name) VALUES(%s)"
                    cursor.execute(sql, (depName))
                    connection.commit()
            finally:
                connection.close()

        btnSave = ttk.Button(inputFrame, text="Save", command=save_department)
        btnSave.grid(row=0, column=2)
    #============RELIGION SETTINGS============
    def religion(self):
        connection = connect()
        relTplvl = Toplevel()
        relFrame = ttk.Frame(relTplvl)
        relFrame.pack()
        relTable = ttk.Treeview(relFrame)
        relTable['columns'] = ('No')
        relTable.heading('#0', text='No')
        relTable.heading('#1', text='Religion')
        try:
            with connection.cursor() as cursor:
                sql = "SELECT * FROM home_societies"
                cursor.execute(sql)
                result = cursor.fetchall()
                i = 0
                for row in result:
                    i += 1
                    relTable.insert('','end',  text=i, value=row['society_name'])
        finally:
            connection.close()
        relTable.pack()
        relData = ttk.Frame(relTplvl)
        relData.pack()
        lblName = ttk.Label(relData, text="Religion name:")
        lblName.grid(row=0, column=0)
        relName = StringVar()

        entryName = ttk.Entry(relData)
        entryName.grid(row=0, column=1)
        #==============SAVING RELIGION FUNCTION
        def save_religion():
            connection = connect()
            relName = entryName.get()
            try:
                with connection.cursor() as cursor:
                    qry = "INSERT INTO home_societies (society_name) VALUES (%s)"
                    cursor.execute(qry, (relName))
                    connection.commit()
                    print('Success')
            finally:
                connection.close()

        btnSave = ttk.Button(relData, text="Save", command=save_religion)
        btnSave.grid(row=0, column=2)

#================BOADING FUNCTIONS OBJECTS==
class BoardingFunctions:
    #===================HOSTELS SECTION=================
    def hostels(self):
        connection = connect()
        """connection = pymysql.connect("localhost", "root", "", "smis", charset="utf8mb4",
                                     cursorclass=pymysql.cursors.DictCursor)"""
        hostels = Toplevel()
        hostels.title("Hostels")
        hostels.wm_attributes("-topmost",1)
        topFrame = ttk.Frame(hostels)
        topFrame.pack()
        hostelTable = ttk.Treeview(topFrame)
        hostelTable['columns'] = ('Hostel name')
        hostelTable.heading('#0',text='Hostel name')
        hostelTable.heading('#1',text='Capacity')
        #Displaying hostels values
        try:
            with connection.cursor() as cursor:
                qry = "SELECT host_name,max_no FROM home_hostels"
                cursor.execute(qry)
                result = cursor.fetchall()
                for row in result:
                    hostelTable.insert('',0,text=row['host_name'], values=row['max_no'])
        finally:
            connection.close()


        hostelTable.pack()

        inputFrame = ttk.Frame(hostels)
        inputFrame.pack(side=LEFT)
        #Variables
        hostName = StringVar()
        capacity = IntVar()

        lblHostName = ttk.Label(inputFrame, text='House name')
        lblHostName.grid(row=0,column=0, padx=5, pady=5)
        entryHostName = ttk.Entry(inputFrame, textvariable=hostName)
        entryHostName.grid(row=0, column=1, padx=5, pady=5)

        lblCapacity = ttk.Label(inputFrame, text='House capacity')
        lblCapacity.grid(row=1,column=0, padx=5, pady=5)
        entryCapacity = ttk.Entry(inputFrame, textvariable=capacity)
        entryCapacity.grid(row=1, column=1, padx=5, pady=5)

        def save_data():
            connection = connect()
            """connection = pymysql.connect("localhost", "root", "", "smis", charset="utf8mb4",
                                         cursorclass=pymysql.cursors.DictCursor)"""
            host = hostName.get()
            cap = capacity.get()

            #connection = Connection().connect
            try:
                with connection.cursor() as cursor:
                    sql = "INSERT INTO home_hostels (host_name,max_no) VALUES (%s,%s)"
                    cursor.execute(sql, (host,cap))
                    connection.commit()
            finally:
                connection.close()

        btnSave = ttk.Button(inputFrame, text="Save", command=save_data)
        btnSave.grid(row=0, column=2)
        btnEdit = ttk.Button(inputFrame, text='Edit')
        btnEdit.grid(row=1, column=2)
    #===================EQUIPMENTS/FACILITIES SECTION=================
    def boarding_equipments(self):
        equipTplvl = Toplevel()
        equipTplvl.title('Boarding equipments/Facilities')
        equipFrame = ttk.Frame(equipTplvl)
        equipFrame.pack()
        tblEquip = ttk.Treeview(equipFrame)
        tblEquip['columns'] = ('No','Item type', 'Item name')
        tblEquip.heading('#0',text='No')
        tblEquip.heading('#1', text='Item type')
        tblEquip.heading('#2', text='Item name')
        tblEquip.heading('#3', text='Quantity')
        tblEquip.pack()
        btnFrame = ttk.Frame(equipTplvl)
        btnFrame.pack()
        #==================New equipment=================
        def new_equipment():
            nwTplvl = Toplevel()
            lblType = ttk.Label(nwTplvl, text="Item type:")
            lblType.grid(row=0, column=0)
            entryType = ttk.Entry(nwTplvl).grid(row=0, column=1)

            lblName = ttk.Label(nwTplvl, text="Item name:").grid(row=1, column=0)
            entryName = ttk.Entry(nwTplvl).grid(row=1, column=1)
        btnSave = ttk.Button(btnFrame, text="New", command=new_equipment)
        btnSave.grid(row=0, column=0)
        btnEdit = ttk.Button(btnFrame, text="Edit")
        btnEdit.grid(row=0, column=1)