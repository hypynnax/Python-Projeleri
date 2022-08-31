import requests
from bs4 import BeautifulSoup
from tkinter import *
import datetime


url_dolar = 'https://www.google.com/finance/quote/USD-TRY?sa=X&ved=2ahUKEwjp4ojX2fD5AhUhQ_EDHWKlDzcQmY0JegQIAhAb'
response_dolar = requests.get(url_dolar)
html_icerigi_dolar = response_dolar.content
soup_dolar = BeautifulSoup(html_icerigi_dolar, "html.parser")
dolar_fiyat = soup_dolar.find_all("div", {"class" : "YMlKec fxKbKc"})
dolar_kuru = dolar_fiyat[0].text

url_euro = 'https://www.google.com/finance/quote/EUR-TRY?sa=X&ved=2ahUKEwjO6IjZ2fD5AhWkQ_EDHSnDBXoQmY0JegQIAhAb'
response_euro = requests.get(url_euro)
html_icerigi_euro = response_euro.content
soup_euro = BeautifulSoup(html_icerigi_euro, "html.parser")
euro_fiyat = soup_euro.find_all("div", {"class" : "YMlKec fxKbKc"})
euro_kuru = euro_fiyat[0].text

def dolar_to_tl_hesaplama():
    dolar_tl.set(float(dolar_girdi.get()) * float(dolar_kuru))

def tl_to_dolar_hesaplama():
    dolar.set(float(dolar_tl_girdi.get()) / float(dolar_kuru))

def euro_to_tl_hesaplama():
    euro_tl.set(float(euro_girdi.get()) * float(euro_kuru))

def tl_to_euro_hesaplama():
    euro.set(float(euro_tl_girdi.get()) / float(euro_kuru))

windows = Tk(className=" Döviz Dönüşümü")
windows.resizable(False, False)
windows.iconbitmap(default='C:\\Users\\hypyn\\OneDrive\\Belgeler\\Python Projeleri\\ParaBirimiDonusturucu\\Currency Converter.ico')

size = Canvas(windows, height=500, width=1100, background='#7ABD8D', highlightbackground='#7ABD8D')
size.pack()

tarih = datetime.datetime.now()
gun = tarih.day
ay = tarih.strftime('%b')
saat = tarih.hour
dakka = tarih.minute

#Dolar ile ilgili herşey
frame_dolar = Frame(size, height=470, width=527, background='#202124')
frame_dolar.place(relx=0.02, rely=0.04)
dolar_baslik = Label(size, text="DOLAR KURU")
dolar_bilgilendirme = Label(frame_dolar, text="1 ABD Doları eşittir", background='#202124', foreground="#92989D", font='Fontspring 10')
dolar_kuru_bilgisi = Label(frame_dolar, text="{} Türk Lirası".format(dolar_kuru), background='#202124', foreground='white', font='Fontspring 20')
dolar_tarihi = Label(frame_dolar, text='{} {} {}:{} UTC'.format(gun, ay, saat, dakka), background='#202124', foreground="#92989D", font='Fontspring 10')
dolar_baslik.place(relx=0.1, rely=0.01)
dolar_bilgilendirme.place(relx=0.03, rely=0.1)
dolar_kuru_bilgisi.place(relx=0.03, rely=0.18)
dolar_tarihi.place(relx=0.03, rely=0.3)

dolar = DoubleVar(frame_dolar, value=1)
dolar.trace("w", lambda name, index, mode, d=dolar: dolar_to_tl_hesaplama())
dolar_girdi = Entry(frame_dolar, textvariable=dolar, width=22, bg='#202124', foreground='#FFFFFF', insertbackground='#48A1FF', font='Arial 30')
dolar_girdi.place(relx=0.05, rely=0.5)
dolar_bilgi = Label(frame_dolar, text="ABD Doları", font='Arial 15', background='#202124', foreground='#FFFFFF', highlightbackground='#48A1FF')
dolar_bilgi.place(relx=0.75, rely=0.52)

dolar_tl = DoubleVar(frame_dolar, value=1 * dolar_kuru)
dolar_tl.trace("w", lambda name, index, mode, tl=dolar_tl: tl_to_dolar_hesaplama())
dolar_tl_girdi = Entry(frame_dolar, textvariable=dolar_tl, width=22, bg='#202124', foreground='#FFFFFF', insertbackground='#48A1FF', font='Arial 30')
dolar_tl_girdi.place(relx=0.05, rely=0.7)
dolar_tl_bilgi = Label(frame_dolar, text="Türk Lirası", font='Arial 15', background='#202124', foreground='#FFFFFF', highlightbackground='#48A1FF')
dolar_tl_bilgi.place(relx=0.75, rely=0.72)


#Euro ile ilgili herşey
frame_euro = Frame(size, height=470, width=527, background='#202124')
frame_euro.place(relx=0.503, rely=0.04)
euro_baslik = Label(size, text="EURO KURU")
euro_bilgilendirme = Label(frame_euro, text="1 Euro eşittir", background='#202124', foreground="#92989D", font='Fontspring 10')
euro_kuru_bilgisi = Label(frame_euro, text="{} Türk Lirası".format(euro_kuru), background='#202124', foreground='white', font='Fontspring 20')
euro_tarihi = Label(frame_euro, text='{} {} {}:{} UTC'.format(gun, ay, saat, dakka), background='#202124', foreground="#92989D", font='Fontspring 10')
euro_baslik.place(relx=0.6, rely=0.01)
euro_bilgilendirme.place(relx=0.03, rely=0.1)
euro_kuru_bilgisi.place(relx=0.03, rely=0.18)
euro_tarihi.place(relx=0.03, rely=0.3)

euro = DoubleVar(frame_euro, value=1)
euro.trace("w", lambda name, index, mode, e=euro: euro_to_tl_hesaplama())
euro_girdi = Entry(frame_euro, textvariable=euro, width=22, bg='#202124', foreground='#FFFFFF', insertbackground='#48A1FF', font='Arial 30')
euro_girdi.place(relx=0.05, rely=0.5)
euro_bilgi = Label(frame_euro, text="Euro", font='Arial 15', background='#202124', foreground='#FFFFFF', highlightbackground='#48A1FF')
euro_bilgi.place(relx=0.75, rely=0.52)

euro_tl = DoubleVar(frame_euro, value=1 * euro_kuru)
euro_tl.trace("w", lambda name, index, mode, tl=euro_tl: tl_to_euro_hesaplama())
euro_tl_girdi = Entry(frame_euro, textvariable=euro_tl, width=22, bg='#202124', foreground='#FFFFFF', insertbackground='#48A1FF', font='Arial 30')
euro_tl_girdi.place(relx=0.05, rely=0.7)
euro_tl_bilgi = Label(frame_euro, text="Türk Lirası", font='Arial 15', background='#202124', foreground='#FFFFFF', highlightbackground='#48A1FF')
euro_tl_bilgi.place(relx=0.75, rely=0.72)


windows.mainloop()
