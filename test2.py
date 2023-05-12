class Stock:

	def __init__(self, settings):
		self.settings = settings
		self.stock_list = self.settings.load_data(self.settings.data_json_path)

	def show_stock(self):
		#system('cls')
		self.stock_list = self.settings.load_data(self.settings.data_json_path)
		if len(self.stock_list) > 0:
			print('Kode\tBarang\tJumlah\tHarga\n')
			for kode, data in self.stock_list.items():
				print(f'{kode}\t{data["barang"]}\t{data["jumlah"]}\t{data["harga"]}\t')