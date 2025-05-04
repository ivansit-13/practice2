# Задание 2. Модифицируйте класс Worker из предыдущей задачи, сделайте все его
#  свойства приватными, а для их чтения сделайте методы-геттеры;

class Worker:
    def __init__(self, name="name", surname="surname", rate=0, days=0):
        # Добавил двойное подчеркивание "__" перед именами атрибутов делает их “приватными”.
        self.__name = name
        self.__surname = surname
        self.__rate = rate
        self.__days = days

    # Геттеры для доступа к приватным атрибутам
    def getter_name(self):
        return print(f"Имя - {self.__name}")

    def getter_surname(self):
        return print(f"Фамилия - {self.__surname}")

    def getter_rate(self):
        return print(f"Ставка - {self.__rate}")

    def getter_days(self):
        return print(f"Количество отработаных дней - {self.__days}")

    def getter_salary(self):
        return self.__rate * self.__days

    def info(self):
        print("____________информация о персонале_____________")
        print(f"Имя - {self.__name}")
        print(f"Фамилия - {self.__surname}")
        print(f"Ставка - {self.__rate}")
        print(f"Количество отработаных дней - {self.__days}")
        print("_______________________________________________")


men = Worker("Иван", "Петрович", 250, 5)
men.info()
print("______________ЗП___________________")
print("Зарплата сие человека = ", men.getter_salary())

print("____________Приватная информация о персонале_____________")
men.getter_name()
men.getter_surname()
men.getter_rate()
men.getter_days()
print("_______________________________________________")