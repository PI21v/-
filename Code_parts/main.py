from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from users import *
from settings import *
from user_number import *
from test import *
from correct import *

def changeTheme():
    global check
    if check == 0:
        calculatorTab.configure(background='black')
        settingsTab.configure(background='black')
        accountTab.configure(background='black')
        changePasswordTab.configure(background='black')
        enterNumbersLabel.configure(background='black',fg='white')
        resultLabel.configure(background='black',fg='white')
        numbers.configure(bg='black',fg='white',highlightbackground='white', highlightcolor='white',insertbackground='white')
        result.configure(bg='black', fg='white', highlightbackground='white', highlightcolor='white',
                         insertbackground='white')
        readFromFileButton.configure(background='black',fg='white',activeforeground='white',activebackground='black')
        workButton.configure(background='black',fg='white',activeforeground='white',activebackground='black')
        darkThemeCheck.configure(text='Светлая тема',background='black',fg='white',activeforeground='white',activebackground='black')
        rangeLabel.configure(background='black',fg='white')
        rangeScale.configure(background='black',fg='white',activebackground='yellow')
        readCountLabel.configure(background='black',fg='white')
        countRadioButton1.configure(selectcolor='black',fg='white',bg='black', font=('Arial', 15), activebackground='black',
                                        activeforeground='white')
        countRadioButton2.configure(selectcolor='black', fg='white', bg='black', font=('Arial', 15),activebackground='black',
                                    activeforeground='white')
        chooseFileButton.configure(background='black',fg='white',activeforeground='white',activebackground='black')
        calculationRadioButton1.configure(selectcolor='black',fg='white',bg='black', font=('Arial', 15), activebackground='black',
                                        activeforeground='white')
        calculationRadioButton2.configure(selectcolor='black', fg='white', bg='black', font=('Arial', 15),
                                          activebackground='black',
                                          activeforeground='white')
        calculationRadioButton3.configure(selectcolor='black', fg='white', bg='black', font=('Arial', 15),
                                          activebackground='black',
                                          activeforeground='white')
        calculationRadioButton4.configure(selectcolor='black', fg='white', bg='black', font=('Arial', 15),
                                          activebackground='black',
                                          activeforeground='white')
        saveChangesButton.configure(background='black',fg='white',activeforeground='white',activebackground='black')
        calculationsLabel.configure(background='black', fg='white')
        reversedCalculationsLabel.configure(background='black', fg='white')
        reversedCalculationRadioButton1.configure(selectcolor='black', fg='white', bg='black', font=('Arial', 15),
                                          activebackground='black',
                                          activeforeground='white')
        reversedCalculationRadioButton2.configure(selectcolor='black', fg='white', bg='black', font=('Arial', 15),
                                                  activebackground='black',
                                                  activeforeground='white')
        reversedCalculationRadioButton3.configure(selectcolor='black', fg='white', bg='black', font=('Arial', 15),
                                                  activebackground='black',
                                                  activeforeground='white')
        reversedCalculationRadioButton4.configure(selectcolor='black', fg='white', bg='black', font=('Arial', 15),
                                                  activebackground='black',
                                                  activeforeground='white')
        accountButton.configure(background='black',fg='white',activeforeground='white',activebackground='black')
        accLoginLabel.configure(background='black',fg='white')
        accGoBackButton.configure(background='black',fg='white',activeforeground='white',activebackground='black')
        accChangePassword.configure(background='black',fg='white',activeforeground='white',activebackground='black')
        accCurrentLoginLabel.configure(background='black',fg='white')
        goBackToAccountButton.configure(background='black',fg='white',activeforeground='white',activebackground='black')
        changeTabPasswordLabel.configure(background='black',fg='white')
        changeToLabel.configure(background='black',fg='white')
        currentPasswordEntry.configure(bg='black',fg='white',highlightbackground='white', highlightcolor='white',
                                       insertbackground='white')
        changeToPasswordEntry.configure(bg='black',fg='white',highlightbackground='white', highlightcolor='white',
                                       insertbackground='white')
        changePasswordButton.configure(background='black',fg='white',activeforeground='white',activebackground='black')
        accWatchHistory.configure(background='black',fg='white',activeforeground='white',activebackground='black')
        style.configure('TNotebook.Tab', background='black', foreground='white')
        style.map('TNotebook.Tab', background=[("selected", 'black')])
        check = 1
    else:
        calculatorTab.configure(background='#B9CDE5')
        settingsTab.configure(background='#B9CDE5')
        accountTab.configure(background='#B9CDE5')
        changePasswordTab.configure(background='#B9CDE5')
        enterNumbersLabel.configure(background='#B9CDE5', fg='black')
        resultLabel.configure(background='#B9CDE5', fg='black')
        numbers.configure(bg='white',fg='black',highlightbackground='black', highlightcolor='black',insertbackground='black')
        result.configure(bg='white',fg='black',highlightbackground='black', highlightcolor='black',insertbackground='black')
        readFromFileButton.configure(background='#DCE6F2',activebackground='#DCE6F2',activeforeground='black',fg='black')
        workButton.configure(background='#DCE6F2',activebackground='#DCE6F2',activeforeground='black',fg='black')
        darkThemeCheck.configure(text='Тёмная тема',background='#DCE6F2',activebackground='#DCE6F2',activeforeground='black',fg='black')
        rangeLabel.configure(background='#B9CDE5', fg='black')
        rangeScale.configure(background='#B9CDE5', fg='black',activebackground='#B9CDE5')
        readCountLabel.configure(background='#B9CDE5', fg='black')
        countRadioButton1.configure(selectcolor='white', fg='black', bg='#B9CDE5', font=('Arial', 15),
                                    activebackground='#B9CDE5',
                                    activeforeground='black')
        countRadioButton2.configure(selectcolor='white', fg='black', bg='#B9CDE5', font=('Arial', 15),
                                    activebackground='#B9CDE5',
                                    activeforeground='black')
        chooseFileButton.configure(background='#DCE6F2',activebackground='#DCE6F2',activeforeground='black',fg='black')
        calculationRadioButton1.configure(selectcolor='white', fg='black', bg='#B9CDE5', font=('Arial', 15),
                                    activebackground='#B9CDE5',
                                    activeforeground='black')
        calculationRadioButton2.configure(selectcolor='white', fg='black', bg='#B9CDE5', font=('Arial', 15),
                                          activebackground='#B9CDE5',
                                          activeforeground='black')
        calculationRadioButton3.configure(selectcolor='white', fg='black', bg='#B9CDE5', font=('Arial', 15),
                                          activebackground='#B9CDE5',
                                          activeforeground='black')
        calculationRadioButton4.configure(selectcolor='white', fg='black', bg='#B9CDE5', font=('Arial', 15),
                                          activebackground='#B9CDE5',
                                          activeforeground='black')
        saveChangesButton.configure(background='#DCE6F2',activebackground='#DCE6F2',activeforeground='black',fg='black')
        calculationsLabel.configure(background='#B9CDE5', fg='black')
        reversedCalculationsLabel.configure(background='#B9CDE5', fg='black')
        reversedCalculationRadioButton1.configure(selectcolor='white', fg='black', bg='#B9CDE5', font=('Arial', 15),
                                          activebackground='#B9CDE5',
                                          activeforeground='black')
        reversedCalculationRadioButton2.configure(selectcolor='white', fg='black', bg='#B9CDE5', font=('Arial', 15),
                                                  activebackground='#B9CDE5',
                                                  activeforeground='black')
        reversedCalculationRadioButton3.configure(selectcolor='white', fg='black', bg='#B9CDE5', font=('Arial', 15),
                                                  activebackground='#B9CDE5',
                                                  activeforeground='black')
        reversedCalculationRadioButton4.configure(selectcolor='white', fg='black', bg='#B9CDE5', font=('Arial', 15),
                                                  activebackground='#B9CDE5',
                                                  activeforeground='black')
        accountButton.configure(background='#DCE6F2',activebackground='#DCE6F2',activeforeground='black',fg='black')
        accLoginLabel.configure(background='#B9CDE5', fg='black')
        accGoBackButton.configure(background='#DCE6F2',activebackground='#DCE6F2',activeforeground='black',fg='black')
        accChangePassword.configure(background='#DCE6F2',activebackground='#DCE6F2',activeforeground='black',fg='black')
        accCurrentLoginLabel.configure(background='#B9CDE5', fg='black')
        goBackToAccountButton.configure(background='#DCE6F2',activebackground='#DCE6F2',activeforeground='black',fg='black')
        changeTabPasswordLabel.configure(background='#B9CDE5', fg='black')
        changeToLabel.configure(background='#B9CDE5', fg='black')
        currentPasswordEntry.configure(bg='white',fg='black',highlightbackground='black', highlightcolor='black',
                                       insertbackground='black')
        changeToPasswordEntry.configure(bg='white',fg='black',highlightbackground='black', highlightcolor='black',
                                       insertbackground='black')
        changePasswordButton.configure(background='#DCE6F2',activebackground='#DCE6F2',activeforeground='black',fg='black')
        accWatchHistory.configure(background='#DCE6F2',activebackground='#DCE6F2',activeforeground='black',fg='black')
        style.configure('TNotebook.Tab', background='#B9CDE5', foreground='black')
        style.map('TNotebook.Tab', background=[("selected", '#B9CDE5')])
        check = 0


def login():
    notebook.forget(loginTab)
    notebook.add(calculatorTab, text="Калькулятор")
    notebook.add(settingsTab, text="Настройки")

def openRegistrationTab():
    notebook.forget(loginTab)
    notebook.add(registrationTab, text="Регистрация")
    notebook.select(registrationTab)


def openLoginTab():
    notebook.forget(registrationTab)
    notebook.add(loginTab, text="Вход")
    notebook.select(loginTab)


def openAccountTab():
    notebook.forget(settingsTab)
    notebook.add(accountTab, text="Аккаунт")
    notebook.select(accountTab)


def goBackToSettings():
    notebook.forget(accountTab)
    notebook.add(settingsTab, text="Настройки")
    notebook.select(settingsTab)


def openChangePasswordTab():
    notebook.forget(accountTab)
    notebook.add(changePasswordTab, text="Смена пароля")
    notebook.select(changePasswordTab)


def goBackToAccount():
    notebook.forget(changePasswordTab)
    notebook.add(accountTab, text="Аккаунт")
    notebook.select(accountTab)


def openFile():
    filePath = filedialog.askopenfilename()
    if filePath[-4::] == '.txt':
        settings1.input_file_name = filePath
        messagebox.showinfo("Настройки", "Файл " + filePath + " успешно выбран")
    else:
        messagebox.showerror("Настройки", "Файл должен иметь расширение \'.txt\'")


settings1 = Settings()
users1 = Users()
user_number1 = User_number()
number1 = Number("1.1")

def sign_up_message():
    global users1
    login = loginEntry2.get()
    password = passwordEntry2.get()
    if login == '' or password == '':
        messagebox.showerror("Регистрация", "Логин и/или пароль не могут быть пустыми!")
    else:
        out_test = users1.sign_up(login, password)
        if out_test == 0:
            messagebox.showinfo("Регистрация", "Успешная регистрация")
            users1.user_name = login
            accCurrentLoginLabel.configure(text=users1.user_name)
            notebook.forget(registrationTab)
            notebook.add(calculatorTab, text="Калькулятор")
            notebook.add(settingsTab, text="Настройки")
        elif out_test == 1:
            messagebox.showerror("Регистрация", "Некорректный логин или пароль")
        elif out_test == 2:
            messagebox.showerror("Регистрация", "Пользователь уже существует")


def sign_in_message():
    global users1
    login = loginEntry1.get()
    password = passwordEntry1.get()
    in_test = users1.sign_in(login, password)
    if in_test == 0:
        messagebox.showinfo("Вход", "Успешный вход")
        users1.user_name = login
        accCurrentLoginLabel.configure(text=users1.user_name)
        notebook.forget(loginTab)
        notebook.add(calculatorTab, text="Калькулятор")
        notebook.add(settingsTab, text="Настройки")
        # здесь будет переход на основную форму
    elif in_test == 1:
        messagebox.showerror("Вход", "Пользователь не зарегистрирован")
    elif in_test == 2:
        messagebox.showerror("Вход", "Неверный пароль")


def change_all():
    global settings1
    global count
    global calculation
    global reversedCalculation
    count1 = rangeScale.get()
    count_file = count.get()
    new_steps_flag = calculation.get()
    new_converse_flag = reversedCalculation.get()
    settings1.set_count_number(count1)
    settings1.set_count_file_number(count_file)
    settings1.set_steps_flag(new_steps_flag)
    settings1.set_converse_flag(new_converse_flag)
    messagebox.showinfo('Настройки', 'Настройки успешно изменены')


def get_data():
    global user_number1
    number_list=numbers.get(1.0, "end-1c")
    if number_list[-1]=="\n":
        number_list=number_list[:-2:]
    test = ok(number_list)
    if test == -1:
        return test
    else:
        user_number1.update(number_list)
        return 0

def get_result():
    global users1
    global user_number1
    global number1
    global settings1
    steps=settings1.count_number
    if get_data() == -1:
        messagebox.showerror("Ввод", "Некорректный ввод")
    else:
        for i in user_number1.input_number:
            number1.update(i)
            number1.convert(steps)
            number1.get_reverse()
            user_number1.result_str += number1.print_result()
            if settings1.steps_flag == 1 or settings1.steps_flag == 2:
                user_number1.result_str += "\n\n"
                user_number1.result_str += number1.steps_string
                user_number1.result_str += "\n"
                user_number1.result_str += number1.converse_string
            user_number1.result_str += "\n"
            if settings1.converse_flag == 1 or settings1.converse_flag == 2:
                user_number1.result_str += "\n"
                user_number1.result_str += number1.reverse
            user_number1.list_steps.append(number1.steps_string)
            user_number1.list_reverse.append(number1.reverse)
            user_number1.list_converse.append(number1.converse_string)
            user_number1.results.append(number1.print_result())

            try:
                log_file = open("log/" + users1.user_name + ".txt", "a")
                try:
                    log_file.write(number1.print_result()+"\n")
                finally:
                    log_file.close()
            except:
                s = ""

        result.delete('1.0', END)
        result.insert(1.0, user_number1.result_str)

        if settings1.steps_flag==2 or settings1.steps_flag==3:
            write_steps_file()
        if settings1.converse_flag==2 or settings1.converse_flag==3:
            write_converse_file()

def get_file_result():
    global user_number1
    global number1
    global settings1
    if settings1.input_file_name == '':
        messagebox.showerror("Файл", "Файл не выбран")
    else:
        steps=settings1.count_number
        if get_file_data() == -1:
            messagebox.showerror("Ввод", "Некорректный ввод")
        else:
            for i in user_number1.input_number:
                number1.update(i)
                number1.convert(steps)
                number1.get_reverse()
                user_number1.result_str += number1.print_result()
                if settings1.steps_flag == 1 or settings1.steps_flag == 2:
                    user_number1.result_str += "\n\n"
                    user_number1.result_str += number1.steps_string
                    user_number1.result_str += "\n"
                    user_number1.result_str += number1.converse_string
                user_number1.result_str += "\n"
                if settings1.converse_flag == 1 or settings1.converse_flag == 2:
                    user_number1.result_str += "\n"
                    user_number1.result_str += number1.reverse
                user_number1.list_steps.append(number1.steps_string)
                user_number1.list_reverse.append(number1.reverse)
                user_number1.list_converse.append(number1.converse_string)
                user_number1.results.append(number1.print_result())

                try:
                    log_file = open("log/" + users1.user_name + ".txt", "a")
                    try:
                        log_file.write(number1.print_result() + "\n")
                    finally:
                        log_file.close()
                except:
                    s = ""

            result.delete('1.0', END)
            result.insert(1.0, user_number1.result_str)

            if settings1.steps_flag==2 or settings1.steps_flag==3:
                write_steps_file()
            if settings1.converse_flag==2 or settings1.converse_flag==3:
                write_converse_file()

def write_steps_file():
    global settings1
    global user_number1
    file_name = "results/" + settings1.steps_file_name
    try:
        login_file = open(file_name, "w")
        try:
            for i in range(user_number1.count):
                login_file.write(user_number1.list_steps[i])
                login_file.write("\n")
                login_file.write(user_number1.list_converse[i])
                login_file.write("\n\n")
        finally:
            login_file.close()
    except:
        s = ""


def write_converse_file():
    global settings1
    global user_number1
    file_name = "results/" + settings1.converse_file_name
    try:
        login_file = open(file_name, "w")
        try:
            for i in range(user_number1.count):
                login_file.write(user_number1.list_reverse[i])
                login_file.write("\n\n")
        finally:
            login_file.close()
    except:
        s = ""

def get_file_data():
    global user_number1
    global settings1
    s=""
    print(settings1.input_file_name)
    try:
        login_file=open(settings1.input_file_name,"r")
        if count.get() == 0:
            try:
              for i in login_file:
                s+=i
                break
            finally:
                login_file.close()
        else:
            try:
                for i in login_file:
                    s += i
            finally:
                login_file.close()
    except:
       s=""
    if s[-1]=="\n":
        s=s[:-2:]
    numbers.delete('1.0', END)
    test = ok(s)
    if test == -1:
        return test
    else:
        numbers.insert(1.0, s)
        user_number1.update(s)
        return 0


def correct_password_test(password):
    for s in password:
        if ord(s) == 32:
            return 1
    return 0

def change_password():
    global users1
    global login_file
    password = currentPasswordEntry.get()
    new_password = changeToPasswordEntry.get()
    if password == '' or new_password == '':
        messagebox.showerror("Смена пароля", "Текущий и/или новый паротль не может быть пустым")
    else:
        if correct_password_test(new_password)+correct_password_test(password) > 0:
            messagebox.showerror("Смена пароля", "Текущий и/или новый паротль не может содержать пробелы")
        else:
            login = users1.user_name
            user_id = users1.search(login)
            if user_id > 0:
                current_password = locker1.unlock(users1.login_list[user_id][1])
                if password == current_password:
                    users1.login_list[user_id][1] = locker1.lock(new_password)
                    try:
                        login_file = open("user.txt", "w")
                        for i in users1.login_list:
                            login_file.write(i[0] + " " + i[1] + " " + "\n")
                    except:
                        s = ""
                    finally:
                        login_file.close()
                    messagebox.showinfo("Смена пароля", "Успешная смена пароля")
                else:
                    messagebox.showerror("Смена пароля", "Неверный пароль")


window = Tk()
window.geometry('1366x768')
window.title('ConverterFloatsToBinary')
window.iconbitmap("photo.ico")
window.resizable(height=False, width=False)




def openHistoryWindow():
    global check
    global users1
    global user_number1
    global settings1
    historyWindow = Toplevel(window)
    historyWindow.geometry('1366x768')
    historyWindow.title('История кальуклятора')
    historyWindow.iconbitmap("history.ico")
    historyWindow.resizable(height=False, width=False)
    if check == 0:
        historyWindow.configure(bg='#B9CDE5')
        historyLabel = Label(historyWindow, text='История калькулятора:',fg='black', bg='#B9CDE5',font=('Arial', 15))
        historyLabel.grid(row=0, column=0, sticky=SW, pady=(35, 0), padx=10)
        historyText = Text(historyWindow, bg='white',fg='black',highlightthickness=1, highlightbackground='black', highlightcolor='black',
                        insertbackground='black', width=100, height=20, font=('Arial', 15))
        historyText.grid(row=1, column=0, pady=(10, 0), padx=(10, 0))
        historyScrollbar = ttk.Scrollbar(historyWindow, orient='vertical', command=historyText.yview)
        historyScrollbar.grid(row=1, column=1, sticky='NWS', pady=(10, 0))
        historyText['yscrollcommand'] = historyScrollbar.set
    else:
        historyWindow.configure(bg='black')
        historyLabel = Label(historyWindow, text='История калькулятора:',fg='white', bg='black', font=('Arial', 15))
        historyLabel.grid(row=0, column=0, sticky=SW, pady=(35, 0), padx=10)
        historyText = Text(historyWindow, bg='black', fg='white', highlightthickness=1, highlightbackground='white',
                        highlightcolor='white',insertbackground='white', width=100, height=20, font=('Arial', 15))
        historyText.grid(row=1, column=0, pady=(10, 0), padx=(10, 0))
        historyScrollbar = ttk.Scrollbar(historyWindow, orient='vertical', command=historyText.yview)
        historyScrollbar.grid(row=1, column=1, sticky='NWS', pady=(10, 0))
        historyText['yscrollcommand'] = historyScrollbar.set


    s = ""
    print(settings1.input_file_name)
    try:
        login_file = open("log/" + users1.user_name + ".txt", "r")

        try:
            for i in login_file:
                s += i
        finally:
            login_file.close()

    except:
        s = ""
    if s[-1] == "\n":
        s = s[:-2:]
    historyText.delete('1.0', END)
    historyText.insert('1.0', s)


style = ttk.Style()
style.theme_use("default")
style.configure('TNotebook.Tab', background='#B9CDE5', foreground='black')
style.map('TNotebook.Tab', background=[("selected", '#B9CDE5')])

notebook = ttk.Notebook(window)

loginTab = Frame(notebook, bg='#B9CDE5')
loginTab.grid_columnconfigure(0, weight=1, minsize=160)
loginTab.grid_columnconfigure(1, weight=1, minsize=100)
loginTab.grid_columnconfigure(2, weight=1, minsize=100)
loginTab.grid_columnconfigure(3, weight=1, minsize=120)
registrationTab = Frame(notebook, bg='#B9CDE5')
registrationTab.grid_columnconfigure(0, weight=1, minsize=160)
registrationTab.grid_columnconfigure(1, weight=1, minsize=100)
registrationTab.grid_columnconfigure(2, weight=1, minsize=120)
registrationTab.grid_columnconfigure(3, weight=1, minsize=100)
calculatorTab = Frame(notebook, bg='#B9CDE5')
calculatorTab.grid_columnconfigure(0, weight=1, minsize=300)
calculatorTab.grid_columnconfigure(1, weight=1, minsize=120)
calculatorTab.grid_columnconfigure(2, weight=1, minsize=20)
calculatorTab.grid_columnconfigure(3, weight=2, minsize=300)
calculatorTab.grid_columnconfigure(4, weight=1, pad=90, minsize=20)
settingsTab = Frame(notebook, bg='#B9CDE5')
settingsTab.grid_columnconfigure(4, weight=1, pad=90, minsize=30)
accountTab = Frame(notebook, bg='#B9CDE5')
changePasswordTab = Frame(notebook, bg='#B9CDE5')

check = 0

notebook.add(loginTab, text="Вход")

# Виджеты входа

loginLabel1 = Label(loginTab, text="Логин:", bg='#B9CDE5', font=('Arial', 20), width=20,
                    height=6, pady=6, padx=50, anchor=SE)
loginLabel1.grid(row=1, column=0)
passwordLabel1 = Label(loginTab, text="Пароль:", bg='#B9CDE5', font=('Arial', 20), width=20,
                       height=5, pady=6, padx=50, anchor=NE)
passwordLabel1.grid(row=2, column=0)
loginEntry1 = Entry(loginTab, width=20, font=('Arial', 20), highlightthickness=1,
                    highlightbackground='black', highlightcolor='black')
loginEntry1.grid(row=1, column=1, sticky=S, pady=6)
passwordEntry1 = Entry(loginTab, width=20, font=('Arial', 20), highlightthickness=1,
                       highlightbackground='black', highlightcolor='black')
passwordEntry1.grid(row=2, column=1, sticky=N, pady=6)
loginButton1 = Button(loginTab, text='Вход', width=20, height=2, bg='#DCE6F2',
                      command=sign_in_message, activebackground='#DCE6F2', font=('Arial'))
loginButton1.grid(row=1, column=2, rowspan=3, sticky=W, padx=10)
registerButton1 = Button(loginTab, text='Регистрация', width=20, height=2, bg='#DCE6F2',
                         activebackground='#DCE6F2', font=('Arial'),
                         command=openRegistrationTab)
registerButton1.grid(row=0, column=3, sticky=NE, padx=10, pady=10)
warningLabel1 = Label(loginTab, bg='#B9CDE5', font=('Arial', 20),
                      text='Если Вы используете программу впервые, пожалуйста,' +
                           'зарегистрируйтесь')
warningLabel1.grid(row=3, column=0, columnspan=4)

# Виджеты регистрации

loginLabel2 = Label(registrationTab, text="Логин:", bg='#B9CDE5', font=('Arial', 20), width=20,
                    height=6, pady=6, padx=50, anchor=SE)
loginLabel2.grid(row=1, column=0)
passwordLabel2 = Label(registrationTab, text="Пароль:", bg='#B9CDE5', font=('Arial', 20),
                       width=20, height=5, pady=6, padx=50, anchor=NE)
passwordLabel2.grid(row=2, column=0)
loginEntry2 = Entry(registrationTab, width=20, font=('Arial', 20), highlightthickness=1,
                    highlightbackground='black', highlightcolor='black')
loginEntry2.grid(row=1, column=1, sticky=S, pady=6)
passwordEntry2 = Entry(registrationTab, width=20, font=('Arial', 20), highlightthickness=1,
                       highlightbackground='black', highlightcolor='black')
passwordEntry2.grid(row=2, column=1, sticky=N, pady=6)
registerButton2 = Button(registrationTab, text='Регистрация', width=20, height=2, bg='#DCE6F2',
                         command=sign_up_message, activebackground='#DCE6F2', font=('Arial'))
registerButton2.grid(row=1, column=2, rowspan=3, sticky=W, padx=10)
loginButton2 = Button(registrationTab, text='Вход', width=20, height=2, bg='#DCE6F2',
                      activebackground='#DCE6F2', font=('Arial'),
                      command=openLoginTab)
loginButton2.grid(row=0, column=3, sticky=NE, padx=10, pady=10)
warningLabel2 = Label(registrationTab, bg='#B9CDE5', font=('Arial', 20),
                      text='Придумайте логин и пароль для входа в приложение')
warningLabel2.grid(row=3,column=0, columnspan=4)

# Виджеты калькулятора:

enterNumbersLabel = Label(calculatorTab, text='Введите число(-а) для перевода:',
                          bg='#B9CDE5', font=('Arial', 15), height=5, width=28, anchor=SW)
enterNumbersLabel.grid(row=0, column=0,padx=(50, 0), pady=2,sticky=W, columnspan=2)
numbers = Text(calculatorTab, height=15, width=50, highlightthickness=1,
               highlightbackground='black', highlightcolor='black', font=('Arial', 12))
numbers.grid(row=1, column=0, sticky=W, padx=(50, 0), columnspan=2)
numbersScrollbar = ttk.Scrollbar(calculatorTab, orient='vertical', command=numbers.yview)
numbersScrollbar.grid(row=1, column=2, sticky='NWS')
numbers['yscrollcommand'] = numbersScrollbar.set
resultLabel = Label(calculatorTab, text='Результат:', bg='#B9CDE5', font=('Arial', 15),
                    height=5, width=40, anchor=SW)
resultLabel.grid(row=0, column=3, padx=(110, 0), pady=2, sticky=W)
result = Text(calculatorTab, height=15, width=70, highlightthickness=1,
              highlightbackground='black', highlightcolor='black', font=('Arial', 12))
result.grid(row=1, column=3, sticky=W, padx=(110, 0))
resultScrollbar = ttk.Scrollbar(calculatorTab, orient='vertical', command=result.yview)
resultScrollbar.grid(row=1, column=4, sticky='NWS')
result['yscrollcommand'] = resultScrollbar.set
readFromFileButton = Button(calculatorTab, text='Считать число(-а) из файла',
                            bg='#DCE6F2', activebackground='#DCE6F2', font=('Arial'), command=get_file_result)
readFromFileButton.grid(row=2,column=0,sticky=W,padx=(70,10),pady=20)
workButton = Button(calculatorTab, text='Перевести', bg='#DCE6F2', activebackground='#DCE6F2',
                    font=('Arial'), anchor=W, command=get_result)
workButton.grid(row=2, column=1, sticky=W, pady=20)

# Виджеты настроек

darkThemeCheck = Button(settingsTab, text='Тёмная тема', bg='#DCE6F2',
                        command=changeTheme, activebackground='#DCE6F2', font=('Arial'))
darkThemeCheck.grid(row=0, column=0,
                    padx=10, pady=10, sticky=W)
rangeLabel = Label(settingsTab, text='Диапазон чисел после запятой:', bg='#B9CDE5',
                   font=('Arial', 15))
rangeLabel.grid(row=1, column=0, padx=10, pady=(20, 0))
rangeScale = Scale(settingsTab, bg='#B9CDE5', orient='horizontal', highlightthickness=0,
                   activebackground='#B9CDE5', from_=1, to=20)
rangeScale.set(5)
rangeScale.grid(row=2, column=0)
readCountLabel = Label(settingsTab, text='Чтение чисел из файла:', bg='#B9CDE5',
                       font=('Arial', 15))
readCountLabel.grid(row=3, column=0, sticky=NW, padx=10, pady=20)

count = IntVar()
counts = ["Одного числа", "Всех чисел"]
countRadioButton1 = Radiobutton(settingsTab, text=counts[0], variable=count, value=0,
                                bg='#B9CDE5', font=('Arial', 15), activebackground='#B9CDE5')
countRadioButton1.grid(row=4, column=0, sticky=W, padx=10)
countRadioButton2 = Radiobutton(settingsTab, text=counts[1], variable=count, value=1,
                                bg='#B9CDE5', font=('Arial', 15), activebackground='#B9CDE5')
countRadioButton2.grid(row=5, column=0, sticky=W, padx=10)


chooseFileButton = Button(settingsTab, text='Выбрать файл', bg='#DCE6F2',
                          activebackground='#DCE6F2', font=('Arial'), command=openFile)
chooseFileButton.grid(row=7, column=0,padx=10, pady=10, sticky=W)

calculationsLabel = Label(settingsTab, text='Вывод перевода:', bg='#B9CDE5',
                          font=('Arial', 15))
calculationsLabel.grid(row=0, column=2, padx=(220, 0))

calculation = IntVar()
calculationOptions = ["Нет", "Только на экран", "На экран и в файл", "Только в файл"]

calculationRadioButton1 = Radiobutton(settingsTab, text=calculationOptions[0], variable=calculation, value=0,
                                     fg='black', bg='#B9CDE5', font=('Arial', 15), activebackground='#B9CDE5', height=2)
calculationRadioButton1.grid(row=0, column=3, sticky=W, padx=10)

calculationRadioButton2 = Radiobutton(settingsTab, text=calculationOptions[1], variable=calculation, value=1,
                                      fg='black',bg='#B9CDE5', font=('Arial', 15), activebackground='#B9CDE5', height=2)
calculationRadioButton2.grid(row=1, column=3, sticky=W, padx=10)
calculationRadioButton3 = Radiobutton(settingsTab, text=calculationOptions[2], variable=calculation, value=2,
                                      fg='black',bg='#B9CDE5', font=('Arial', 15), activebackground='#B9CDE5', height=2)
calculationRadioButton3.grid(row=2, column=3, sticky=W, padx=10)
calculationRadioButton4 = Radiobutton(settingsTab, text=calculationOptions[3], variable=calculation, value=3,
                                      fg='black',bg='#B9CDE5', font=('Arial', 15), activebackground='#B9CDE5', height=2)
calculationRadioButton4.grid(row=3, column=3, sticky=W, padx=10)
reversedCalculationsLabel = Label(settingsTab, text='Вывод обратного перевода:', bg='#B9CDE5',
                                  font=('Arial', 15))
reversedCalculationsLabel.grid(row=6, column=2, padx=(220, 0))
reversedCalculation = IntVar()
reversedCalculationRadioButton1 = Radiobutton(settingsTab, text=calculationOptions[0],
                                                 variable=reversedCalculation, value=0,
                                                 bg='#B9CDE5', font=('Arial', 15), activebackground='#B9CDE5', height=2)
reversedCalculationRadioButton1.grid(row=6, column=3, sticky=W, padx=10)
reversedCalculationRadioButton2 = Radiobutton(settingsTab, text=calculationOptions[1],
                                                 variable=reversedCalculation, value=1,
                                                 bg='#B9CDE5', font=('Arial', 15), activebackground='#B9CDE5', height=2)
reversedCalculationRadioButton2.grid(row=7, column=3, sticky=W, padx=10)
reversedCalculationRadioButton3 = Radiobutton(settingsTab, text=calculationOptions[2],
                                                 variable=reversedCalculation, value=2,
                                                 bg='#B9CDE5', font=('Arial', 15), activebackground='#B9CDE5', height=2)
reversedCalculationRadioButton3.grid(row=8, column=3, sticky=W, padx=10)
reversedCalculationRadioButton4 = Radiobutton(settingsTab, text=calculationOptions[3],
                                                 variable=reversedCalculation, value=3,
                                                 bg='#B9CDE5', font=('Arial', 15), activebackground='#B9CDE5', height=2)
reversedCalculationRadioButton4.grid(row=9, column=3, sticky=W, padx=10)

accountButton = Button(settingsTab, text='Аккаунт', width=20, bg='#DCE6F2', command=openAccountTab,
                       activebackground='#DCE6F2', font=('Arial'))
accountButton.grid(row=0, column=4, sticky=NE, padx=10, pady=10)

saveChangesButton = Button(settingsTab, text='Сохранить изменения', bg='#DCE6F2',
                          command=change_all, activebackground='#DCE6F2', font=('Arial'))
saveChangesButton.grid(row=9, column=0, padx=10, pady=10, sticky=W)

# Виджеты аккаунта
accGoBackButton = Button(accountTab, text='Назад', width=20, bg='#DCE6F2', height=2,
                         activebackground='#DCE6F2', font=('Arial'),
                         command=goBackToSettings)
accGoBackButton.grid(row=0, column=0, sticky=NW, padx=10, pady=10, )
accLoginLabel = Label(accountTab, text="Текущий пользователь:", bg='#B9CDE5', font=('Arial', 20), width=20,
                      height=6, pady=6, padx=50, anchor=SE)
accLoginLabel.grid(row=1, column=0, padx=(70, 0))
accCurrentLoginLabel = Label(accountTab, font=('Arial', 20),bg='#B9CDE5')
accCurrentLoginLabel.grid(row=1, column=1, sticky=SW, pady=(0, 6))
accChangePassword = Button(accountTab, font=('Arial', 20), text='Смена пароля',
                           command=openChangePasswordTab, bg='#DCE6F2', activebackground='#DCE6F2')
accChangePassword.grid(row=2,column=0,sticky=N,padx=(170, 0))
accWatchHistory = Button(accountTab, text="Посмотреть историю калькулятора", bg='#DCE6F2',activebackground='#DCE6F2',
                         font=('Arial',20),command=openHistoryWindow)
accWatchHistory.grid(row=2,column=1, sticky=NS)

# Виджеты смены пароля

goBackToAccountButton = Button(changePasswordTab, text='Аккаунт', width=20, bg='#DCE6F2', height=2,
                               activebackground='#DCE6F2', font=('Arial'),command=goBackToAccount)
goBackToAccountButton.grid(row=0, column=0, sticky=NW, padx=10, pady=10, )
changeTabPasswordLabel = Label(changePasswordTab, text="Текущий пароль:", bg='#B9CDE5', font=('Arial', 20), width=20,
                            height=6, pady=6, padx=50, anchor=SE)
changeTabPasswordLabel.grid(row=1, column=0, padx=(70, 0))
changeToLabel = Label(changePasswordTab, text="Сменить на:", bg='#B9CDE5', font=('Arial', 20), width=20,
                      height=5, pady=6, padx=50, anchor=NE)
changeToLabel.grid(row=2, column=0, padx=(70, 0))
currentPasswordEntry = Entry(changePasswordTab, width=20, font=('Arial', 20), highlightthickness=1,
                             highlightbackground='black', highlightcolor='black')
currentPasswordEntry.grid(row=1, column=1, sticky=S,pady=(0, 6))
changeToPasswordEntry = Entry(changePasswordTab, width=20, font=('Arial', 20), highlightthickness=1,
                              highlightbackground='black', highlightcolor='black')
changeToPasswordEntry.grid(row=2, column=1, sticky=N)
changePasswordButton = Button(changePasswordTab, font=('Arial', 15), text='Сменить пароль',
                              bg='#DCE6F2', activebackground='#DCE6F2', command=change_password)
changePasswordButton.grid(row=2, column=2, sticky=N, padx=10)

notebook.pack(expand=True, fill='both')
window.mainloop()
