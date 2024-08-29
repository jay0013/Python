from tkinter import *
from tkinter.filedialog import asksaveasfile, askopenfile
from tkinter.messagebox import showerror

filename = None

def newFile():
    global filename
    filename = "Untitled"
    text.delete(1.0, END)  # Changed from 0.0 to 1.0 to indicate line 1, character 0

def saveFile():
    global filename
    if filename is None:
        saveAs()
    else:
        t = text.get(1.0, END)
        try:
            with open(filename, 'w') as f:
                f.write(t)
        except:
            showerror(title="Error!", message="Unable to save file...")

def saveAs():
    global filename
    f = asksaveasfile(mode='w', defaultextension='.txt')
    if f is not None:
        filename = f.name
        t = text.get(1.0, END)
        try:
            f.write(t.rstrip())
        except:
            showerror(title="Error!", message="Unable to save file...")

def openFile():
    global filename
    f = askopenfile(mode='r')
    if f is not None:
        filename = f.name
        t = f.read()
        text.delete(1.0, END)
        text.insert(1.0, t)

root = Tk()
root.title("Denny's Text Editor")
root.minsize(width=400, height=400)
root.maxsize(width=400, height=400)  # Corrected from mixsize to maxsize

text = Text(root, width=400, height=400)
text.pack()

menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)  # Added tearoff=0 to prevent menu tear-off
filemenu.add_command(label="New", command=newFile)
filemenu.add_command(label="Open", command=openFile)
filemenu.add_command(label="Save", command=saveFile)
filemenu.add_command(label="Save As", command=saveAs)
filemenu.add_separator()
filemenu.add_command(label="Quit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)  # Added quotes around 'File'

root.config(menu=menubar)
root.mainloop()


# from _tkinter import *
# from tkFileDialog import *

# filename = None
# def newFile():
#     global filename
#     filename = "Untitled"
#     text.delete(0.0, END)

# def saveFile():
#     global filename
#     t = text.get(0.0,END)
#     f = open(filename , w)
#     f.write(t)
#     f.close()

# def SaveAs():
#     f = asksaveasfile(mode='w',defaultextention='txt')
#     t = text.get(0.0, END)
#     try:
#         f.write(t.rstrip())
#     except:
#         showerror(title="Error!", message="Unable to save file...")

# def openFile():
#     f = askopenfile(mode='r')
#     t = f.read()
#     text.delete(0.0, END)
#     text.insert(0.0 , t)

# root = Tk()
# root.title("Denny's Text Editor")
# root.minsize(width=400 , height=400)
# root.mixsize(width=400 , height=400)

# text = Text(root , width=400 , height=400)
# text.pack()

# menubar = Menu(root)
# filemenu = Menu(menubar)
# filemenu.add_command(label="New" , command=newFile)
# filemenu.add_command(label="Open" , command=openFile)
# filemenu.add_command(label="Save" , command=saveFile)
# filemenu.add_command(label="Save As" , command=SaveAs)
# filemenu.add_separator()
# filemenu.add_command(label="Quit" , command=root.quit)
# menubar.add_cascade(label=File, menu = filemenu)

# root.config(menu=menubar)
# root.mainloop()