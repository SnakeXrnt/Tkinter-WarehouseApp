import tkinter as tk
from page import Page01
from function  import *
from time import *
from page02 import Page02


from settings import Settings
class MainWindow(tk.Tk):

	def __init__(self, App):
		self.settings = App.settings



		super().__init__()
		self.title(self.settings.app_title)
		self.geometry(self.settings.screen)
		self.pages = {}
		self.create_container()
		self.resizable(False, False)
		self.protocol("WM_DELETE_WINDOW", self.logout)

		self.create_page01()
		self.create_page02()

	def logout(self):
		sleep(1)
		question = messagebox.askquestion("confirm", "Are you sure you want to Quit?")
		if question == 'yes':
			quit()
		else :
			tk.messagebox.showinfo('Return','You will now return to the application screen')
			sleep(1)


	def create_container(self):
		self.container = tk.Frame(bg="grey")
		self.container.pack(side="top", fill="both", expand=True)

	def create_page01(self):
		self.pages['page01'] = Page01(self.container, self)
		print('page01 created')

	def create_masukbarang(self):
		self.pages['MasukBarang'] = MasukBarang(self.container, self)
		print('page masuk barang created')
		self.pages['page01'].destroy()

	def create_keluarbarang(self):
		self.pages['KeluarBarang'] = KeluarBarang(self.container, self)
		print('page keluar barang created')
		self.pages['page01'].destroy()

	def create_UbhNamabarang(self):
		self.pages['UbhNamaBarang'] = UbhNamaBarang(self.container, self)
		print('page UbhNama barang created')
		self.pages['page01'].destroy()

	def create_BuatLporbarang(self):
		self.pages['BuatLporBarang'] = BuatLporBarang(self.container, self)
		print('page BuatLpor barang created')
		self.pages['page01'].destroy()

	def create_LiatLogbarang(self):
		self.pages['LiatLogBarang'] = LiatLogBarang(self.container, self)
		print('page LiatLog barang created')
		self.pages['page01'].destroy()

	def create_Settingsbarang(self):
		self.pages['SettingsBarang'] = SettingsBarang(self.container, self)
		print('page Settings barang created')
		self.pages['page01'].destroy()



	def MskBrng_back_to_main(self):
		self.pages['MasukBarang'].destroy()
		print('sucsessfully go to main menu')
		self.pages['page01'] = Page01(self.container, self)

	def KeluarBrng_back_to_main(self):
		self.pages['KeluarBarang'].destroy()
		print('sucsessfully go to main menu')
		self.pages['page01'] = Page01(self.container, self)

	def Feedback_back_to_main(self):
		self.pages['UbhNamaBarang'].destroy()
		print('sucsessfully go to main menu')
		self.pages['page01'] = Page01(self.container, self)

	def BuatLporBrng_back_to_main(self):
		self.pages['BuatLporBarang'].destroy()
		print('sucsessfully go to main menu')
		self.pages['page01'] = Page01(self.container, self)

	def LiatLogBrng_back_to_main(self):
		self.pages['LiatLogBarang'].destroy()
		print('sucsessfully go to main menu')
		self.pages['page01'] = Page01(self.container, self)

	def SettingsBrng_back_to_main(self):
		self.pages['SettingsBarang'].destroy()
		print('sucsessfully go to main menu')
		self.pages['page01'] = Page01(self.container,self)

	def create_page02(self):
		self.pages['page01'].destroy()
		self.pages['page02'] = Page02(self.container, self)

	def change_to_page01(self):
		usernameVar = self.pages['page02'].nameVar.get()
		passwordVar = self.pages['page02'].passwordVar.get()
		babi = open('login.json','r+')
		dictbar = {}
		dictbar = load(babi)
		keylist = list(dictbar.keys())

		counter = 0
		if usernameVar in keylist:
			passwordavia = dictbar[usernameVar]["pass "]
			if passwordVar == passwordavia :

				self.pages['page01'] = Page01(self.container,self)
				self.pages['page02'].destroy()
				tanggal = str(strftime('%H:%M:%S   %b %d %Y'))

				with open('log.txt','a') as log:
					sendtolog = ('['+ tanggal +']' + ' ' + 'login' + ' : '+  '['  + usernameVar + ']'+ '\n')
					log.write(sendtolog)
			else :
				tk.messagebox.showerror('System','Password false')
				tanggal = str(strftime('%H:%M:%S   %b %d %Y'))

				with open('log.txt','a') as log:
					sendtolog = ('['+ tanggal +']' + ' ' + 'login' + ' : '+  'login gagal, Password not found'+ '\n')
					log.write(sendtolog)
		else :
			tk.messagebox.showerror('System','Username not found')
			tanggal = str(strftime('%H:%M:%S   %b %d %Y'))

			with open('log.txt','a') as log:
				sendtolog = ('['+ tanggal +']' + ' ' + 'login' + ' : '+  'login gagal, Username not found'+ '\n')
				log.write(sendtolog)

		


class App:

	def __init__(self):
		self.settings = Settings()

		self.main_window = MainWindow(self)


	def run(self):
		self.main_window.mainloop()


if __name__ == '__main__':
	my_app = App()
	my_app.run()
