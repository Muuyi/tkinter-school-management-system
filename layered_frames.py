from tkinter import *
from tkinter import ttk
import modules
from database import connect
from tkinter import messagebox
#=========================Registration frame=================
class RegistrationFrame(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        connection = connect()
        clsListsFrame = ttk.LabelFrame(self, text="CLASS LISTS")
        clsListsFrame.pack()
        clsTables = ttk.Treeview(clsListsFrame)
        clsTables['columns'] = ('Name','Gender','KCPE Marks','Guardian\'s name','Guardian\'s contact','Date of Birth', 'Date of Admission')
        clsTables.heading('#0', text='Name')
        clsTables.heading('#1', text='Gender')
        clsTables.heading('#2', text='KCPE Marks')
        clsTables.heading('#3', text='Guardian\'s name')
        clsTables.heading('#4', text='Guardian\'s contact')
        clsTables.heading('#5', text='Date of Birth')
        clsTables.heading('#6', text='Date of Admission')
        #Database values
        try:
            with connection.cursor() as cursor:
                qry = "SELECT * FROM home_students"
                cursor.execute(qry)
                result = cursor.fetchall()
        finally:
            connection.close()
        clsTables.pack()
        btnsFrames = ttk.Frame(self)
        btnsFrames.pack()
        btnNew = ttk.Button(btnsFrames, text="New", command=modules.RegistrationFunctions().display_new_tplvlwndw)
        btnNew.pack(side=LEFT)
        btnEdit = ttk.Button(btnsFrames, text="Edit")
        btnEdit.pack(side=LEFT)
        btnDelete = ttk.Button(btnsFrames, text="Delete")
        btnDelete.pack(side=LEFT)
        btnPrint = ttk.Button(btnsFrames, text="Print")
        btnPrint.pack(side=LEFT)

class Registration(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        lbl = ttk.Label(self, text="Registration page")
        lbl.pack()
        btn = ttk.Button(self, text="Frames slides", command=lambda:controller.show_frame(RegistrationFrame))
        btn.pack()
