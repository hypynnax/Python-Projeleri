import math
from tkinter import *

sonuc = 0
sayi = 0
son_basamak = 0
son_islem = ''
virgulden_sonra_basamak_sayisi = 0

def tus_bir():
    tus("1")
def tus_iki():
    tus("2")
def tus_uc():
    tus("3")
def tus_dort():
    tus("4")
def tus_bes():
    tus("5")
def tus_alti():
    tus("6")
def tus_yedi():
    tus("7")
def tus_sekiz():
    tus("8")
def tus_dokuz():
    tus("9")
def tus_sifir():
    tus("0")
def tus_arti():
    tus("+")
def tus_cikar():
    tus("-")
def tus_carp():
    tus("×")
def tus_bol():
    tus("÷")
def tus_yuzde():
    tus("%")
def tus_kare():
    tus("x²")
def tus_bir_bolu():
    tus("1/x")
def tus_karekok():
    tus("√x")
def tus_herseyi_sil():
    tus("C")
def tus_toplu_sil():
    tus("CE")
def tus_sil():
    tus("<x|")
def tus_zit():
    tus("±")
def tus_virgul():
    tus(",")
def tus_esit():
    tus("=")

def ekrana_yazdir(cikti):
    Label.config(self=ekran, text=str(cikti))

def tus(basilan_tus):
    global sonuc, sayi, son_islem, virgulden_sonra_basamak_sayisi, son_basamak
    if basilan_tus == '=':
        if son_islem == '+':
            sonuc += sayi
        elif son_islem == '-':
            sonuc -= sayi
        elif son_islem == '*':
            sonuc *= sayi
        elif son_islem == '/':
            sonuc /= sayi
        ekrana_yazdir(sonuc)
        sayi = 0
        virgulden_sonra_basamak_sayisi = 0
        sayi = int(sayi)
    elif basilan_tus == '+':
        if sonuc == 0:
            sonuc = sayi
            sayi = 0
        else:
            if sayi != 0:
                sonuc += sayi
                sayi = 0
            ekrana_yazdir(sonuc)
        son_islem = '+'
        virgulden_sonra_basamak_sayisi = 0
        sayi = int(sayi)
    elif basilan_tus == '-':
        if sonuc == 0:
            sonuc = sayi
            sayi = 0
        else:
            if sayi != 0:
                sonuc -= sayi
                sayi = 0
            ekrana_yazdir(sonuc)
        son_islem = '-'
        virgulden_sonra_basamak_sayisi = 0
        sayi = int(sayi)
    elif basilan_tus == '×':
        if sonuc == 0:
            sonuc = sayi
            sayi = 0
        else:
            if sayi != 0:
                sonuc *= sayi
                sayi = 0
            ekrana_yazdir(sonuc)
        son_islem = '*'
        virgulden_sonra_basamak_sayisi = 0
        sayi = int(sayi)
    elif basilan_tus == '÷':
        if sonuc == 0:
            sonuc = sayi
            sayi = 0
        else:
            if sayi != 0:
                sonuc /= sayi
                sayi = 0
            ekrana_yazdir(sonuc)
        son_islem = '/'
        virgulden_sonra_basamak_sayisi = 0
        sayi = int(sayi)
    elif basilan_tus == '%':
        if sayi == 0:
            sonuc **= 2
            sonuc /= 100
            ekrana_yazdir(sonuc)
        else:
            sayi **= 2
            sayi /= 100
            ekrana_yazdir(sayi)
    elif basilan_tus == 'x²':
        if sayi == 0:
            sonuc **= 2
            ekrana_yazdir(sonuc)
        else:
            sayi **= 2
            ekrana_yazdir(sayi)
    elif basilan_tus == '1/x':
        if sayi == 0:
            sonuc = 1 / sonuc
            ekrana_yazdir(sonuc)
        else:
            sayi = 1 / sayi
            ekrana_yazdir(sayi)
    elif basilan_tus == '√x':
        if sayi == 0:
            sonuc = int(math.sqrt(sonuc))
            ekrana_yazdir(sonuc)
        else:
            sayi = int(math.sqrt(sayi))
            ekrana_yazdir(sayi)
    elif basilan_tus == '<x|':
        if type(sayi) == float:
            if virgulden_sonra_basamak_sayisi == 0:
                sayi = int(sayi)
                ekrana_yazdir(sayi)
            else:
                print(son_basamak / (10**virgulden_sonra_basamak_sayisi))
                sayi -= son_basamak / (10**virgulden_sonra_basamak_sayisi)
                virgulden_sonra_basamak_sayisi -= 1
                ekrana_yazdir(sayi)
        else:
            sayi /= 10
            sayi = int(sayi)
        ekrana_yazdir(sayi)
    elif basilan_tus == 'C':
        sayi = 0
        sonuc = 0
        son_islem = ''
        virgulden_sonra_basamak_sayisi = 0
        ekrana_yazdir(sonuc)
    elif basilan_tus == 'CE':
        sayi = 0
        virgulden_sonra_basamak_sayisi = 0
        ekrana_yazdir(sayi)
    elif basilan_tus == ',':
        sayi = float(sayi)
        if sayi == 0:
            ekrana_yazdir('0.')
        else:
            ekrana_yazdir("{}.".format(int(sayi)))
    elif basilan_tus == '±':
        if sayi == 0:
            sonuc *= -1
            ekrana_yazdir(sonuc)
        else:
            sayi *= -1
            ekrana_yazdir(sayi)
    elif int(basilan_tus) in range(10):
        if type(sayi) == float:
            if sayi == 0:
                sayi += int(basilan_tus) / 10
                virgulden_sonra_basamak_sayisi += 1
                ekrana_yazdir(sayi)
            else:
                virgulden_sonra_basamak_sayisi += 1
                katsayi = 10 ** virgulden_sonra_basamak_sayisi
                sayi += int(basilan_tus) / katsayi
                ekrana_yazdir(sayi)
            son_basamak = int(basilan_tus)
        else:
            if sayi == 0:
                sayi = int(basilan_tus)
                ekrana_yazdir(sayi)
            else:
                sayi *= 10
                sayi += int(basilan_tus)
                ekrana_yazdir(sayi)

window = Tk(className=' Hesap Makinesi')
window.resizable(False, False)
window.iconbitmap(default='C:\\Users\\hypyn\\OneDrive\\Belgeler\\Python Projeleri\\HesapMakinesi\\calculator.ico')

size = Canvas(height=498, width=315, background='#1f1f1f', highlightbackground= '#1f1f1f')
size.pack()

screen = Text(size, background='#1f1f1f', highlightbackground='#1f1f1f', foreground="white", font='Impact 40')
screen.place(relx=0, rely=0.15, height=77, width=320)

ekran = Label(screen, text='0', background='#1f1f1f', highlightbackground='#1f1f1f', foreground="white", font='Impact 40')
ekran.pack(side=RIGHT)

tus_yuzde = Button(size, activebackground='#494949', background='#131313', highlightbackground='#131313', text='%', foreground='#cbcbcb', font='Impact 20', command=tus_yuzde)
tus_yuzde.place(relx=0.012, rely=0.316, height=55, width=76.3, anchor=NW)

tus_toplu_sil = Button(size, activebackground='#494949', background='#131313', highlightbackground='#131313', text='CE', foreground='#cbcbcb', font='Impact 20', command=tus_toplu_sil)
tus_toplu_sil.place(relx=0.258, rely=0.316, height=55, width=76.3, anchor=NW)

tus_herseyi_sil = Button(size, activebackground='#494949', background='#131313', highlightbackground='white', text='C', foreground='#cbcbcb', font='Impact 20', command=tus_herseyi_sil)
tus_herseyi_sil.place(relx=0.503, rely=0.316, height=55, width=76.3, anchor=NW)

tus_sil = Button(size, activebackground='#494949', background='#131313', highlightbackground='white', text='<x|', foreground='#cbcbcb', font='Impact 20', command=tus_sil)
tus_sil.place(relx=0.747, rely=0.316, height=55, width=77.5, anchor=NW)

tus_bir_bolu_x = Button(size, activebackground='#494949', background='#131313', highlightbackground='white', text='1/x', foreground='#cbcbcb', font='Impact 20', command=tus_bir_bolu)
tus_bir_bolu_x.place(relx=0.012, rely=0.430, height=55, width=76.3, anchor=NW)

tus_x_kare = Button(size, activebackground='#494949', background='#131313', highlightbackground='white', text='x²', foreground='#cbcbcb', font='Impact 20', command=tus_kare)
tus_x_kare.place(relx=0.258, rely=0.430, height=55, width=76.3, anchor=NW)

tus_karekok = Button(size, activebackground='#494949', background='#131313', highlightbackground='white', text='√x', foreground='#cbcbcb', font='Impact 20', command=tus_karekok)
tus_karekok.place(relx=0.503, rely=0.430, height=55, width=76.3, anchor=NW)

tus_bol = Button(size, activebackground='#494949', background='#131313', highlightbackground='white', text='÷', foreground='#cbcbcb', font='Impact 20', command=tus_bol)
tus_bol.place(relx=0.747, rely=0.430, height=55, width=77.5, anchor=NW)

tus_7 = Button(size, activebackground='#494949', background='#060606', highlightbackground='white', text='7', foreground='#cbcbcb', font='Impact 20', command=tus_yedi)
tus_7.place(relx=0.012, rely=0.543, height=55, width=76.3, anchor=NW)

tus_8 = Button(size, activebackground='#494949', background='#060606', highlightbackground='white', text='8', foreground='#cbcbcb', font='Impact 20', command=tus_sekiz)
tus_8.place(relx=0.258, rely=0.543, height=55, width=76.3, anchor=NW)

tus_9 = Button(size, activebackground='#494949', background='#060606', highlightbackground='white', text='9', foreground='#cbcbcb', font='Impact 20', command=tus_dokuz)
tus_9.place(relx=0.503, rely=0.543, height=55, width=76.3, anchor=NW)

tus_carp = Button(size, activebackground='#494949', background='#131313', highlightbackground='white', text='×', foreground='#cbcbcb', font='Impact 20', command=tus_carp)
tus_carp.place(relx=0.747, rely=0.543, height=55, width=77.5, anchor=NW)

tus_4 = Button(size, activebackground='#494949', background='#060606', highlightbackground='white', text='4', foreground='#cbcbcb', font='Impact 20', command=tus_dort)
tus_4.place(relx=0.012, rely=0.658, height=55, width=76.3, anchor=NW)

tus_5 = Button(size, activebackground='#494949', background='#060606', highlightbackground='white', text='5', foreground='#cbcbcb', font='Impact 20', command=tus_bes)
tus_5.place(relx=0.258, rely=0.658, height=55, width=76.3, anchor=NW)

tus_6 = Button(size, activebackground='#494949', background='#060606', highlightbackground='white', text='6', foreground='#cbcbcb', font='Impact 20', command=tus_alti)
tus_6.place(relx=0.503, rely=0.658, height=55, width=76.3, anchor=NW)

tus_cikar = Button(size, activebackground='#494949', background='#131313', highlightbackground='white', text='-', foreground='#cbcbcb', font='Impact 20', command=tus_cikar)
tus_cikar.place(relx=0.747, rely=0.658, height=55, width=77.5, anchor=NW)

tus_1 = Button(size, activebackground='#494949', background='#060606', highlightbackground='white', text='1', foreground='#cbcbcb', font='Impact 20', command=tus_bir)
tus_1.place(relx=0.012, rely=0.770, height=55, width=76.3, anchor=NW)

tus_2 = Button(size, activebackground='#494949', background='#060606', highlightbackground='white', text='2', foreground='#cbcbcb', font='Impact 20', command=tus_iki)
tus_2.place(relx=0.258, rely=0.770, height=55, width=76.3, anchor=NW)

tus_3 = Button(size, activebackground='#494949', background='#060606', highlightbackground='white', text='3', foreground='#cbcbcb', font='Impact 20', command=tus_uc)
tus_3.place(relx=0.503, rely=0.770, height=55, width=76.3, anchor=NW)

tus_topla = Button(size, activebackground='#494949', background='#131313', highlightbackground='white', text='+', foreground='#cbcbcb', font='Impact 20', command=tus_arti)
tus_topla.place(relx=0.747, rely=0.770, height=55, width=77.5, anchor=NW)

tus_zit_isaret = Button(size, activebackground='#494949', background='#060606', highlightbackground='white', text='±', foreground='#cbcbcb', font='Impact 20', command=tus_zit)
tus_zit_isaret.place(relx=0.012, rely=0.885, height=55, width=76.3, anchor=NW)

tus_0 = Button(size, activebackground='#494949', background='#060606', highlightbackground='white', text='0', foreground='#cbcbcb', font='Impact 20', command=tus_sifir)
tus_0.place(relx=0.258, rely=0.885, height=55, width=76.3, anchor=NW)

tus_virgul = Button(size, activebackground='#494949', background='#060606', highlightbackground='white', text=',', foreground='#cbcbcb', font='Impact 20', command=tus_virgul)
tus_virgul.place(relx=0.503, rely=0.885, height=55, width=76.3, anchor=NW)

tus_esit = Button(size, activebackground='#9a0089', background='#501349', highlightbackground='white', text='=', foreground='#cbcbcb', font='Impact 20', command=tus_esit)
tus_esit.place(relx=0.747, rely=0.885, height=55, width=77.5, anchor=NW)

window.mainloop()
