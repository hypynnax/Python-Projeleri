from tkinter import *
from tkcalendar import DateEntry


window = Tk(className=" Not Uygulaması")
window.resizable(False, False)
window.geometry("+%d+%d" % ((1366/2 - 550/2), (768/2 - 750/2)))
window.iconbitmap('C:\\Users\\hypyn\\OneDrive\\Belgeler\\Python Projeleri\\NotUygulamasi\\Notes.ico')

size = Canvas(window, height=550, width=750, background='#FFFFFF', highlightbackground='#FFFFFF')
size.pack()

ust_frame = Frame(size, background='#FF7F00', height=75, width=700)
ust_frame.place(relx=0.035, rely=0.07)

Label(ust_frame, background='#ADD8FF', text= "Hatırlatma Zamanı", font= 'Impact').place(relx=0.65, rely=0.4)
hatirlatma_zamani = DateEntry(ust_frame, width=12, background='#FF7F00', foreground='#000000', borderwidth=1, locale="de_DE")
hatirlatma_zamani._top_cal.iconbitmap('C:\\Users\\hypyn\\OneDrive\\Belgeler\\Python Projeleri\\NotUygulamasi\\Calendar.ico')
hatirlatma_zamani._top_cal.title("Takvim")
hatirlatma_zamani.place(relx=0.85, rely=0.43)

alt_frame = Frame(window, background='#ADD8FF', height=415, width=700)
alt_frame.place(relx=0.035, rely=0.21)

Label(alt_frame, background='#ADD8FF', text="Hatırlatma Mesajı", font="Impact").place(relx=0.05, rely=0.05)
ilk_metin = "Buraya bir mesaj girin"
text_area = Text(alt_frame, background='#FFFFFF', foreground='#000000', insertbackground='#48A1FF', height=18, width=80)
text_area.insert('end', ilk_metin)
text_area.place(relx=0.04, rely=0.15)

def kaydet():
    kayit_ekrani = Tk(className=" Kayıt")
    kayit_ekrani.resizable(False, False)
    kayit_ekrani.geometry("+%d+%d" % ((1366/2 - 210/2), (768/2 - 100/2)))
    kayit_ekrani.iconbitmap('C:\\Users\\hypyn\\OneDrive\\Belgeler\\Python Projeleri\\NotUygulamasi\\Save.ico')

    kayit_ekrani_size = Canvas(kayit_ekrani, width=210, height=100, background='#FFFFFF', highlightbackground= '#000000')
    kayit_ekrani_size.pack()

    text_alani = Text(kayit_ekrani_size, height=1, width=13, font='Arial 20', background='#000000', foreground='#FFFFFF', insertbackground='#48A1FF')
    text_alani.place(relx=0.038, rely=0.05)

    def kayit_et():
        dosya_adi = text_alani.get("1.0", "end-1c") + '.txt'
        tarih = hatirlatma_zamani.get()
        text = text_area.get('1.0', 'end')
        with open(dosya_adi, 'w') as dosya:
            dosya.write('   '*37)
            dosya.write("{}\n{}".format(tarih, text))
            dosya.close()
        kayit_ekrani.destroy()
        window.destroy()

    kaydet_butonu = Button(kayit_ekrani_size, borderwidth=5, text="Kaydet", height=1, width=6, font=30, background='#FFFFFF', foreground='#000000', activebackground='#FF0000', activeforeground='#FFFFFF', command=kayit_et)
    kaydet_butonu.place(relx=0.35, rely=0.5)

kaydet_butonu = Button(alt_frame, borderwidth=5, text="Kaydet", height=1, width=7, font='Impact', background='#FF7F00', foreground='#66FF00', activebackground='#66FF00', activeforeground='#FF7F00', command=kaydet)
kaydet_butonu.place(relx=0.46, rely=0.88)

window.mainloop()
