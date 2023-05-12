from tkinter import *
from tkinter import ttk
from json import load
from settings import Settings
 
# judul dan isi tabel
judul_kolom = ("NAMA LENGKAP", "KOTA ASAL", "JURUSAN")
stock_list = self.settings.load_data(self.settings.data_json_path)
barang = open('barang.json', 'r+')
data_mhs = load(barang)

data_mhs = {
    [kode]
}
print(data_mhs.get("nama"))
 
 
class DemoTabelMHS:
    def __init__(self, induk, judul):
        self.induk = induk
         
        self.induk.title(judul)
        self.induk.protocol("WM_DELETE_WINDOW", self.Tutup)
        self.induk.resizable(False, False)
         
        self.aturKomponen()
        self.isiTabel()
         
    def aturKomponen(self):
        # buat frame utama
        mainFrame = Frame(self.induk)
        mainFrame.pack(fill=BOTH, expand=YES)
         
        # buat frame untuk tabel beserta scrollbar-nya
        fr_data = Frame(mainFrame, bd=10)
        fr_data.pack(fill=BOTH, expand=YES)
         
        # buat tabel dengan Treeview
        self.trvTabel = ttk.Treeview(fr_data, columns=judul_kolom, 
                show='headings')
         
        # buat scrollbar
        sbVer = Scrollbar(fr_data, orient='vertical', 
                command=self.trvTabel.yview)
        sbHor = Scrollbar(fr_data, orient='horizontal', 
                command=self.trvTabel.xview)
        # pasang dengan layout manager pack()       
        sbVer.pack(side=RIGHT, fill=Y)
        sbHor.pack(side=BOTTOM, fill=X)
        self.trvTabel.pack(side=LEFT, fill=BOTH)
             
        # buat statusbar
        lblStatus = Label(mainFrame, 
                text='www.KlinikPython.wordpress.com', bd=1, relief=SUNKEN)
        lblStatus.pack(side=BOTTOM, fill=X)
         
    def isiTabel(self):
        # isi judul tabel
        for kolom in judul_kolom:
            self.trvTabel.heading(kolom, text=kolom)
                     
        # isi data tabel
        for dat in data_mhs:
            self.trvTabel.insert('', 'end', values=dat)
         
    def Tutup(self, event=None):
        self.induk.destroy()
         
if __name__ == '__main__':
    root = Tk()
     
    app = DemoTabelMHS(root, ":: Demo Tabel Mahasiswa ::")
     
    root.mainloop()