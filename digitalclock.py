#GUI
from tkinter import*
from tkinter import font
from datetime import datetime, time
from typing import TextIO
 
 
def finish(*args):
    global window
    window.destory()

def clock_time():
    time =datetime.now()
    time=time.strftime('%H:%M:%S')
    txt.set(time)
    window.after(1000,clock_time)
window = Tk()
window.title('My Digital clock')
window.geometry('850x200')
window.configure(background='black')
window.after(1000,clock_time)
window.bind("<Escape>",finish)
fnt= font.Font(family='helvetica',size=120,weight='bold')
txt=StringVar()
lbl=Label(window,textvariable=txt,font=fnt,foreground='yellow',background='black')
lbl.place(relx=0.5,rely=0.5,anchor=CENTER)
window.mainloop()