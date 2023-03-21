from tkinter import *
import tkinter.messagebox as mg
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os

def new():
    global file
    root.title("Untitled - Notepad")
    file = None
    TextArea.delete(1.0, END)

def openFile():
    global file
    file = askopenfilename(defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                      ("Text Documents", "*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + " - Notepad")
        TextArea.delete(1.0, END)
        f = open(file, "r")
        TextArea.insert(1.0, f.read())
        f.close()

def save():
    global file
    if file == None:
        file = asksaveasfilename(initialfile='Untitled.txt', defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                      ("Text Documents", "*.txt")])
        if file == "":
            file = None

        else:
            #Save as a new file
            f = open(file, "w")
            f.write((TextArea.get(1.0, END)))
            f.close()
            root.title(os.path.basename(file) + " - Notepad")
    else:
        # Save The File
        f = open(file, "w")
        f.write(TextArea.get(1.0, END))
        f.close()

def cut():
    TextArea.event_generate(("<<Cut>>"))

def copy():
    TextArea.event_generate(("<<Copy>>"))

def paste():
    TextArea.event_generate(("<<Paste>>"))

def about():
    mg.showinfo("About GUI Notepad", "GUI Notepad © 2023. All rights reserved.")

def close():
    root.destroy()

root = Tk()
root.title("GUI Notepad")
root.iconbitmap("ico.ico")

# Create a Scrollbar
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

# Add TextArea
TextArea = Text(root, font="consolas 11", yscrollcommand=scrollbar.set)
file = None
TextArea.pack(expand=True, fill=BOTH)
scrollbar.config(command=TextArea.yview)

# Create a Menu

# File Menu
MenuBar = Menu(root)
FileMenu = Menu(MenuBar, tearoff=0)
FileMenu.add_command(label="New", command=new)
FileMenu.add_command(label="Open", command=openFile)
FileMenu.add_command(label="Save", command=save)
FileMenu.add_command(label="Exit", command=close)

MenuBar.add_cascade(label="File", menu=FileMenu)

# Edit Menu
EditMenu = Menu(root, tearoff=0)
EditMenu.add_command(label="Cut", command=cut)
EditMenu.add_command(label="Copy", command=copy)
EditMenu.add_command(label="Paste", command=paste)

MenuBar.add_cascade(label="Edit", menu=EditMenu)

# Help Menu
HelpMenu = Menu(root, tearoff=0)
HelpMenu.add_command(label="About this app", command=about)

MenuBar.add_cascade(label="Help", menu=HelpMenu)



root.config(menu=MenuBar)

root.mainloop()