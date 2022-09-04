from tkinter import *


window = Tk(className=" Yapılacaklar Listesi")
window.resizable(False, False)
window.geometry("+%d+%d" % ((1366/2 - 490/2), (768/2 - 750/2)))
window.iconbitmap(default='C:\\Users\\hypyn\\OneDrive\\Belgeler\\Python Projeleri\\YapilacaklarListesi\\To-Do List.ico')

size = Canvas(window, width=600, height=800, background='#000000', highlightbackground= '#000000')
size.pack()

tahta = Frame(size, width=470, height=650, background='#AA4400', highlightbackground= '#AA4400')
tahta.pack(padx=10, pady=10)

sayfa = Frame(tahta, width=415, height=594, background='#FFFFFF')
sayfa.place(relx=0.0595, rely=0.048)

baslik = Label(sayfa, text='Yapılacaklar Listesi', font=('Orange Juice', 30), background='#FFFFFF', foreground='#000000')
baslik.place(relx=0.09, rely=0.02)

def ekle_1():
    if metin_degeri_1.get() != '':
        metin_1.destroy()
        ekle_butonu_1.destroy()
        checkbutton_1 = Checkbutton(sayfa, text=metin_degeri_1.get(), variable=checkbutton_degeri_1, offvalue=0, onvalue=1, background='#FFFFFF', activebackground='#FFFFFF', foreground='#000000', font='Arial 20')
        checkbutton_1.place(relx=0.015, rely=0.14)
        return checkbutton_1.cget('text')
    else:
        return None
metin_degeri_1 = StringVar()
metin_1 = Entry(sayfa, textvariable=metin_degeri_1, width=20, background='#FFFFFF', foreground='#000000', insertbackground='#48A1FF', font='Arial 20')
metin_1.place(relx=0.1, rely=0.14)
checkbutton_degeri_1 = IntVar()
ekle_butonu_1 = Button(sayfa, borderwidth=5, text="Ekle", height=1, width=5, font=30, background='#FFFFFF', foreground='#000000', activebackground='#FFFFF0', activeforeground='#00FF00', command=ekle_1)
ekle_butonu_1.place(relx=0.84, rely=0.14)

def ekle_2():
    if metin_degeri_2.get() != '':
        metin_2.destroy()
        ekle_butonu_2.destroy()
        checkbutton_2 = Checkbutton(sayfa, text=metin_degeri_2.get(), variable=checkbutton_degeri_2, offvalue=0, onvalue=1, background='#FFFFFF', activebackground='#FFFFFF', foreground='#000000', font='Arial 20')
        checkbutton_2.place(relx=0.015, rely=0.24)
        return checkbutton_2.cget('text')
    else:
        return None
metin_degeri_2 = StringVar()
metin_2 = Entry(sayfa, textvariable=metin_degeri_2, width=20, background='#FFFFFF', foreground='#000000', insertbackground='#48A1FF', font='Arial 20')
metin_2.place(relx=0.1, rely=0.24)
checkbutton_degeri_2 = IntVar()
ekle_butonu_2 = Button(sayfa, borderwidth=5, text="Ekle", height=1, width=5, font=30, background='#FFFFFF', foreground='#000000', activebackground='#FFFFF0', activeforeground='#00FF00', command=ekle_2)
ekle_butonu_2.place(relx=0.84, rely=0.24)

def ekle_3():
    if metin_degeri_3.get() != '':
        metin_3.destroy()
        ekle_butonu_3.destroy()
        checkbutton_3 = Checkbutton(sayfa, text=metin_degeri_3.get(), variable=checkbutton_degeri_3, offvalue=0, onvalue=1, background='#FFFFFF', activebackground='#FFFFFF', foreground='#000000', font='Arial 20')
        checkbutton_3.place(relx=0.015, rely=0.34)
        return checkbutton_3.cget('text')
    else:
        return None
metin_degeri_3 = StringVar()
metin_3 = Entry(sayfa, textvariable=metin_degeri_3, width=20, background='#FFFFFF', foreground='#000000', insertbackground='#48A1FF', font='Arial 20')
metin_3.place(relx=0.1, rely=0.34)
checkbutton_degeri_3 = IntVar()
ekle_butonu_3 = Button(sayfa, borderwidth=5, text="Ekle", height=1, width=5, font=30, background='#FFFFFF', foreground='#000000', activebackground='#FFFFF0', activeforeground='#00FF00', command=ekle_3)
ekle_butonu_3.place(relx=0.84, rely=0.34)

def ekle_4():
    if metin_degeri_4.get() != '':
        metin_4.destroy()
        ekle_butonu_4.destroy()
        checkbutton_4 = Checkbutton(sayfa, text=metin_degeri_4.get(), variable=checkbutton_degeri_4, offvalue=0, onvalue=1, background='#FFFFFF', activebackground='#FFFFFF', foreground='#000000', font='Arial 20')
        checkbutton_4.place(relx=0.015, rely=0.44)
        return checkbutton_4.cget('text')
    else:
        return None
metin_degeri_4 = StringVar()
metin_4 = Entry(sayfa, textvariable=metin_degeri_4, width=20, background='#FFFFFF', foreground='#000000', insertbackground='#48A1FF', font='Arial 20')
metin_4.place(relx=0.1, rely=0.44)
checkbutton_degeri_4 = IntVar()
ekle_butonu_4 = Button(sayfa, borderwidth=5, text="Ekle", height=1, width=5, font=30, background='#FFFFFF', foreground='#000000', activebackground='#FFFFF0', activeforeground='#00FF00', command=ekle_4)
ekle_butonu_4.place(relx=0.84, rely=0.44)

def ekle_5():
    if metin_degeri_5.get() != '':
        metin_5.destroy()
        ekle_butonu_5.destroy()
        checkbutton_5 = Checkbutton(sayfa, text=metin_degeri_5.get(), variable=checkbutton_degeri_5, offvalue=0, onvalue=1, background='#FFFFFF', activebackground='#FFFFFF', foreground='#000000', font='Arial 20')
        checkbutton_5.place(relx=0.015, rely=0.54)
        return checkbutton_5.cget('text')
    else:
        return None
metin_degeri_5 = StringVar()
metin_5 = Entry(sayfa, textvariable=metin_degeri_5, width=20, background='#FFFFFF', foreground='#000000', insertbackground='#48A1FF', font='Arial 20')
metin_5.place(relx=0.1, rely=0.54)
checkbutton_degeri_5 = IntVar()
ekle_butonu_5 = Button(sayfa, borderwidth=5, text="Ekle", height=1, width=5, font=30, background='#FFFFFF', foreground='#000000', activebackground='#FFFFF0', activeforeground='#00FF00', command=ekle_5)
ekle_butonu_5.place(relx=0.84, rely=0.54)

def ekle_6():
    if metin_degeri_6.get() != '':
        metin_6.destroy()
        ekle_butonu_6.destroy()
        checkbutton_6 = Checkbutton(sayfa, text=metin_degeri_6.get(), variable=checkbutton_degeri_6, offvalue=0, onvalue=1, background='#FFFFFF', activebackground='#FFFFFF', foreground='#000000', font='Arial 20')
        checkbutton_6.place(relx=0.015, rely=0.64)
        return checkbutton_6.cget('text')
    else:
        return None
metin_degeri_6 = StringVar()
metin_6 = Entry(sayfa, textvariable=metin_degeri_6, width=20, background='#FFFFFF', foreground='#000000', insertbackground='#48A1FF', font='Arial 20')
metin_6.place(relx=0.1, rely=0.64)
checkbutton_degeri_6 = IntVar()
ekle_butonu_6 = Button(sayfa, borderwidth=5, text="Ekle", height=1, width=5, font=30, background='#FFFFFF', foreground='#000000', activebackground='#FFFFF0', activeforeground='#00FF00', command=ekle_6)
ekle_butonu_6.place(relx=0.84, rely=0.64)

def ekle_7():
    if metin_degeri_7.get() != '':
        metin_7.destroy()
        ekle_butonu_7.destroy()
        checkbutton_7 = Checkbutton(sayfa, text=metin_degeri_7.get(), variable=checkbutton_degeri_7, offvalue=0, onvalue=1, background='#FFFFFF', activebackground='#FFFFFF', foreground='#000000', font='Arial 20')
        checkbutton_7.place(relx=0.015, rely=0.74)
        return checkbutton_7.cget('text')
    else:
        return None
metin_degeri_7 = StringVar()
metin_7 = Entry(sayfa, textvariable=metin_degeri_7, width=20, background='#FFFFFF', foreground='#000000', insertbackground='#48A1FF', font='Arial 20')
metin_7.place(relx=0.1, rely=0.74)
checkbutton_degeri_7 = IntVar()
ekle_butonu_7 = Button(sayfa, borderwidth=5, text="Ekle", height=1, width=5, font=30, background='#FFFFFF', foreground='#000000', activebackground='#FFFFF0', activeforeground='#00FF00', command=ekle_7)
ekle_butonu_7.place(relx=0.84, rely=0.74)

def ekle_8():
    if metin_degeri_8.get() != '':
        metin_8.destroy()
        ekle_butonu_8.destroy()
        checkbutton_8 = Checkbutton(sayfa, text=metin_degeri_8.get(), variable=checkbutton_degeri_8, offvalue=0, onvalue=1, background='#FFFFFF', activebackground='#FFFFFF', foreground='#000000', font='Arial 20')
        checkbutton_8.place(relx=0.015, rely=0.84)
        return checkbutton_8.cget('text')
    else:
        return None
metin_degeri_8 = StringVar()
metin_8 = Entry(sayfa, textvariable=metin_degeri_8, width=20, background='#FFFFFF', foreground='#000000', insertbackground='#48A1FF', font='Arial 20')
metin_8.place(relx=0.1, rely=0.84)
checkbutton_degeri_8 = IntVar()
ekle_butonu_8 = Button(sayfa, borderwidth=5, text="Ekle", height=1, width=5, font=30, background='#FFFFFF', foreground='#000000', activebackground='#FFFFF0', activeforeground='#00FF00', command=ekle_8)
ekle_butonu_8.place(relx=0.84, rely=0.84)

def kaydet():
    kayit_ekrani = Tk(className=" Kayıt")
    kayit_ekrani.resizable(False, False)
    kayit_ekrani.geometry("+%d+%d" % ((1366/2 - 210/2), (768/2 - 400/2)))
    kayit_ekrani.iconbitmap('C:\\Users\\hypyn\\OneDrive\\Belgeler\\Python Projeleri\\YapilacaklarListesi\\Save.ico')

    kayit_ekrani_size = Canvas(kayit_ekrani, width=210, height=100, background='#FFFFFF', highlightbackground= '#000000')
    kayit_ekrani_size.pack()

    text = Text(kayit_ekrani_size, height=1, width=13, font='Arial 20', background='#000000', foreground='#FFFFFF', insertbackground='#48A1FF')
    text.place(relx=0.038, rely=0.05)

    def kayit_et():
        dosya_adi = text.get("1.0", "end-1c") + '.txt'
        satirlar = [ekle_1(), ekle_2(), ekle_3(), ekle_4(), ekle_5(), ekle_6(), ekle_7(), ekle_8()]
        print(satirlar)
        with open(dosya_adi, 'w') as dosya:
            i = 1
            for satir in satirlar:
                if satir != None:
                    dosya.write("{}. {}\n".format(i, satir))
                    i += 1
            dosya.close()
        kayit_ekrani.destroy()
        window.destroy()

    kaydet_butonu = Button(kayit_ekrani_size, borderwidth=5, text="Kaydet", height=1, width=6, font=30, background='#FFFFFF', foreground='#000000', activebackground='#FF0000', activeforeground='#FFFFFF', command=kayit_et)
    kaydet_butonu.place(relx=0.35, rely=0.5)

kaydet_butonu = Button(sayfa, borderwidth=5, text="Kaydet", height=1, width=6, font=30, background='#FFFFFF', foreground='#000000', activebackground='#FF0000', activeforeground='#FFFFFF', command=kaydet )
kaydet_butonu.place(relx=0.43, rely=0.925)

window.mainloop()
