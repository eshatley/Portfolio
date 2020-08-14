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
        self.settitle()
        
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
        
        #Define the settitle function
        
        #WIP Add rest of code 
        
        
      
        
        
        
        
        
        
        
