from tkinter import *
from tkinter import ttk,filedialog,messagebox
import webbrowser
import validators

class PSADDLChecker:

    def openurl(self,url):
        webbrowser.open(url,new=1)

    def geturls(self):
        global urls
        urls = self.urlbox.get(1.0,END).split("\n")    

    def savefile(self):
        filename = filedialog.asksaveasfile(title="Save File", mode='w', defaultextension=".txt",filetypes=[('Text Files', '.txt')])
        if filename is None:
            return
        filename.write(str(self.urlbox.get(1.0, END)))
        filename.close()

    def openfile(self):
        filename = filedialog.askopenfilename(title="Open File", filetypes=(("Text Files", "*.txt"),))
        filename = open(filename, 'r')
        self.urlbox.insert(END,filename.read())
        filename.close()

    def checkall(self):
        self.geturls()
        for url in urls:
            if validators.url(url):
                self.openurl(url)
    
    # def checkselection(self):
    #     selectedurls = self.urlbox.selection_get().split("\n")
    #     for url in selectedurls:
    #         if validators.url(url):
    #             self.openurl(url)
    
    def checkspecefic(self,name):
        flag=True
        self.geturls()
        for url in urls:
            if name in url:
                self.openurl(url)
                flag=False
        if flag:
            messagebox.showerror("Not Found","No links with "+name+" was found")


    def __init__(self,app):
        self.urlbox = Text(app,width=80,height=15)  
        self.urlbox.grid(row=0,column=0,padx=10,pady=2)

        self.verticalbtnsframe = Frame(app)
        self.verticalbtnsframe.grid(row=0,column=1)

        self.horizontalbtnsframe = Frame(app)
        self.horizontalbtnsframe.grid(row=1,column=0)

        self.uptoboxbtn = ttk.Button(self.verticalbtnsframe,text="Uptobox Check",command=lambda: self.checkspecefic("uptobox"))
        self.uptoboxbtn.grid(row=0,column=0,padx=5,pady=5)

        self.megabtn = ttk.Button(self.verticalbtnsframe,text="Mega Check",command=lambda: self.checkspecefic("mega.nz"))
        self.megabtn.grid(row=1,column=0,padx=5,pady=5)

        self.nitroflarebtn = ttk.Button(self.verticalbtnsframe,text="Nitroflare Check",command=lambda: self.checkspecefic("nitroflare"))
        self.nitroflarebtn.grid(row=2,column=0,padx=5,pady=5)

        self.katfilebtn = ttk.Button(self.verticalbtnsframe,text="Katfile Check",command=lambda: self.checkspecefic("katfile"))
        self.katfilebtn.grid(row=3,column=0,padx=5,pady=5)

        self.openloadbtn = ttk.Button(self.verticalbtnsframe,text="Openload Check",command=lambda: self.checkspecefic("openload.co"))
        self.openloadbtn.grid(row=4,column=0,padx=5)

        self.megaloadbtn = ttk.Button(self.verticalbtnsframe,text="Megaload Check",command=lambda: self.checkspecefic("megaload"))
        self.megaloadbtn.grid(row=5,column=0,padx=5,pady=5)

        self.zippysharebtn = ttk.Button(self.verticalbtnsframe,text="Zippyshare Check",command=lambda: self.checkspecefic("zippyshare"))
        self.zippysharebtn.grid(row=6,column=0,padx=5,pady=5)

        self.anonfilesbtn = ttk.Button(self.verticalbtnsframe,text="Anonfiles Check",command=lambda: self.checkspecefic("anonfiles"))
        self.anonfilesbtn.grid(row=7,column=0,padx=5,pady=5)

        self.clearbtn = ttk.Button(self.horizontalbtnsframe,text="Clear",command=lambda: self.urlbox.delete(1.0,END))
        self.clearbtn.grid(row=0,column=0,padx=5,pady=5)

        self.openbtn = ttk.Button(self.horizontalbtnsframe,text="Open .txt",command=self.openfile)
        self.openbtn.grid(row=0,column=1,padx=5,pady=5)

        self.addseparatorbtn = ttk.Button(self.horizontalbtnsframe,text="Add Separator",command=lambda: self.urlbox.insert(END,"\n"+"*"*80+"\n"))
        self.addseparatorbtn.grid(row=0,column=2,padx=5,pady=5)

        self.savebtn = ttk.Button(self.horizontalbtnsframe,text="Save .txt",command=self.savefile)
        self.savebtn.grid(row=0,column=3,padx=5,pady=5)

        self.checkselectionbtn = ttk.Button(self.horizontalbtnsframe,text="Check Selection",command=self.checkselection)
        self.checkselectionbtn.grid(row=0,column=4,padx=5,pady=5)
        
        self.checkallbtn = ttk.Button(self.horizontalbtnsframe,text="Check All",command=self.checkall)
        self.checkallbtn.grid(row=0,column=5,padx=5,pady=5)

def main():
    root = Tk()
    root.title("PSA DDL Checker")
    root.resizable("False","False")
    root.iconbitmap(default="icon.ico")
    obj = PSADDLChecker(root)
    root.mainloop()

if __name__ == "__main__":
    main()