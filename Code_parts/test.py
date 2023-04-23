#from settings import *
class Number:
    def __init__(self,test):
        test_len=list(test.split("."))
        self.sign=""
        self.reverse = ""
        self.len_double=len(test_len[1])
        self.integer10,self.double10=map(int,test_len)
        self.integer2=""
        self.double2=""
        self.number2=""
        self.number10=float(test)
        
        self.steps_string=""
        self.converse_string=""
    def update(self,test):
        self.sign = ""
        self.reverse = ""
        test_len=list(test.split("."))
        if test_len[0][0] == "-":
            self.sign = "-"
            test_len[0] = test_len[0][1::]
        self.len_double=len(test_len[1])
        self.integer10,self.double10=map(int,test_len)
        self.integer2=""
        self.double2=""
        self.number2=""
        self.number10=float(test)
        
        self.steps_string=""
        self.converse_string=""

    def print10(self):
        print(self.number10)
    def print2(self):
        print(self.number2)
    def print_result(self):
        return str(self.number10)+"="+self.sign+str(self.number2)
    
    #следующие методы создают строку, которую нужно вставить в текстовое поле/файл. это строки steps_string, converse_string
    
    def int_into_2(self):
        if self.integer10>1:
            tab=0
            self.steps_string+="{:d}|{:d}\n".format(self.integer10,2)
            counter=self.integer10//2
            self.integer2+=str(self.integer10-counter*2)
            self.steps_string+="{:s}{:d}|{:d}|{:d}\n".format(" "*tab,counter*2,counter,2)
            tab+=len(str(self.integer10))+1
            safe=self.integer10-counter*2
            self.integer10=counter
            while self.integer10!=1:
                counter=self.integer10//2
                self.integer2+=str(self.integer10-counter*2)
                if counter>1:
                    self.steps_string+="{:s}{:d} {:d}|{:d}|{:d}\n".format(" "*(tab-2),safe,counter*2,counter,2)
                else:
                    self.steps_string+="{:s}{:d} {:d}|{:d}\n".format(" "*(tab-2),safe,counter*2,counter)
                tab+=len(str(self.integer10))+1
                safe=self.integer10-counter*2
                self.integer10=counter
            self.steps_string+="{:s}{:d}\n".format(" "*(tab-2),safe)
            self.integer2+="1"
        else:
            self.steps_string+="{:d}|{:d}\n".format(self.integer10,2)
            self.steps_string+="{:s}{:d}|{:d}\n".format(" ",self.integer10,self.integer10)
            self.integer2+=str(self.integer10)


    def double_into_2(self,steps):
        n=self.len_double
        format_double="0"*(n-len(str(self.double10)))+str(self.double10)
        self.converse_string+=" |{:s}|2\n".format(format_double)
        for i in range(steps):
            self.double10*=2
            if len(str(self.double10))>n:
                self.double2+="1"
                self.double10%=10**(n)
                format_double="0"*(n-len(str(self.double10)))+str(self.double10)
                self.converse_string+="1|{:s}|2\n".format(format_double)
            else:
                self.double2+="0"
                format_double="0"*(n-len(str(self.double10)))+str(self.double10)
                self.converse_string+="0|{:s}|2\n".format(format_double)
                
    def convert(self,steps):
            self.int_into_2()
            self.double_into_2(steps)
            self.number2=self.integer2[::-1]+"."+self.double2

    def get_reverse(self):
        result_str = ""

        t = list(self.number2.split("."))
        int_part = 0
        double_part = 0
        count_int = len(t[0])
        count_double = 1
        part1 = ""
        part2 = ""
        part3 = ""
        part4 = ""
        for i in t[0]:
            part1 += str(int(i)) + "*2**(" + str(count_int - 1) + ")+"
            part2 += str(int(i) * 2 ** (count_int - 1)) + "+"
            int_part += int(i) * 2 ** (count_int - 1)
            count_int -= 1
        result_str += t[0] + "=" + part1[:-1:] + "=" + part2[:-1:] + "=" + str(int_part) + "\n"

        for i in t[1]:
            part3 += str(int(i)) + "*2**(-" + str(count_double) + ")+"
            part4 += str(int(i) * 2 ** (-count_double)) + "+"
            double_part += int(i) * 2 ** (-count_double)
            count_double += 1
        result_str += t[1] + "=" + part3[:-1:] + "=" + part4[:-1:] + "=" + str(double_part) + "\n"
        self.reverse = result_str

  
number1=Number("1.54")
number1.convert(10)
print(number1.print_result())
  

                





                
