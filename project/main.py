import sys, os
import pandas as pd

def clr():
    os.system('cls' if os.name == 'nt' else 'clear')

def banner():
    print("""
 ╭━━━╮╱╱╱╭╮╭╮
 ┃╭━╮┃╱╱╭╯╰┫┃
 ┃╰━╯┣╮╱┣╮╭┫╰━┳━━┳━╮
 ┃╭━━┫┃╱┃┃┃┃╭╮┃╭╮┃╭╮╮
 ┃┃╱╱┃╰━╯┃╰┫┃┃┃╰╯┃┃┃┃
 ╰╯╱╱╰━╮╭┻━┻╯╰┻━━┻╯╰╯
 ╱╱╱╱╭━╯┃  V1.0.0
 ╱╱╱╱╰━━╯
 ╭━━━╮╱╱╱╱╱╱╱╱╱╱╱╱╱╭╮
 ┃╭━╮┃╱╱╱╱╱╱╱╱╱╱╱╱╭╯╰╮
 ┃┃╱╰╋━━┳━╮╭╮╭┳━━┳┻╮╭╋━━┳━╮
 ┃┃╱╭┫╭╮┃╭╮┫╰╯┃┃━┫╭┫┃┃┃━┫╭╯
 ┃╰━╯┃╰╯┃┃┃┣╮╭┫┃━┫┃┃╰┫┃━┫┃
 ╰━━━┻━━┻╯╰╯╰╯╰━━┻╯╰━┻━━┻╯

 Contact         : https://wa.me/+6281251389915
 About Developer : https://github.com/Nux-xader
 ________________________________________________
""")

class Load:
	def __init__(self, path):
		self.path = path


	def json_reader(self):
		try:
			df = pd.read_json(self.path)
			return df
		except:
			return False


class Converter:
	def __init__(self, df):
		self.df = df

	def df_to_dict(self):
		return self.df.to_dict()


class Dump():
	def __init__(self, df, path):
		self.df = df
		self.path = path

	def as_xlsx(self):
		excel_wr = pd.ExcelWriter(self.path)
		self.df.to_excel(excel_wr)
		excel_wr.save()


def main():
	clr()
	banner()
	while True:
		try:
			path = str(input(" Json file : "))
			df = Load(path).json_reader()
			break
		except:
			print(f" [!] File {path} not found")

	path_save = str(input(" Save result to : "))
	print(" [+] Converting to xlsx ...")
	if path_save.split(".") != "xlsx": path_save+=".xlsx"
	dumper = Dump(df, path_save)
	dumper.as_xlsx()
	print(" [+] Success convert from json to xlsx")

if __name__ == '__main__':
	main()