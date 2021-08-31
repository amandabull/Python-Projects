#import tkinter and webbrowesr
import tkinter
from tkinter import *
import webbrowser

#Setting up the configurations of the GUI
class ParentWindow(Frame):
    def __init__ (self, master):
        Frame.__init__ (self)

        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(700, 400))
        self.master.title('Web Page Generator!')
        self.master.config(bg='lightgrey')

        #Creating a labeled field for the user to input their website's message
        self.varBody = StringVar() 
        
        self.lblBody = Label(self.master, text='Website Text: ', font=("Helvetica", 16), fg='black', bg='lightblue')
        self.lblBody.grid(row=0, column=0, padx=(30,0), pady=(30,0))

        self.lblDisplay = Label(self.master, text='', font=("Helvetica", 16), fg='black', bg='lightblue')
        self.lblDisplay.grid(row=3, column=1, padx=(30,0), pady=(30,0))

        self.txtBody = Entry(self.master, text=self.varBody, font=("Helvetica", 16), fg='black', bg='lightblue')
        self.txtBody.grid(row=0, column=1, padx=(30,0), pady=(30,0))

        #Creating two different buttons so the user can either submit their message or cancel the process
        self.btnSubmit = Button(self.master, text="Submit", width=10, height=2, command=self.submit)
        self.btnSubmit.grid(row=2, column=1, padx=(0,0), pady=(30,0), sticky=NE)

        self.btnCancel = Button(self.master, text="Cancel", width=10, height=2, command=self.cancel)
        self.btnCancel.grid(row=2, column=1, padx=(0,90), pady=(30,0), sticky=NE)

    #Submission process that will rewrite the new message in the html file and open the file in a browser or user can cancel
    def submit(self):
        body = self.varBody.get()
        
        f = open("webpage.html", "w")
        f.write("<!DOCTYPE html> \n<html> \n\t<body> \n\t\t<h1> \n\t\t\t{} \n\t\t</h1> \n\t</body> \n</html>".format(body))
        f.close()
        
         #open and read the file after appending:
        f = open("webpage.html", "r")
        print(f.read())

        url = 'webpage.html'
        f = webbrowser.open_new_tab(url)

    def cancel(self):
        self.master.destroy()

        
if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
  
