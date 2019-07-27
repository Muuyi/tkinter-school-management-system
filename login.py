from tkinter import *
from tkinter import ttk
import modules
import main
import pymysql
from tkinter import messagebox
#########################LOGIN CLASS###########################
class Login:
    def __init__(self,master):
        self.master = master
        self.master.title("School Management Information System(SMIS)")
        #self.master.iconbitmap(r'icons/school.ico')
        #self.master.resizable(false,false)
#=========CONTENT PANEL====================
        #contentPanel = Frame(mainPanel).pack(fill=X,fill=Y)
        self.userName = ttk.Label(master, text="Username:", font=('arial 12 bold'))
        self.userName.grid(row=0,column=0, padx=10, pady=10)
        self.userPassword = ttk.Label(master, text="Password:", font=('arial 12 bold'))
        self.userPassword.grid(row=1,column=0, padx=10, pady=10)

        self.entryUserName = ttk.Entry(master, font=('arial 15'))
        self.entryUserName.grid(row=0,column=1, columnspan=2, padx=10, pady=10)
        self.entryPassword = ttk.Entry(master, font=('arial 15'))
        self.entryPassword.grid(row=1,column=1, columnspan=2, padx=10, pady=10)

        self.btnLogin = ttk.Button(master, text="Login",command=main.MainPanel())
        self.btnLogin.grid(row=2,column=0, padx=10, pady=10)
        self.btnForgotPass = ttk.Button(master, text="Forgot password")
        self.btnForgotPass.grid(row=2,column=1, padx=10, pady=10)
        self.btnCancel = ttk.Button(master, text="Cancel", command=self.master.destroy)
        self.btnCancel.grid(row=2,column=2, padx=10, pady=10)

        self.userName = Label(master, text="Connected", font=('arial 12 bold italic'))
        self.userName.grid(row=3, column=2, padx=10, pady=10)
    #=======MAIN PANEL WINDOW=======
    #def open_main_window(self):
    #    main = Toplevel()
    #    main.title("")"""
if __name__ == "__main__":
    root = Tk()
    login = Login(root)
    root.mainloop()
