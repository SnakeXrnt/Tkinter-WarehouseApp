import tkinter as tk
from tkinter import messagebox
from time import *
import os
import sys
from json import *
import csv


class MasukBarang(tk.Frame):

    def __init__(self, parent, App):
        self.settings = App.settings
        self.app = App
        super().__init__(parent)
        self.configure(bg="white")
        self.pack(fill="both", expand=True)

        self.pixelButton = tk.PhotoImage(width=1, height=1)
        self.mainframe()
        self.FrameUp()
        self.LowerFr_left()
        self.LowerFr_right()


    def mainframe(self):
    	self.MskBrng = tk.Frame(self,bg='purple',width=self.settings.width,height = self.settings.height)
    	self.MskBrng.grid(row=0,column=0,sticky='nsew')
    	self.MskBrng.pack_propagate(False)



    def FrameUp(self):
        FrameUp = tk.Frame(self.MskBrng, bg='gray',width=self.settings.width,height=(self.settings.height//5))
        FrameUp.pack(fill='both')
        tk.Label(FrameUp , text ='APLIKASI PERGUDANGAN \n  by: Ethan Bast , Kenzie',font=('arial',20),bg='gray',fg='white').pack(side='right')
        tk.Button(FrameUp , text=' <- Back to main menu ' , command = self.app.MskBrng_back_to_main).pack(side='left')

    def LowerFr_left(self):
        lowfr = tk.Frame(self.MskBrng, bg='black',width = (self.settings.width//2),height=(self.settings.height))
        lowfr.pack(side='left')
        lowfr.pack_propagate(False)
        tk.Label(lowfr, text='DETAIL BARANG \t \t',bg='black',fg='white',font=('arial',15),justify='left').pack(fill='x')
        tk.Label(lowfr, text='Kode Barang \t \t:',bg='black',fg='white',font=('arial',15),justify='left').pack(fill='x')
        tk.Label(lowfr, text='Nama Barang \t \t:',bg='black',fg='white',font=('arial',15),justify='left').pack(fill='x')
        tk.Label(lowfr, text='Jumlah Barang \t \t:',bg='black',fg='white',font=('arial',15),justify='left').pack(fill='x')
        tk.Label(lowfr, text='\n \t \t',bg='black',fg='white',font=('arial',15),justify='left').pack(fill='x')
        tk.Label(lowfr, text='Tanggal  \t \t \t',bg='black',fg='white',font=('arial',15),justify='left').pack(fill='x')
        tk.Label(lowfr, text='Tempat Masuk \t \t:',bg='black',fg='white',font=('arial',15),justify='left').pack(fill='x')

    def LowerFr_right(self):
        lowfrR = tk.Frame(self.MskBrng, bg='Gray',width = (self.settings.width//2),height=(self.settings.height))
        lowfrR.pack(side='right')
        lowfrR.pack_propagate(False)
        tk.Label(lowfrR, text='Buat User Baru \t \t:',bg='Gray',fg='Gray',font=('arial',15),justify='left').pack(fill='x')
        #ALL ENTRY
        self.kodebarang = tk.StringVar()
        self.namabarang = tk.StringVar()
        self.jumlahbarang = tk.StringVar()
        self.tempatmasuk = tk.StringVar()

        self.KodeBarang = tk.Entry(lowfrR,width=(self.settings.width//2),bd=4,textvariable=self.kodebarang)
        self.KodeBarang.pack()
        self.NamaBarang = tk.Entry(lowfrR,width=(self.settings.width//2),bd=4,textvariable=self.namabarang)
        self.NamaBarang.pack()
        self.JumlahBarang = tk.Entry(lowfrR,width=(self.settings.width//2),bd=4,textvariable=self.jumlahbarang)
        self.JumlahBarang.pack()
        tk.Label(lowfrR, text='Buat User Baru \n \t \t:',bg='Gray',fg='Gray',font=('arial',15),justify='left').pack(fill='x')
        tk.Label(lowfrR, text='Buat User Baru \n \t \t:',bg='Gray',fg='Gray',font=('arial',5),justify='left').pack(fill='x')
        self.TempatMasuk = tk.Entry(lowfrR,width=(self.settings.width//2),bd=4,textvariable=self.tempatmasuk)
        self.TempatMasuk.pack()
        tk.Button(lowfrR,text='Masukan Barang',width=(self.settings.width//2),command=self.masukanbarang).pack()

    def masukanbarang(self):
        kode = self.kodebarang.get()
        nama = self.namabarang.get()
        jumlah = self.jumlahbarang.get()
        tanggal = str(strftime('%H:%M:%S   %b %d %Y'))
        tempat = self.tempatmasuk.get()

        sementara = {

        }

        barangR = open('barang.json','r+')
        sementara = load(barangR)



        if kode in sementara.keys():
            jumlahlama = sementara[kode]['jumlah']
            jumlahBARUSTR =  int(jumlahlama) + int(jumlah)
            jumlahBARU = str(jumlahBARUSTR)

        else :
            jumlahBARU = jumlah


        sementara[kode]={
            'nama' : nama,
            'jumlah' : jumlahBARU,
            'tanggal' : tanggal,
            'tempat' : tempat
        }

        with open('barang.json','w') as barangW:
            dump(sementara,barangW)
        print(sementara)

        with open('log.txt','a') as log:
            sendtolog = ('['+ tanggal +']' + ' ' + 'Barang Masuk' + ' : '+ '{'+ kode+ '}' + ' ' + '{'+ nama +'}'+ ' ' + '{'+ jumlah+ '}' + ' ' + '{'+ tempat+ '}' + '\n')
            log.write(sendtolog)

        self.KodeBarang.delete(0,'end')
        self.NamaBarang.delete(0,'end')
        self.JumlahBarang.delete(0,'end')
        self.TempatMasuk.delete(0,'end')


        print('berhasil mencetak barang')


class KeluarBarang(tk.Frame):

    def __init__(self, parent, App):
        self.settings = App.settings
        self.app = App

        super().__init__(parent)
        self.configure(bg="white")
        self.pack(fill="both", expand=True)

        self.pixelButton = tk.PhotoImage(width=1, height=1)
        self.mainframe()
        self.FrameUp()
        self.LowerFr_left()
        self.LowerFr_right()


    def mainframe(self):
    	self.KluarBrng = tk.Frame(self,bg='purple',width=self.settings.width,height = self.settings.height)
    	self.KluarBrng.grid(row=0,column=0,sticky='nsew')
    	self.KluarBrng.pack_propagate(False)

    def FrameUp(self):
        FrameUp = tk.Frame(self.KluarBrng, bg='gray',width=self.settings.width,height=(self.settings.height//5))
        FrameUp.pack(fill='both')
        tk.Label(FrameUp , text ='APLIKASI PERGUDANGAN \n  by: Ethan Bast , Kenzie',font=('arial',20),bg='gray',fg='white').pack(side='right')
        tk.Button(FrameUp , text=' <- Back to main menu ', command = self.app.KeluarBrng_back_to_main).pack(side='left')

    def LowerFr_left(self):
        lowfr = tk.Frame(self.KluarBrng, bg='black',width = (self.settings.width//2),height=(self.settings.height))
        lowfr.pack(side='left')
        lowfr.pack_propagate(False)
        tk.Label(lowfr, text='DETAIL BARANG \t \t',bg='black',fg='white',font=('arial',15),justify='left').pack(fill='x')
        tk.Label(lowfr, text='Kode Barang \t \t:',bg='black',fg='white',font=('arial',15),justify='left').pack(fill='x')
        tk.Label(lowfr, text='Nama Barang \t \t:',bg='black',fg='white',font=('arial',15),justify='left').pack(fill='x')
        tk.Label(lowfr, text='Jumlah Barang \t \t:',bg='black',fg='white',font=('arial',15),justify='left').pack(fill='x')
        tk.Label(lowfr, text='\n \t \t',bg='black',fg='white',font=('arial',15),justify='left').pack(fill='x')
        tk.Label(lowfr, text='Tanggal  \t \t \t',bg='black',fg='white',font=('arial',15),justify='left').pack(fill='x')
        tk.Label(lowfr, text='Tempat Keluar \t \t:',bg='black',fg='white',font=('arial',15),justify='left').pack(fill='x')

    def LowerFr_right(self):
        lowfrR = tk.Frame(self.KluarBrng, bg='Gray',width = (self.settings.width//2),height=(self.settings.height))
        lowfrR.pack(side='right')
        lowfrR.pack_propagate(False)
        tk.Label(lowfrR, text='Buat User Baru \t \t:',bg='Gray',fg='Gray',font=('arial',15),justify='left').pack(fill='x')
        self.kodebarang = tk.StringVar()
        self.namabarang = tk.StringVar()
        self.jumlahbarang = tk.StringVar()
        self.tempatmasuk = tk.StringVar()

        self.KodeBarang = tk.Entry(lowfrR,width=(self.settings.width//2),bd=4,textvariable=self.kodebarang)
        self.KodeBarang.pack()
        self.NamaBarang = tk.Entry(lowfrR,width=(self.settings.width//2),bd=4,textvariable=self.namabarang)
        self.NamaBarang.pack()
        self.JumlahBarang = tk.Entry(lowfrR,width=(self.settings.width//2),bd=4,textvariable=self.jumlahbarang)
        self.JumlahBarang.pack()
        tk.Label(lowfrR, text='Buat User Baru \n g \t \t:',bg='Gray',fg='Gray',font=('arial',20),justify='left').pack(fill='x')
        tk.Label(lowfrR, text='Buat User Baru \n \n \t \t:',bg='Gray',fg='Gray',font=('arial',5),justify='left').pack(fill='x')
        self.TempatMasuk = tk.Entry(lowfrR,width=(self.settings.width//2),bd=4,textvariable=self.tempatmasuk)
        self.TempatMasuk.pack()
        tk.Button(lowfrR,text='Keluar Barang',width=(self.settings.width//2),command=self.keluarbarang).pack()

    def keluarbarang(self):
        kode = self.kodebarang.get()
        jumlah = self.jumlahbarang.get()
        tanggal = str(strftime('%H:%M:%S , %b %d %Y'))
        tempat = self.tempatmasuk.get()

        sementara = {

        }

        barangR = open('barang.json','r+')
        sementara = load(barangR)



        if kode in sementara.keys():
            jumlahlama = sementara[kode]['jumlah']
            jumlahBARUSTR =  int(jumlahlama) - int(jumlah)
            jumlahBARU = str(jumlahBARUSTR)

        else :
            jumlahBARU = jumlah


        sementara[kode]['jumlah'] = jumlahBARU

        with open('barang.json','w') as barangW:
            dump(sementara,barangW)
        print(sementara)

        nama = sementara[kode]['nama']
        with open('log.txt','a') as log:
            sendtolog = ('['+ tanggal +']' + ' ' + 'Barang Keluar' + ' : '+ '{'+ kode+ '}' + ' ' + '{'+ nama +'}'+ ' ' + '{'+ jumlah+ '}' + ' ' + '{'+ tempat+ '}' + '\n')
            log.write(sendtolog)

        self.KodeBarang.delete(0,'end')
        self.NamaBarang.delete(0,'end')
        self.JumlahBarang.delete(0,'end')
        self.TempatMasuk.delete(0,'end')


        print('berhasil mencetak barang')


class UbhNamaBarang(tk.Frame):

    def __init__(self, parent, App):
        self.settings = App.settings
        self.app = App

        super().__init__(parent)
        self.configure(bg="white")
        self.pack(fill="both", expand=True)

        self.pixelButton = tk.PhotoImage(width=1, height=1)
        self.mainframe()
        self.FrameUp()
        self.LowerFr_left()
        self.LowerFr_right()


    def mainframe(self):
    	self.UbhNamaBrng = tk.Frame(self,bg='purple',width=self.settings.width,height = self.settings.height)
    	self.UbhNamaBrng.grid(row=0,column=0,sticky='nsew')
    	self.UbhNamaBrng.pack_propagate(False)

    def FrameUp(self):
        FrameUp = tk.Frame(self.UbhNamaBrng, bg='gray',width=self.settings.width,height=(self.settings.height//5))
        FrameUp.pack(fill='both')
        tk.Label(FrameUp , text ='APLIKASI PERGUDANGAN \n  by: Ethan Bast , Kenzie',font=('arial',20),bg='gray',fg='white').pack(side='right')
        tk.Button(FrameUp , text=' <- Back to main menu ', command = self.app.UbhNamaBrng_back_to_main).pack(side='left')

    def LowerFr_left(self):
        lowfr = tk.Frame(self.UbhNamaBrng, bg='black',width = (self.settings.width//2),height=(self.settings.height))
        lowfr.pack(side='left')
        lowfr.pack_propagate(False)
        tk.Label(lowfr, text='DETAIL BARANG \t \t',bg='black',fg='white',font=('arial',15),justify='left').pack(fill='x')
        tk.Label(lowfr, text='Kode Barang \t \t:',bg='black',fg='white',font=('arial',15),justify='left').pack(fill='x')
        tk.Label(lowfr, text='\n \n ',bg='black',fg='white',font=('arial',15),justify='left').pack(fill='x')
        tk.Label(lowfr, text='Buat User Baru \t \t:',bg='black',fg='black',font=('arial',3),justify='left').pack(fill='x')
        tk.Label(lowfr, text='Nama Barang \t \t:',bg='black',fg='white',font=('arial',15),justify='left').pack(fill='x')
        tk.Label(lowfr, text='Jumlah Barang \t \t:',bg='black',fg='white',font=('arial',15),justify='left').pack(fill='x')

    def LowerFr_right(self):
        lowfrR = tk.Frame(self.UbhNamaBrng, bg='Gray',width = (self.settings.width//2),height=(self.settings.height))
        lowfrR.pack(side='right')
        lowfrR.pack_propagate(False)
        tk.Label(lowfrR, text='Buat User Baru \t \t:',bg='Gray',fg='Gray',font=('arial',15),justify='left').pack(fill='x')
        KodeBarang = tk.Entry(lowfrR,width=(self.settings.width//2),bd=4)
        KodeBarang.pack()

        tk.Button(lowfrR,text='Cari Barang',width=(self.settings.width//2)).pack()
        tk.Label(lowfrR, text='Buat User Baru \t \t:',bg='Gray',fg='Gray',font=('arial',15),justify='left').pack(fill='x')
        tk.Label(lowfrR, text='Buat User Baru \t \t:',bg='Gray',fg='Gray',font=('arial',15),justify='left').pack(fill='x')
        NamaBarang = tk.Entry(lowfrR,width=(self.settings.width//2),bd=4)
        NamaBarang.pack()
        JumlahBarang = tk.Entry(lowfrR,width=(self.settings.width//2),bd=4)
        JumlahBarang.pack()
        tk.Button(lowfrR,text='Simpan Barang',width=(self.settings.width//2)).pack()


class BuatLporBarang(tk.Frame):

    def __init__(self, parent, App):
        self.settings = App.settings
        self.app = App

        super().__init__(parent)
        self.configure(bg="white")
        self.pack(fill="both", expand=True)

        self.pixelButton = tk.PhotoImage(width=1, height=1)
        self.mainframe()
        self.FrameUp()
        self.FrameLeft()



    def mainframe(self):
    	self.BuatLporBrng = tk.Frame(self,bg='purple',width=self.settings.width,height = self.settings.height)
    	self.BuatLporBrng.grid(row=0,column=0,sticky='nsew')
    	self.BuatLporBrng.pack_propagate(False)

    def FrameUp(self):
        FrameUp = tk.Frame(self.BuatLporBrng, bg='gray',width=self.settings.width,height=(self.settings.height//5))
        FrameUp.pack(fill='both')
        tk.Label(FrameUp , text ='APLIKASI PERGUDANGAN \n  by: Ethan Bast , Kenzie',font=('arial',20),bg='gray',fg='white').pack(side='right')
        tk.Button(FrameUp , text=' <- Back to main menu ', command = self.app.BuatLporBrng_back_to_main).pack(side='left')

    def FrameLeft(self):
        FrameDown = tk.Frame(self.BuatLporBrng, bg='black',width=self.settings.width ,height=self.settings.height)
        FrameDown.pack(side='left')
        FrameDown.pack_propagate(False)
        tk.Button(FrameDown , text='Export data to CSV', command = self.tocsv).pack()

        self.textbox_scroll = tk.Scrollbar(FrameDown)
        self.textbox_scroll.pack(side="right", fill="y")

        textbox = tk.Text(FrameDown,bg='black',fg='gray',font=('Arial',13), yscrollcommand=self.textbox_scroll.set)
        textbox.pack(fill='both',expand=True)
        barang = open('barang.json','r+')
        dictbar = load(barang)
        keylist = list(dictbar.keys())
        keysavia = len(keylist)
        print(keysavia)
        counter = 0
        print(keylist)
        for x in range(len(keylist)):
            keyonebyone = keylist[x]
            nama = dictbar[keyonebyone]['nama']
            jumlah = dictbar[keyonebyone]['jumlah']
            tanggal = dictbar[keyonebyone]['tanggal']
            tempat = dictbar[keyonebyone]['tempat']
            all = "nama : " + nama + " jumlah : " + jumlah + " tanggal : " + tanggal + " tempat : " + tempat + "\n"
            textbox.insert(tk.END,all)

        self.textbox_scroll.config(command=textbox.yview)

    def tocsv(self):
        barang = open('barang.json','r+')
        dictbar = load(barang)
        keylist = list(dictbar.keys())
        keysavia = len(keylist)
        print(keysavia)
        counter = 0
        print(keylist)
        header = ['nama','jumlah','tanggal','tempat']
        file = open('barang.csv', 'w', newline ='')
        writer = csv.DictWriter(file, fieldnames = header)
        writer.writeheader()
        for x in range(len(keylist)):
            keyonebyone = keylist[x]
            nama = dictbar[keyonebyone]['nama']
            jumlah = dictbar[keyonebyone]['jumlah']
            tanggal = dictbar[keyonebyone]['tanggal']
            tempat = dictbar[keyonebyone]['tempat']
            writer.writerow({
            'nama':nama,
            'jumlah':jumlah,
            'tanggal':tanggal,
            'tempat':tempat
            })


class LiatLogBarang(tk.Frame):

    def __init__(self, parent, App):
        self.settings = App.settings
        self.app = App

        super().__init__(parent)
        self.configure(bg="white")
        self.pack(fill="both", expand=True)

        self.pixelButton = tk.PhotoImage(width=1, height=1)
        self.mainframe()
        self.FrameUp()
        self.FrameDown()


    def mainframe(self):
        self.LiatLogBrng = tk.Frame(self,bg='purple',width=self.settings.width,height = self.settings.height)
        self.LiatLogBrng.grid(row=0,column=0,sticky='nsew')
        self.LiatLogBrng.pack_propagate(False)


    def FrameUp(self):
        FrameUp = tk.Frame(self.LiatLogBrng, bg='gray',width=self.settings.width,height=(self.settings.height//5))
        FrameUp.pack(fill='both')
        tk.Label(FrameUp , text ='APLIKASI PERGUDANGAN \n  by: Ethan Bast , Kenzie',font=('arial',20),bg='gray',fg='white').pack(side='right')
        tk.Button(FrameUp , text=' <- Back to main menu ', command = self.app.LiatLogBrng_back_to_main).pack(side='left')

    def FrameDown(self):
        logpull = open('log.txt','r')
        inslog = logpull.read()

        self.textbox_scroll = tk.Scrollbar(self.LiatLogBrng)
        self.textbox_scroll.pack(side="right", fill="y")

        self.textbox = tk.Text(self.LiatLogBrng,bg='black',fg='gray',font=('Arial',13), yscrollcommand=self.textbox_scroll.set)
        self.textbox.pack(fill='both',expand=True)
        self.textbox.insert(tk.END,inslog)

        self.textbox_scroll.config(command=self.textbox.yview)



class SettingsBarang(tk.Frame):

    def __init__(self, parent, App):
        self.settings = App.settings
        self.app = App

        super().__init__(parent)
        self.configure(bg="white")
        self.pack(fill="both", expand=True)

        self.pixelButton = tk.PhotoImage(width=1, height=1)
        self.mainframe()
        self.FrameUp()
        self.LowerFr_left()
        self.LowerFr_right()


    def mainframe(self):
    	self.SettingsBrng = tk.Frame(self,bg='purple',width=self.settings.width,height = self.settings.height)
    	self.SettingsBrng.grid(row=0,column=0,sticky='nsew')
    	self.SettingsBrng.pack_propagate(False)

    def FrameUp(self):
        FrameUp = tk.Frame(self.SettingsBrng, bg='gray',width=self.settings.width,height=(self.settings.height//5))
        FrameUp.pack(fill='both')
        tk.Label(FrameUp , text ='APLIKASI PERGUDANGAN \n  by: Ethan Bast , Kenzie',font=('arial',20),bg='Gray',fg='white').pack(side='right')
        tk.Button(FrameUp , text=' <- Back to main menu ', command = self.app.SettingsBrng_back_to_main).pack(side='left')

    def LowerFr_left(self):
    	lowfr = tk.Frame(self.SettingsBrng, bg='black',width = (self.settings.width//2),height=(self.settings.height))
    	lowfr.pack(side='left')
    	lowfr.pack_propagate(False)
    	tk.Label(lowfr, text='AKUN Gmail \t \t',bg='black',fg='white',font=('arial',15),justify='left').pack(fill='x')
    	tk.Label(lowfr, text='Email Gudang \t \t:',bg='black',fg='white',font=('arial',15),justify='left').pack(fill='x')
    	tk.Label(lowfr, text='Password \t \t:',bg='black',fg='white',font=('arial',15),justify='left').pack(fill='x')
    	tk.Label(lowfr, text='\n \t \t',bg='black',fg='white',font=('arial',20),justify='left').pack(fill='x')
    	tk.Label(lowfr, text='MEMBUAT USER BARU \t',bg='black',fg='white',font=('arial',15),justify='left').pack(fill='x')
    	tk.Label(lowfr, text='Username Baru \t \t:',bg='black',fg='white',font=('arial',15),justify='left').pack(fill='x')
    	tk.Label(lowfr, text='Password User \t \t:',bg='black',fg='white',font=('arial',15),justify='left').pack(fill='x')
    	tk.Label(lowfr, text='Konfirmasi Password \t:',bg='black',fg='white',font=('arial',15),justify='left').pack(fill='x')
    	tk.Label(lowfr, text='Buat User Baru \t \t:',bg='black',fg='white',font=('arial',15),justify='left').pack(fill='x')
    	tk.Label(lowfr, text='\n \t \t',bg='black',fg='white',font=('arial',15),justify='left').pack(fill='x')

    def LowerFr_right(self):
        lowfrR = tk.Frame(self.SettingsBrng, bg='Gray',width = (self.settings.width//2),height=(self.settings.height))
        lowfrR.pack(side='right')
        lowfrR.pack_propagate(False)
        tk.Label(lowfrR, text='Buat User Baru \t \t:',bg='Gray',fg='Gray',font=('arial',15),justify='left').pack(fill='x')
        EmailGmail = tk.Entry(lowfrR,width=(self.settings.width//2),bd=4)
        EmailGmail.pack()
        PassGmail = tk.Entry(lowfrR,show='*',width=(self.settings.width//2),bd=4)
        PassGmail.pack()
        tk.Button(lowfrR,text='Simpan email dan password',width=(self.settings.width//2)).pack()
        tk.Label(lowfrR, text='Buat User Baru \n \t \t:',bg='Gray',fg='Gray',font=('arial',14),justify='left').pack(fill='x')
        tk.Label(lowfrR, text='Buat User Baru \n \t \t:',bg='Gray',fg='Gray',font=('arial',10),justify='left').pack(fill='x')
        UserLog = tk.Entry(lowfrR,width=(self.settings.width//2),bd=4)
        UserLog.pack()
        PassLog = tk.Entry(lowfrR,show="*",width=(self.settings.width//2),bd=4)
        PassLog.pack()
        ConPassLog = tk.Entry(lowfrR,width=(self.settings.width//2),bd=4)
        ConPassLog.pack()
        tk.Button(lowfrR,text='Make New User',width=(self.settings.width//2)).pack()