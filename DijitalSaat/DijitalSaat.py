import time
from tkinter import *


window = Tk(className=' Saat')
window.configure(height=500, width=1250, background='#000000')
window.geometry("+%d+%d" % ((1366/2 - 1250/2), (768/2 - 500/2)))
window.iconbitmap(default='C:\\Users\\hypyn\\OneDrive\\Belgeler\\Python Projeleri\\DijitalSaat\\Clock.ico')

saat = ''
kadran = Label(window, font=('DS-Digital','250'), text=saat, background='#000000', foreground='#48FF00')
kadran.place(relx=0.5, rely=0.5, anchor=CENTER)

def dijital_saat():
    global saat
    saat = time.strftime('%H:%M:%S')
    kadran.config(text=saat)
    kadran.after(100, dijital_saat)

dijital_saat()
window.mainloop()
