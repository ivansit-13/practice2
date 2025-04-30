# Задание 2. Модифицируйте класс Worker из предыдущей задачи, сделайте все его
#  свойства приватными, а для их чтения сделайте методы-геттеры;
# Геттеры (getters) в Python — это методы, которые используются для получения значений закрытых атрибутов объекта.

class Worker:
    def __init__(self, name="name", surname="surname", rate=0, days=0):
        self.__name = name
        self.__surname = surname
        self.__rate = rate
        self.__days = days

    def get_name(self):
        return self.__name

    def get_surname(self):
        return self.__surname

    def get_rate(self):
        return self.__rate

    def get_days(self):
        return self.__days

    def get_salary(self):
        return self.__rate * self.__days

    def info(self):
        print("____________Информация о персонале_____________")
        # Добавил двойное подчеркивание "__" перед именами атрибутов делает их “приватными”.
        print(f"Имя - {self.__name}")
        print(f"Фамилия - {self.__surname}")
        print(f"Ставка - {self.__rate}")
        print(f"Количество отработаных дней - {self.__days}")
        print("_______________________________________________")


men = Worker("Иван", "Петрович", 250, 5)
men.info()
print("______________ЗП___________________")
print("Зарплата сие человека =", men.get_salary())
print("_______________________________________________")
print("_______________Пример использования геттеров__________________")
print("Имя - ", men.get_name())
print("Фамилия - ", men.get_surname())
print("Ставка - ", men.get_rate())
print("Количество отработаных дней - ", men.get_days())
print("_______________________________________________")