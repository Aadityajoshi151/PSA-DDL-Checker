from tkinter import *
from tkinter import ttk,filedialog,messagebox
import tkinter.scrolledtext as scrolledtext
from idlelib.tooltip import Hovertip
import webbrowser
import validators
import platform
import pyperclip

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

    def copySpeceficLinks(self, event, name):
        specefic_urls = ""
        flag=True
        self.geturls()
        for url in urls:
            if name in url:
                specefic_urls+=f"{url}\n"
                flag=False
        if flag:
            messagebox.showerror("Not Found","No links with "+name+" was found")
        else:
            pyperclip.copy(specefic_urls)
            print(specefic_urls.count("\n"))
            messagebox.showinfo("Copied",str(specefic_urls.count("\n"))+" "+name+" urls copied to clipboard")

    def __init__(self,app):
        Buttons = ['Uptobox','Mega.nz','Send.cm','Katfile','Clicknupload','Megaload','Zippyshare','Anonfiles','Bayfiles','DDownload','Megaup','Dropapk']
        self.urlbox = scrolledtext.ScrolledText(app,width=90,height=24,undo=True)  
        self.urlbox.grid(row=0,column=0,padx=10,pady=2)

        self.verticalbtnsframe = Frame(app)
        self.verticalbtnsframe.grid(row=0,column=1)

        self.horizontalbtnsframe = Frame(app)
        self.horizontalbtnsframe.grid(row=1,column=0)

        for i in range(len(Buttons)):
            self.b = ttk.Button(self.verticalbtnsframe, text=f'{Buttons[i]} Check', command=lambda i=i: self.checkspecefic(Buttons[i].lower()))
            self.b.grid(row=i, column=0,padx=5,pady=5)
            self.b.bind('<Button-3>',lambda event,i=i: self.copySpeceficLinks(event,Buttons[i].lower()))
            self.tooltip = Hovertip(self.b, f'Right click to copy all {Buttons[i].lower()} links to the clipboard')

        self.clearbtn = ttk.Button(self.horizontalbtnsframe,text="Clear",command=self.clearURLbox)
        self.clearbtn.grid(row=0,column=0,padx=5,pady=5)

        self.addseparatorbtn = ttk.Button(self.horizontalbtnsframe,text="Add Separator",command=lambda: self.urlbox.insert(END,"\n"+"*"*80+"\n"))
        self.addseparatorbtn.grid(row=0,column=1,padx=5,pady=5)

        self.checkselectionbtn = ttk.Button(self.horizontalbtnsframe,text="Check Selection",command=self.checkselection)
        self.checkselectionbtn.grid(row=0,column=2,padx=5,pady=5)
        
        self.checkallbtn = ttk.Button(self.horizontalbtnsframe,text="Check All",command=self.checkall)
        self.checkallbtn.grid(row=0,column=3,padx=5,pady=5)

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
    mymenu = Menu(root)
    root.config(menu=mymenu)
    # File Menu
    myfilemenu = Menu(mymenu, tearoff=False)
    mymenu.add_cascade(label="File", menu=myfilemenu)
    myfilemenu.add_command(label="Open .txt file (Ctrl+O)",command=obj.openfile)
    myfilemenu.add_command(label="Save .txt file (Ctrl+S)",command=obj.savefile)
    myfilemenu.add_separator()
    myfilemenu.add_command(label="Quit", command=lambda: root.quit())
    root.mainloop()

if __name__ == "__main__":
    main()