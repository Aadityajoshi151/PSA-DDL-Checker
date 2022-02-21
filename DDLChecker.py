from tkinter import *
from tkinter import ttk,filedialog,messagebox
import tkinter.scrolledtext as scrolledtext
import webbrowser
import validators
import platform

class PSADDLChecker:

    def openurl(self,url):
        if OS_WINDOWS:
            webbrowser.open(url,new=1)
        else:
            webbrowser.open_new_tab(url)

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
        self.clearURLbox()
        self.urlbox.insert(END,filename.read())
        filename.close()

    def checkall(self):
        self.geturls()
        if urls[0] == "" and urls[1] == "":
            messagebox.showerror("No URLS","No URLs present")
            return
        open_all_response= messagebox.askyesno("Are You Sure",f"This may open <={len(urls)-1} tabs. Are you sure you want to proceed?")
        if open_all_response:
            for url in urls:
                if validators.url(url):
                    self.openurl(url)
    
    def checkselection(self):
        try:
            selectedurls = self.urlbox.selection_get().split("\n")
            for url in selectedurls:
                if validators.url(url):
                    self.openurl(url)
        except:
            messagebox.showerror("No Selection","Please Select Something")
  
    def checkspecefic(self,name):
        flag=True
        self.geturls()
        for url in urls:
            if name in url:
                self.openurl(url)
                flag=False
        if flag:
            messagebox.showerror("Not Found","No links with "+name+" was found")

    def clearURLbox(self):
        self.urlbox.delete(1.0,END)

    def __init__(self,app):
        self.urlbox = scrolledtext.ScrolledText(app,width=90,height=24,undo=True)  
        self.urlbox.grid(row=0,column=0,padx=10,pady=2)

        self.verticalbtnsframe = Frame(app)
        self.verticalbtnsframe.grid(row=0,column=1)

        self.horizontalbtnsframe = Frame(app)
        self.horizontalbtnsframe.grid(row=1,column=0)

        self.uptoboxbtn = ttk.Button(self.verticalbtnsframe,text="Uptobox Check",command=lambda: self.checkspecefic("uptobox"))
        self.uptoboxbtn.grid(row=0,column=0,padx=5,pady=5)

        self.megabtn = ttk.Button(self.verticalbtnsframe,text="Mega Check",command=lambda: self.checkspecefic("mega.nz"))
        self.megabtn.grid(row=1,column=0,padx=5,pady=5)

        self.sendcmbtn = ttk.Button(self.verticalbtnsframe,text="Send.cm Check",command=lambda: self.checkspecefic("send.cm"))
        self.sendcmbtn.grid(row=2,column=0,padx=5,pady=5)

        self.katfilebtn = ttk.Button(self.verticalbtnsframe,text="Katfile Check",command=lambda: self.checkspecefic("katfile"))
        self.katfilebtn.grid(row=3,column=0,padx=5,pady=5)

        self.clicknuploadbtn = ttk.Button(self.verticalbtnsframe,text="Clicknupload Check",command=lambda: self.checkspecefic("clicknupload"))
        self.clicknuploadbtn.grid(row=4,column=0,padx=5)

        self.megaloadbtn = ttk.Button(self.verticalbtnsframe,text="Megaload Check",command=lambda: self.checkspecefic("megaload"))
        self.megaloadbtn.grid(row=5,column=0,padx=5,pady=5)

        self.zippysharebtn = ttk.Button(self.verticalbtnsframe,text="Zippyshare Check",command=lambda: self.checkspecefic("zippyshare"))
        self.zippysharebtn.grid(row=6,column=0,padx=5,pady=5)

        self.anonfilesbtn = ttk.Button(self.verticalbtnsframe,text="Anonfiles Check",command=lambda: self.checkspecefic("anonfiles"))
        self.anonfilesbtn.grid(row=7,column=0,padx=5,pady=5)

        self.bayfilesbtn = ttk.Button(self.verticalbtnsframe,text="Bayfiles Check",command=lambda: self.checkspecefic("bayfiles"))
        self.bayfilesbtn.grid(row=8,column=0,padx=5,pady=5)

        self.ddownloadbtn = ttk.Button(self.verticalbtnsframe,text="DDownload Check",command=lambda: self.checkspecefic("ddownload"))
        self.ddownloadbtn.grid(row=9,column=0,padx=5,pady=5)

        self.megaupbtn = ttk.Button(self.verticalbtnsframe,text="Megaup Check",command=lambda: self.checkspecefic("megaup"))
        self.megaupbtn.grid(row=10,column=0,padx=5,pady=5)

        self.dropapkbtn = ttk.Button(self.verticalbtnsframe,text="Dropapk Check",command=lambda: self.checkspecefic("dropapk"))
        self.dropapkbtn.grid(row=11,column=0,padx=5,pady=5)

        self.clearbtn = ttk.Button(self.horizontalbtnsframe,text="Clear",command=self.clearURLbox)
        self.clearbtn.grid(row=0,column=0,padx=5,pady=5)

        self.openbtn = ttk.Button(self.horizontalbtnsframe,text="Open .txt",command=self.openfile)
        self.openbtn.grid(row=0,column=1,padx=5,pady=5)

        self.addseparatorbtn = ttk.Button(self.horizontalbtnsframe,text="Add Separator",command=lambda: self.urlbox.insert(END,"*"*80+"\n"))
        self.addseparatorbtn.grid(row=0,column=2,padx=5,pady=5)

        self.savebtn = ttk.Button(self.horizontalbtnsframe,text="Save .txt",command=self.savefile)
        self.savebtn.grid(row=0,column=3,padx=5,pady=5)

        self.checkselectionbtn = Button(self.horizontalbtnsframe,text="Check Selection",fg="green",command=self.checkselection)
        self.checkselectionbtn.grid(row=0,column=4,padx=5,pady=5)
        
        self.checkallbtn = Button(self.horizontalbtnsframe,text="Check All",fg="red",command=self.checkall)
        self.checkallbtn.grid(row=0,column=5,padx=5,pady=5)

def main():
    global OS_WINDOWS
    if platform.system() == 'Windows': OS_WINDOWS = True
    else: OS_WINDOWS = False
    root = Tk()
    root.title("PSA DDL Checker")
    root.resizable("False","False")
    if OS_WINDOWS:
        root.iconbitmap(default="assets/icon.ico")
    obj = PSADDLChecker(root)
    root.mainloop()

if __name__ == "__main__":
    main()