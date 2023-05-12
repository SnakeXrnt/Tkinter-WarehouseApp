import tkinter as tk

class Page02(tk.Frame):

	def __init__(self, parent, App):
		self.app = App
		self.settings = App.settings

		super().__init__(parent)
		self.configure(bg="red", width=self.settings.width, height=self.settings.height)
		# self.pack(fill="both", expand=True)
		self.pack(expand=True)
		self.show_login()

	def lihatPassword(self):
			nilaiCek = self.cek.get()
			 
			if nilaiCek== 1:
				self.passwordEntry['show'] = ''
			else:
				self.passwordEntry['show'] = '*'

	def show_login(self):
		background_color = "white"
		font_page = ("Arial", 25, "bold")
		font_content = ("Arial", 16, "bold")

		self.frame01 = tk.Frame(self, bg=background_color,height=self.settings.height, width=self.settings.width)
		self.frame01.pack(fill="both", expand=True)

		self.textTitle = tk.Label(self.frame01, text="Application Login Page\n", font=font_page, bg=background_color)
		self.textTitle.pack(expand=True)

		self.nameLabel = tk.Label(self.frame01, text="Username :\n", font=font_content, bg=background_color)
		self.nameLabel.pack(expand=True)

		self.nameVar = tk.StringVar()
		self.nameEntry = tk.Entry(self.frame01, bg=background_color, font=font_content, textvariable=self.nameVar)
		self.nameEntry.pack(expand=True)
		

		self.passwordLabel = tk.Label(self.frame01, text="Password :\n", font=font_content, bg=background_color)
		self.passwordLabel.pack(expand=True)

		self.passwordVar = tk.StringVar()
		self.passwordEntry = tk.Entry(self.frame01, bg=background_color, font=font_content, show="*", textvariable=self.passwordVar)
		self.passwordEntry.pack(expand=True)

		self.cek = tk.IntVar() 
         
		self.cbShowPass = tk.Checkbutton(self.frame01, text='show password\t', bg="white", variable=self.cek, command=self.lihatPassword)
		self.cbShowPass.pack(side="right")

		self.button_to_p1 = tk.Button(self.frame01, text="        Login         ", command=self.app.change_to_page01, bg=background_color, font=font_content)
		self.button_to_p1.pack(expand=True, side="right")

		
