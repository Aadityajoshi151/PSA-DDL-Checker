from tkinter import *
from tkinter import ttk

root = Tk()
root.title("PSA DDL Checker")

class PSADDLChecker:

    def addseparator(self):
        self.urlbox.insert(END,"\n"+"*"*80+"\n")


    def __init__(self,app):
        self.urlbox = Text(app,width=80,height=10)  
        self.urlbox.grid(row=0,column=0,padx=10,pady=10)

        self.verticalbtnsframe = Frame(app)
        self.verticalbtnsframe.grid(row=0,column=1)

        self.horizontalbtnsframe = Frame(app)
        self.horizontalbtnsframe.grid(row=1,column=0)

        self.uptoboxbtn = ttk.Button(self.verticalbtnsframe,text="Uptobox Check")
        self.uptoboxbtn.grid(row=0,column=0,padx=5,pady=5)

        self.megabtn = ttk.Button(self.verticalbtnsframe,text="Mega Check")
        self.megabtn.grid(row=1,column=0,padx=5,pady=5)

        self.nitroflarebtn = ttk.Button(self.verticalbtnsframe,text="Nitroflare Check")
        self.nitroflarebtn.grid(row=2,column=0,padx=5,pady=5)

        self.katfilebtn = ttk.Button(self.verticalbtnsframe,text="Katfile Check")
        self.katfilebtn.grid(row=3,column=0,padx=5,pady=5)

        self.openloadbtn = ttk.Button(self.verticalbtnsframe,text="Openload Check")
        self.openloadbtn.grid(row=4,column=0,padx=5,pady=5)

        self.addseparatorbtn = ttk.Button(self.horizontalbtnsframe,text="Add Separator",command=self.addseparator)
        self.addseparatorbtn.grid(row=0,column=0,padx=5,pady=5)

        self.savebtn = ttk.Button(self.horizontalbtnsframe,text="Save .txt")
        self.savebtn.grid(row=0,column=1,padx=5,pady=5)
        
        self.checkallbtn = ttk.Button(self.horizontalbtnsframe,text="Check All")
        self.checkallbtn.grid(row=0,column=2,padx=5,pady=5)

obj = PSADDLChecker(root)
root.mainloop()