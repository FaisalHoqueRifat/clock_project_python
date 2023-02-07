from tkinter import *
from tkinter.ttk import *
from time import strftime
root = Tk()
root.title("Clock")
def time():
    string = strftime('     %I : %M : %S %p\n        %A\n %B %d, %Y')
    #string = strftime('%H:%M:%S %p')
    label.config(text = string)
    label.after(1000, time)
label = Label(root, font = ("ds-digital", 40), background = "black",foreground = "pink")
label.pack(anchor = 'center')

Label(root,text = 'ID: C221076', font = ("Times New Roman", 20), foreground = 'purple').pack(side=BOTTOM)
Label(root,text = 'Creator - Md. Faisal Hoque Rifat', font = ("Times New Roman", 20), foreground = 'purple').pack(side=BOTTOM)
time()
mainloop()
