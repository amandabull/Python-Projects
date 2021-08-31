#importing libraries
from tkinter import *
from tkinter import filedialog
import webbrowser
import os,time
import datetime
import shutil
import datetime as dt

#Setting up the configurations of the GUI
class ParentWindow(Frame):
    def __init__ (self, master):
        Frame.__init__ (self)

        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(500, 200))
        self.master.title('Check files')
        self.master.config(bg='lightgrey')

        #Creating a label, button, and entry field for the Source Folder
        self.lblBrowse1 = Label(self.master, text='Select the Source Folder:       ', font=("Arial", 10), bg='lightgrey')
        self.lblBrowse1.grid(row=0, column=0, padx=(0,0), pady=(5,0), sticky=E)

        self.btnBrowse1 = Button(self.master, text="Browse...", width=15, height=1, command=self.browse1)
        self.btnBrowse1.grid(row=1, column=0, padx=(0,20), pady=(0,10), sticky=NE)

        #Creating a label, button, and entry field for the Destination Folder
        self.lblBrowse2 = Label(self.master, text='Select the Destination Folder: ', font=("Arial", 10), bg='lightgrey')
        self.lblBrowse2.grid(row=2, column=0, padx=(20,0), pady=(5,0), sticky=NE)

        self.btnBrowse2 = Button(self.master, text="Browse...", width=15, height=1, command=self.browse2)
        self.btnBrowse2.grid(row=3, column=0, padx=(20,20), pady=(0,10), sticky=NE)

        #Creating a button to Check for Files or Cancel
        
        self.btnSubmit = Button(self.master, text="Check for files...", width=15, height=2, command=self.submit)
        self.btnSubmit.grid(row=4, column=0, padx=(20,20), pady=(5,0), sticky=NE)

        self.btnCancel = Button(self.master, text="Close Program", width=15, height=2, command=self.cancel)
        self.btnCancel.grid(row=4, column=3, padx=(0,0), pady=(5,0), sticky=NE)

    #Submission process that will rewrite the new message in the html file and open the file in a browser or user can cancel
    def browse1(self):
        global folder_selected1
        folder_selected1 = filedialog.askdirectory()
        print(folder_selected1)

    def browse2(self):
        global folder_selected2
        folder_selected2 = filedialog.askdirectory()
        print(folder_selected2)

    def submit(self):
        now = dt.datetime.now()
        ago = now-dt.timedelta(hours=24)
        strftime = "%H:%M %m/%d/%Y"
        source = folder_selected1
        dest = folder_selected2

        for root, dirs,files in os.walk(source):  
            for fname in files:
                path = os.path.join(root, fname)
                st = os.stat(path)    
                mtime = dt.datetime.fromtimestamp(st.st_mtime)
                if mtime > ago:
                    print(fname + " has been moved.")
                    shutil.move(path, dest)
                    # this is actual move
                    
    def cancel(self):
        self.master.destroy()
    

if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
    root.withdraw()
   
