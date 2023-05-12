import tkinter as tk
from tkinter import messagebox
from time import *
import os
import sys


class Page01(tk.Frame):

    def __init__(self, parent, App):
        self.settings = App.settings
        self.app = App

        super().__init__(parent,)
        self.configure(bg="white")
        self.pack(fill='both',expand=True)
        parent.grid_rowconfigure(0, weight=1)
        parent.grid_columnconfigure(0, weight=1)

        self.pixelButton = tk.PhotoImage(width=1, height=1)

        self.FrameUp()
        self.leftFrame()
        self.rightFrame()

    def FrameUp(self):
        FrameUp = tk.Frame(self, bg='gray',width=self.settings.width,height=(self.settings.height//5))
        FrameUp.pack(fill='both')
        tk.Label(FrameUp , text ='APLIKASI PERGUDANGAN \n by: Ethan Bast , Kenzie',font=('arial',20),bg='gray',fg='white').pack()


    def leftFrame(self):
        left = tk.Frame(self, bg="black", width=(self.settings.width//2),height=(self.settings.height*4//5))
        left.pack(side="left", fill="both")



        jam = tk.Label(left,text='0',font=('Arial',30),width=19,height=3,bg='black',fg='white')
        jam.pack()
        def digitalclock():
            text_input = strftime("      %H:%M:%S\n%a, %b %d %Y      ")
            #now = strftime("%s")
            jam.config(text=text_input)
            jam.after(200, digitalclock)
        digitalclock()



        def BarangMasuk(self):
            FrameMsk = tk.Frame(self,bg='grey')
            FrameMsk.pack(fill='both',expand=True)

        buttonMsk = tk.Button(left,text='Carat Barang \n Masuk',image=self.pixelButton, compound="c",height=120, width=400,font=('Arial',20),bg='gray',fg='white',command=self.app.create_masukbarang)
        buttonMsk.pack()
        buttonUbh = tk.Button(left,text='Feedback',image=self.pixelButton, compound="c",height=120, width=400,font=('Arial',20),bg='black',fg='white',command=self.app.create_UbhNamabarang)
        buttonUbh.pack()
        buttonLog = tk.Button(left,text='Lihat Log',image=self.pixelButton, compound="c",height=120, width=400,font=('Arial',20),bg='Gray',fg='white',command=self.app.create_LiatLogbarang)
        buttonLog.pack()


    def rightFrame(self):
        right = tk.Frame(self, bg="black", width=(self.settings.width//2),height=(self.settings.height*4//5))
        right.pack(side="right", fill="both")

        info = tk.Frame(right, bg="blue",height=142, width=400)
        info.pack()
        info.pack_propagate(False)

        self.online = tk.Label(info,text='System \n Online',width=13, height = 20,font=('arial',20),bg ='green' , fg = 'white')
        self.online.pack(side='left')

        infoButton = tk.Frame(info, bg="purple",height=142, width=200)
        infoButton.pack(side='right')
        infoButton.pack_propagate(False)

        def restart():
            sleep(1)
            self.online.config(text='System \n Offline',bg='Red')
            question = messagebox.askquestion("confirm", "Are you sure you want to Restart?")
            if question == 'yes':
                python = sys.executable
                os.execl(python, python, * sys.argv)
                window.destroy()
            else :
                tk.messagebox.showinfo('Return','You will now return to the application screen')
                sleep(1)
                self.online.config(text='System \n Online',bg='Green')



        buttonRestart = tk.Button(infoButton, text='Restart',bg='orange',fg='white',font=('arial',20),command = restart)
        buttonRestart.pack(side='top' , expand=True , fill='both')

        def logout():
            sleep(1)
            self.online.config(text='System \n Offline',bg='Red')
            question = messagebox.askquestion("confirm", "Are you sure you want to Quit?")
            if question == 'yes':
                quit()
            else :
                tk.messagebox.showinfo('Return','You will now return to the application screen')
                sleep(1)
                self.online.config(text='System \n Online',bg='Green')

        buttonQuit = tk.Button(infoButton,text='QUIT' ,font=('Arial',20),bg='red',fg='white',command = logout)
        buttonQuit.pack(side = 'top' , expand=True , fill='both')


        self.buttonKluar = tk.Button(right,text='Keluar / Edit Barang',image=self.pixelButton, compound="c",height=120, width=400,font=('Arial',20),bg='gray',fg='white',command=self.app.create_keluarbarang).pack()
        self.buttonReport = tk.Button(right,text='Buat Laporan Stok',image=self.pixelButton, compound="c",height=120, width=400,font=('Arial',20),bg='black',fg='white',command=self.app.create_BuatLporbarang).pack()
        self.buttonSettings = tk.Button(right,text='Settings',image=self.pixelButton, compound="c",height=120, width=400,font=('Arial',20),bg='gray',fg='white',command=self.app.create_Settingsbarang).pack()
