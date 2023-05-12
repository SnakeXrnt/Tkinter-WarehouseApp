from json import *

class Settings:

	def __init__(self):
		self.app_title = "App Gudang (beta v1.0) , by : Ethan , Kenzie"

		#WINDOW_CONFIG
		base = 100
		w_ratio = 8
		h_ratio = 6
		self.width = w_ratio*base
		self.height = h_ratio*base
		self.screen = f"{self.width}x{self.height}+400+300"


		#USER DATA
		self.username = "admin"
		self.password = "12345"

		#USER INPUT DATA
		self.usernameVar = None
		self.passwordVar = None

		gmailjson = open('gmail.json','r+')
		dictgmail = {}
		dictgmail = load(gmailjson)
		self.email = dictgmail['bini']["email"]
		self.password = dictgmail['bini']["pass"]
