class Settings:
	def __init__(self):
		self.count_number=5
		self.input_file_name=""
		self.output_file_name="output.txt"
		self.steps_file_name="steps.txt"
		self.converse_file_name="converse.txt"
		self.file=True
		self.steps_flag=-1
		self.converse_flag=-1
	
	def set_count_number(self,count):
		self.count_number=count
		
	def set_input_file(self,name):
		self.input_file_name=name
		
	def set_count_file_number(self, count_file):
		self.count_file_number = count_file
	
	def set_steps_flag(self, new_steps_flag):
		self.steps_flag=new_steps_flag
	""" -1 - нет
	0 - на экран
	1 - в файл
	2 - на экран и в файл"""
	
	def set_converse_flag(self, new_converse_flag):
		self.converse_flag = new_converse_flag
	
	def print(self):
		print("count_number=",self.count_number)
		print("input_file=",self.input_file_name)
		print("output_file=",self.output_file_name)
		print("steps_file_name=",self.steps_file_name)
		print("converse_file_name=",self.converse_file_name)
		print("count_file_number=",self.count_file_number)
		print("steps_flag=",self.steps_flag)
		print("converse_flag=",self.converse_flag)
	
		
#следующие функции для команд. выносим из класса
def get_file_count_number():
	x=int(input)
	#здесь будет получение из переменной для кнопок
	if x==1:
		return 1
	else:
		y=int(input())
		# здесь будет получение из поля
		return y
def change_all(count,name,count_file,new_steps_flag,new_converse_flag):
	global settings1
	settings1.set_count_number(count)
	settings1.set_input_file(name)
	settings1.set_count_file_number(count_file)
	settings1.set_steps_flag( new_steps_flag)
	settings1.set_converse_flag( new_converse_flag)

		
settings1=Settings()

#убираем следующие строчки
"""settings1.print()
print("Количество чисел после запятой")
count=int(input())
print("Файл для ввода")
name=input()
print("Количество чисел для ввода")
count_file=int(input())
print("Куда выводить шаги")
new_steps_flag=int(input())
print("Куда выводить перевод")
new_converse_flag=int(input())
change_all(count,name,count_file,new_steps_flag,new_converse_flag)
settings1.print()""" 