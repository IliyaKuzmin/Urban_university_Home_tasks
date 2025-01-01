#!/usr/bin/python3
import os
absolute_path=os.path.abspath(__file__)
class Product(object):
	def __init__(self, category, name, size):
		self.category=category
		self.name=name
		self.size=size
	def __str__(self):
		return f"{self.category}:{self.name} size:{self.size}"
class trade_assortment(object):
	def __init__(self, accounts_file):
		last_sep=absolute_path.rfind(os.sep)-len(absolute_path)
		dir_with_script=absolute_path[:last_sep]
		self.name_of_file=accounts_file
		self.file=os.path.join(dir_with_script,"data",f"{accounts_file}.txt")
	def add_service(self,products):
		file=open(self.file, "a+", encoding="utf-8")
		for el in products:
			file.seek(0)
			control=file.read()
			current_str=str(el)
			if current_str not in control:
				file.write(current_str+"\n")
			else: print (f"'{current_str}' already in file")
		file.close()
	def add(self,*products):# input: объекты класса Product кол-во неограничено
		try:
			self.add_service(products)
		except FileNotFoundError:
			os.makedirs(self.file[:-(len(self.name_of_file+".txt")+1)],mode=0o666,exist_ok=True)
			print("Директория создана! Вроде бы.")
			self.add_service(products)
	def correct(self,*corrector):# input: пара строк вида (строка с ошибкой, исправленная строка) кол-во неограничено
			file=open(self.file, "r+", encoding="utf-8")
			content=file.read()
			error,correct=corrector
			index_error_string=content.find(error)
			# практика указателей в файле
			file.seek(index_error_string)
			temp=file.read()
			separate=temp.split("\n")
			index=separate.index(error)
			separate[index]=correct
			to_save="\n".join(separate)
			if len(temp) <= len(to_save):
				file.seek(index_error_string)
				file.write(to_save)
			file.seek(0)
			print(file.read(index_error_string))
			file.close()
def test():
	last_sep=absolute_path.rfind(os.sep)-len(absolute_path)
	dir_with_script=absolute_path[:last_sep]
	target_file=os.path.join(dir_with_script,"data","experiment.txt")
	file=open(target_file, "r")
	pointer=0
	x=0
	while x < 3:
		file.seek(pointer)
		content=file.read(20)
		new_line=content.rfind("\n")
		pointer+=new_line+1
		print(content,new_line)
		x+=1
	file.close()
cargo=Product("Clothes","Pants","XXL")
cargo1=Product("Vegetables","Potato","2kg")
cargo2=Product("Vegetables","Tomato","2kg")
cargo3=Product("Non-Alcogol-Drinks","Fanta","0.5L")
stock= trade_assortment("experiment")
#stock.add(cargo,cargo1,cargo2,cargo3)
stock.correct("Vegetables:Potato size:2kg","Vegetables:Potato size:2.5kg")