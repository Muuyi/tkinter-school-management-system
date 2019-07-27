from tkinter import *
from tkinter import ttk
import modules
import layered_frames
from tkinter import messagebox
class MainPanel:
    #========OPENING THE MAIN WINDOW PANEL=====
        def __init__(self,*args, **kwargs):
            mainPanel = Toplevel()
            #mainPanel.geometry('2000x2000')
            #  mainPanel.iconbitmap(r'icons/school.ico')
            #==========MENU BAR ITEMS====================
            menu = Menu(mainPanel)
            mainPanel.config(menu=menu)
            #==========FILE SUBMENU=============================
            file = Menu(menu, tearoff=0)
            file.add_command(label="Exit", command=mainPanel.destroy)
            #=========EDIT SUBMENU=============================
            edit = Menu(menu, tearoff=0)
            edit.add_command(label="Edit")
            #=========ADMISSION SUBMENU=============================
            admission = Menu(menu)
            admission.add_command(label="Register")
            admission.add_command(label="Class settings", command=modules.RegistrationFunctions().class_settings)
            admission.add_command(label="Departments settings", command=modules.RegistrationFunctions().departments_settings)
            admission.add_command(label="Societies settings",
                                  command=modules.RegistrationFunctions().religion)
            admission.add_command(label="Student categories",
                                  command=modules.RegistrationFunctions().religion)
            admission.add_command(label="Registration settings")
            #=========BOARDING SUBMENU======================
            boarding = Menu(menu)
            boarding.add_command(label="Hostels", command=modules.BoardingFunctions().hostels)
            boarding.add_command(label="Equipments/Facilities", command=modules.BoardingFunctions().boarding_equipments)
            #=============MENU BAR CONTENTS===================
            menu.add_cascade(label="File", menu=file)
            menu.add_cascade(label="Edit", menu=edit)
            menu.add_cascade(label="Admissions", menu=admission)
            menu.add_cascade(label="Finance")
            menu.add_cascade(label="Boarding", menu=boarding)
            menu.add_cascade(label="Examination")
            menu.add_cascade(label="Library")
            menu.add_cascade(label="Human Resource")
            menu.add_cascade(label="Procurement & stores")
            menu.add_cascade(label="Utilities")
            menu.add_cascade(label="Help")
            #==========TOOLBAR========================
            toolBar = Frame(mainPanel, bd=1, relief=RAISED)
            tbName = ttk.Label(toolBar, text="SMIS").pack(side=LEFT)
            toolBar.pack(side=TOP,fill=X)
            #=========CONTENT PANEL====================
            #contentPanel = Frame(mainPanel).pack()
            #==========ASIDE FRAME===================
            contentPanel = ttk.Frame(mainPanel)
            contentPanel.pack()
            #============LEF SIDE FRAME=======
            leftFrame = ttk.Frame(mainPanel, relief=RAISED)
            leftFrame.pack(side=LEFT)
            #=========ASIDE BAR TREE VIEW PROPERTIES====
            treeView = ttk.Treeview(contentPanel)
            treeView.pack(side=LEFT)
            treeView.heading('#0', text='Modules')
            treeView.insert('', '0', 'item1', text='Admissions')
            #****ADMISSIONS ITEMS****/
            treeView.insert('item1','end', text='Register')
            treeView.insert('item1', 'end', text='Class settings')
            treeView.insert('item1', 'end', text='Department settings')
            treeView.insert('item1','end', text='Registration settings')
            #===========FINANCE ITEMS=======
            treeView.insert('', '1', 'item2', text='Finance')
            #===========BOARDING ITEMS=======
            treeView.insert('', '2', 'item3', text='Boarding')
            treeView.insert('item3','end', text='Hostels')
            treeView.insert('item3', 'end', text='Equipments/Facilities')
            treeView.item('item1', open=TRUE)
            treeView.insert('', '3', 'item4', text='Examinations')
            treeView.insert('', '4', 'item5', text='Library')
            treeView.insert('', '5', 'item6', text='Human Resource')
            treeView.insert('', '6', 'item7', text='Procurement & stores')
            treeView.insert('', '7', 'item8', text='Utilities')

            #===========CONTENT OF THE RIGHT SECTION=========
            """container = Frame(contentPanel)
            container.pack(side=LEFT, fill="both", expand=True)
            container.grid_rowconfigure(0, weight=1)
            container.grid_columnconfigure(0, weight=1)
            lbl = Label(container, text="This is content section")
            lbl.pack()"""
            container = ttk.Frame(contentPanel)
            container.pack(side=LEFT, fill="both", expand=True)
            container.grid_rowconfigure(0, weight=1)
            container.grid_columnconfigure(0, weight=1)
            self.frames = {}
            for F in (layered_frames.RegistrationFrame, layered_frames.Registration):
                frame = F(container, self)
                self.frames[F] = frame
                frame.grid(row=0, column=0, stick="nsew")
                self.show_frame(layered_frames.RegistrationFrame)
            #============status bar===============
            statusBar = Frame(mainPanel, bd=1, relief=SUNKEN)
            sbName = ttk.Label(statusBar, text="Username", anchor=W).pack()
            statusBar.pack(side=BOTTOM, fill=X)
    #========================SHOW FRAME FUNCTION============
        def show_frame(self, frame_name):
            frame = self.frames[frame_name]
            frame.tkraise()
    #=========SHOWING THE LAYERED FRAMES
