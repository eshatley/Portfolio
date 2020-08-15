#import required libraries/modules

#So we can make a GUI application
from tkinter import * 
#Used to send alerts/messages/etc to the user
from tkinter import messagebox 
#Functions and classes for file creation
from tkinter import filedialog 

class textEditor:

    #Contructor
    def __init__(self, root):
        self.root = root
        #Window title. Come up with something more inspired later
        self.root.title("Simple Text") 
        #Window dimensions
        self.root.geometry("1200x700+200+150")
        self.filename = None
        self.title = StringVar()
        self.status = StringVar()
        
        #Create a Title bar
        self.titlebar = Label(self.root, textvariable = self.title, font  = ("times new roman", 15, "bold"), bd = 2, relief = GROOVE)
        self.titlebar.pack(side = TOP, fill = BOTH)
        self.setTitle()
        
        #Create status bar
        self.statusbar = Label(self.root, textvariable = self.status, font = ("times new roman", 15 "bold"), bd = 2, relief = GROOVE)
        self.statusbar.pack(side = BOTTOM, fill = BOTH)
        self.status.set("Welcome")
        
        #Create a menu bar
        self.filemenu = Menu(self.menubar, font = ("times new roman", 15, "bold"), activebackground="blue", tearoff = 0)
        self.root.config(menu = self.menubar)
        
        #"File" menu
        self.filemenu = Menu(self.menubar, font = ("times new roman", 12, "bold"), activebackground = "blue", tearoff = 0)
        
        #"New File"
        self.filemenu.add_command(label = "New File", accelerator = "Ctrl+N", command = self.newfile)
        
        #"Open File"
        self.filemenu.add_command(label = "Open", accelerator = "Ctrl+O", command = self.openfile)
        
        #"Save File"
        self.filemenu.add_command(label = "Save", accelerator = "Ctrl+S", command = self.savefile)
        
        #"Save As"
        self.filemenu.add_command(label = "Save as", accelerator = "Ctrl+A", command = self.saveasfile)
        
        #Add seperator
        self.filemenu.add_seperator()
        
        #Exit-Window command
        self.filemenu.add_command(label = "Exit", accelerator = "Ctrl+E", command = self.exit)
        
        #Cascading filemenu on menubar
        self.menubar.add_cascade(label = "File", menu = self.filemenu)
        
        #Edit Menu
        self.editmenu = Menu(self.menubar, font = ("times new roman", 12, "bold"), activebackground = "blue", tearoff = 0)
        
        #"Copy to Clipboard"
        self.editmenu.add_command(label = "Copy", accelerator = "Ctrl+C", command = self.copy)
        
        #"Paste from Clipboard"
        self.editmenu.add_command(label = "Paste", accelerator = "Ctrl+V", command = self.paste)
        
        #Seperator
        self.editmenu.add_seperator()
        
        #"Undo"
        self.editmenu.add_command(label = "Undo", accelerator = "Ctrl+U", command = self.undo)
        
        #Make it cascade
        self.menubar.add_cascade(label = "Edit", menu = self.editmenu)
        
        #Create a help menu
        self.helpmenu = Menu(self.menubar, font = ("times new roman", 12, "bold), activebackground = "blue", tearoff = 0)
        
        #"About" button, eventually add info about app
        self.helpmenu.add_command(label = "About", accelerator = "Ctrl+H", command = self.infoabout)
        
        #Create a Scrollbar
        scrollBarY = Scrollbar(self.root, orient = VERTICAL)
        
        #Text Area
        self.textArea = Text (self.root, yscrolcommand = scrollBarY.set, font = ("times new roman", 15, "bold"), state = "normal", relief = GROOVE)
        
        #Attach scroll bar to root window
        scrollBarY.pack(side = RIGHT, fill = Y)
        #Attach scrollbar to text area
        scrollBarY.config(command = self.textArea.yview)
        
        #Attach Text Area to root window
        self.textArea.pack(fill = BOTH, expand = 1)
        
        #Call shortcuts function
        self.shortcuts()
        
        #Settitle function
        
    def setTitle(self):
        #Make sure filename isn't none
        if self.filename::
            self.title.set(self.filename)                                           
        else:
            self.title.set("Untitled")                                           
        
    #New file function  
    def newfile(self, *args):
        #Clear the text area
        self.textArea.delete("1.0", END)                                           
        #Reset filename to none
        self.filename = None
        #Update title and status                                           
        self.setTitle()                                           
        self.status.set("Created new File")
        
    #Open file function
    def openfile(self, *args):
        #In case of exception
        try:
            self.filename = filedialog.askopenfilename(title = "Select file", filetypes = (("All Files", "*.*"), ("Text Files", "*.txt"), ("Python Files", "*.py")))
            if self.filename:
                #Open in read mode
                infile = open(self.filename, "r")   
                #Clear textArea
                self.textArea.delete("1.0", END)     
                #Fill textArea with data line by line    
                for line in infile:
                    selt.textArea.insert(END, line)
                #Close the file
                infile.close()
                #Update Status
                self.status.set("File Opened Succesfully")
         except Exception as e:
                messagebox.showerror("Exception Error", e)
                                                       
    #Save File Function
    def savefile(self, *args):
        #Handle exceptions
        try:
            #Make sure it has a filename
            if self.filename:
                #Read in data from textArea
                data = self.textArea.get("1.0", END)   
                #Open file in write mode and write data into it
                outfile = open(self.filename, "w")
                outfile.write(data)
                #Close the file
                outfile.close()
                #Set the title
                self.settitle()
                #Update Status
                self.status.set("File Saved Succesfully")
            else:
                self.saveasfile()
        except Exception as e:
            messagebox.showerror("Exception Error", e)
                                                       
    #Save file as function
    def saveasfile (self, *args):
        #Handle those exceptions
        try:
            #Ask for file type and name
            untitledfile = filedialog.asksaveasfilename(title = "Save File As", defaultextension = ".txt", initialfile = "Untitled.txt", filetypes = (("All Files", "*.*"), "Text Files", "*.txt"), ("Python Files", "*.py"))) 
           #Read the data in the textArea
           data = selt.textArea.get("1,0", END)
           #Open file in write mode and save data to it
           outfile = open(untitledfile, "w")
           outfile.write(data)
           #Close the file
           outfile.close()
           #Update filename to untitled
           self.filename = untitledfile
           #Set title
           self.settitle()
           #Update status
           self.status.set("File Saved Succesfully")
        except Exception as e:
            messagebox.showerror("Exception Error", e)
                             
    #Exit Function
    def exit(self, *args):
        warn = messagebox.askyesno("Warning", "Any Unsaved Data Will Be Lost!")                         
        if warn > 0:
            self.root.destroy()
        eles:
            return
                             
    #Define Editing Functions
                             
    #Cut
    def cut(self, *args):
        self.textArea.event-generate("<<Cut>>")
                             
    #Copy
    def copy(self, *args):
        self.textArea.event_generate("<<Copy>>")
            
    #Paste
    def paste(self, *args):
        self.textArea.event_generate("<<Paste>>")
                             
    #Undo
    def undo(self, *args):
        #Handle Exceptions
        try:
            #Make sure file name isn't none
            if self.filename:
                self.textArea.delete("1.0", END)
                infile = open(self.filename, "r")  
                for line in infile:
                    self.textArea.insert(END, line)
                infile.close()
                self.settitle()
                self.status.set("Undone!")
            else:
                self.textArea.delete("1.0", END)
                self.filename = None
                self.settitle()
                self.status.set("Undone!")
        except Exception as e:
            messagebox.showerror("Exception", e)
                             
    #Where the About info will go
    def info(self):
        messagebox.showinfo("About Simple Text", "A simple text editor")
                             
    #Bind shortcuts to the appropriate keys
    def shortcuts(self):
        self.textArea.bind("<Control-n>", self.newfile)
        self.textArea.bind("<Control-o>", self.openfile)
        self.textArea.bind("<Control-s>", self.savefile)
        self.textArea.bind("<Control-a>", self.saveasfile)
        self.textArea.bind("<Control-e>", self.exit)
        self.textArea.bind("<Control-x>", self.cut)
        self.textArea.bind("<Control-c>", self.copy)
        self.textArea.bind("<Control-v>", self.paste)
        self.textArea.bind("<Control-u>", self.undo)
                             
#Create a TK Container
root = Tk()
textEditor(root)
root.mainloop()                             
                             
