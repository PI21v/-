from test import *
class User_number:
    def __init__(self):
        self.count_file=0
        self.count=1
        self.input_numbet=[]
        self.results=[]
        self.list_steps=[]
        self.list_reverse = []
        self.list_converse=[]

    def update(self, number_list):
        global settings1
        self.input_number=list(number_list.split("\n"))
        self.count=len(self.input_number)
        #self.count_file=settings1.count_file_number
        self.input_numbet=[]
        self.result_str=""
        self.results=[]
        self.list_steps=[]
        self.list_converse=[]
        self.list_reverse=[]

# методы для обработки. переносим из класса
def get_file_data():
    global user_number1
    global settings1
    s=""
    try:
        login_file=open(settings1.input_file_name,"r")

        try:
          for i in login_file:
            s+=i
        finally:
            login_file.close()
    except:
       s=""
    if s[-1]=="\n":
        s=s[:-2:]
    user_number1.update(s)



def get_data():
    global user_number1
    number_list="308.78\n54.67\n45.75\n"
    if number_list[-1]=="\n":
        number_list=number_list[:-2:]
    user_number1.update(number_list)

def get_result():
    global user_number1
    global number1
    global settings1
    steps=settings1.count_number
    if settings1.file:
        get_file_data()
    else:
        get_data()
    for i in user_number1.input_number:
        number1.update(i)
        number1.convert(steps)

        user_number1.result_str+=number1.print_result()
        if settings1.steps_flag==0 or settings1.steps_flag==2:
            user_number1.result_str+="\n\n"
            user_number1.result_str+=number1.steps_string
        if settings1.converse_flag==0 or settings1.converse_flag==2:
            user_number1.result_str+="\n"
            user_number1.result_str+=number1.converse_string
        user_number1.result_str+="\n"

        user_number1.list_steps.append(number1.steps_string)
        user_number1.list_converse.append(number1.converse_string)
        user_number1.results.append(number1.print_result())

def write_steps_file():
  global settings1
  global user_number1
  file_name="results/"+settings1.steps_file_name
  try:
            login_file=open(file_name,"w")
            try:
                for i in range(user_number1.count):
                    login_file.write(user_number1.list_steps[i])
                    login_file.write("\n\n")
            finally:
                login_file.close()
  except:
    s=""
  
def write_converse_file():
    global settings1
    global user_number1
    file_name="results/"+settings1.converse_file_name
    try:
             login_file=open(file_name,"w")
             try:
                    for i in range(user_number1.count):
                        login_file.write(user_number1.list_converse[i])
                        login_file.write("\n\n")
             finally:
                login_file.close()
    except:
        s=""

def print_result():
    global user_number1
    global settings1
    if settings1.steps_flag==1 or settings1.steps_flag==2:
        write_steps_file()
    if settings1.converse_flag==1 or settings1.converse_flag==2:
        write_converse_file()

    print(user_number1.result_str)


"""user_number1=User_number()
settings1=Settings()
number1=Number("1.1")
get_result()
print_result()
try:
        login_file=open("input.txt","w")
        try:
          login_file.write("308.78\n54.67\n45.75\n")
        finally:
            login_file.close()
except:
       s="""""
"""print_and_write_steps()
print_and_write_converse()
print(user_number1.result_str)
number1.convert(10)
number1.print_result()
print_and_write_steps()
print_and_write_converse()
get_data()
print(user_number1.input_number)"""