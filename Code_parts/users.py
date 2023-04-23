from lock import *


class Users:
    def __init__(self):
        self.user_name = ""
        self.login_list = []
        try:
            login_file = open("user.txt", "a")
            login_file.close()
        except:
            s = ""
        try:
            login_file = open("user.txt", "r")
            try:
                for s in login_file:
                    self.login_list.append(list(s.split()))
            finally:
                login_file.close()
        except:
            s = ""

    # Проверка на наличие регистрации пользователя
    def add_test(self, login):
        for s in self.login_list:
            if s[0] == login:
                return 1
        return 0

    # добавление пользователя в список
    def add(self, login, password):
        try:
            login_file = open("user.txt", "a")
            try:
                login_file.write(login + " " + password + " " + "\n")
            finally:
                login_file.close()
        except:
            s = ""

    def correct_login_test(self, login):
        for s in login:
            if ord(s) < 65:
                return 1
            elif ord(s) > 90 and ord(s) < 97:
                return 1
        return 0

    def correct_password_test(self, password):
        for s in password:
            if ord(s) == 32:
                return 1
        return 0

    # регистрация, вызов функций-проверок, вызов функции добавления при корректных данных
    def sign_up(self, login, password):
        global locker1
        error_flag = 0
        if self.correct_login_test(login) + self.correct_password_test(password) > 0:
            return 1
        else:
            if self.add_test(login) > 0:
                return 2
            else:
                lock_password = locker1.lock(password)
                self.add(login, lock_password)
        return 0

    def search(self, login):
        n = len(self.login_list)
        for i in range(n):
            if self.login_list[i][0] == login:
                return i
        return -1

        # вход, поиск логина в списке, проверка пароля

    def sign_in(self, login, password):
        global locker1
        error_flag = 0
        login_index = self.search(login)
        if login_index == -1:
            return 1
        else:
            unlock_password = locker1.unlock(self.login_list[login_index][1])
            if unlock_password == password:
                return 0
            else:
                return 2


# следующие функции для команд. выносим из класса


# Смена пароля. для смены пароля пользователь должен указать текущий пароль. Проверку на корректность логина можно было и не проводить
def change_password(password, new_password):
    global users1
    global login_file
    #global current_password
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
            print("Успешная смена пароля")
        else:
            print("Неверный пароль")


# метод sign_up_message вызываем для регистрации, sign_up_message - для входа, все принты меняем на вывод в соответствующее текстовое поле
# print("Логин. Не дожен содержать цифры, спецсимволы, пробелы")
# print("Пароль. Не дожен содержать пробелы")
# эти правила ввода нужно будет куда-то добавить
def sign_up_message(login, password):
    global users1
    out_test = users1.sign_up(login, password)
    if out_test == 0:
        print("Успешная регистрация")
    elif out_test == 1:
        print("Некорректный логин или пароль")
    elif out_test == 2:
        print("Пользователь уже существует")


def sign_in_message(login, password):
    global users1
    in_test = users1.sign_in(login, password)
    if in_test == 0:
        print("Успешный вход")
        users1.user_name = login
        # здесь будет переход на основную форму
    elif in_test == 1:
        print("Пользователь не зарегистрирован")
    elif in_test == 2:
        print("Неверный пароль")


locker1 = Locker()
users1 = Users()

