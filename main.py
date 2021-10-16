from tkinter import *
import os
from tkinter.filedialog import *
from tkinter import messagebox
root = Tk()
root.title("TkinterEdit ~ New File")


def savefile():
   file_location = asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Text","*.txt"), ("All files","*.*")])


   if not file_location:
      return
   with open(file_location, "w") as file_output:
       text = T.get(1.0, END)
       file_output.write(text)
   root.title(f"TkinterEdit ~ {file_location}")

def openfile():
    file_location = askopenfilename(
        filetypes=[("Text","*.txt"),("All files","*.*")])
    if not file_location:
        return
    T.delete(1.0, END)
    with open(file_location, "r") as file_input:
        text = file_input.read()
        T.insert(END, text)
    root.title(f"TkinterEdit ~ {file_location}")

def newfile():
    T.delete(1.0, END)
    root.title("TkinterEdit ~ New File")

def helpbttn():
    messagebox.showinfo("Tkinter Edit", "A really light and convenient text editor made with Python")


menubar = Menu(root)
T = Text(root)
T.pack(expand=True, fill='both')

filemenu = Menu(menubar, tearoff=0)
helpmenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=newfile)
filemenu.add_command(label="Open", command=openfile)
filemenu.add_command(label="Save", command=savefile)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)
menubar.add_command(label="Help", command=helpbttn)
root.config(menu=menubar)
root.mainloop()
