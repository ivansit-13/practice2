# Задание 2. Модифицируйте класс Worker из предыдущей задачи, сделайте все его
#  свойства приватными, а для их чтения сделайте методы-геттеры;
# Геттеры (getters) в Python — это методы, которые используются для получения значений закрытых атрибутов объекта.

class Worker:
    def __init__(self, name="name", surname="surname", rate=0, days=0):
        # Добавил двойное подчеркивание "__" перед именами атрибутов делает их “приватными”.
        self.__name = name
        self.__surname = surname
        self.__rate = rate
        self.__days = days

    def defGetSalary(self):
        return print("Зарплата сие человека = ",self.__rate * self.__days)

    def info(self):
        print("____________Приватная информация о персонале_____________")
        print(f"Имя - {self.__name}")
        print(f"Фамилия - {self.__surname}")
        print(f"Ставка - {self.__rate}")
        print(f"Количество отработаных дней - {self.__days}")
        print("_______________________________________________")


men = Worker("Иван", "Петрович", 250, 5)
men.info()
print("______________ЗП___________________")
men.defGetSalary()
