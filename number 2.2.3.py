# Задание 3. Создайте класс с двумя свойствами для хранения целых чисел. Добавить
# метод для вывода на экран и метод для изменения этих чисел. Добавить метод, который
# находит сумму значений этих чисел, и метод который находит наибольшее значение из
# этих чисел. Написать программу, демонстрирующую все возможности класса;

class Numbers:
    def __init__(self, number1 = 0, number2 = 0):
        self.number1 = number1
        self.number2 = number2

    def info(self):
        print(f"Число 1 = {self.number1}")
        print(f"Число 2 = {self.number2}")

    def changes_numbers(self,number1,number2):
        self.number1 = number1
        self.number2 = number2

    def sum_numbers(self):
        return print("Сумма этих чисел = ", self.number1+self.number2)

    def The_bigger_NAMBEEERS(self):
        if self.number1 == self.number2:
            return print("Они равны")
        elif self.number2 > self.number1:
            return print("2 чило больше 1")
        else:
            return print("1 чило больше 2")

numbers = Numbers(2,3)
numbers.info()
numbers.sum_numbers()
numbers.The_bigger_NAMBEEERS()
print()
numbers.changes_numbers(4,5)
numbers.info()
numbers.sum_numbers()
numbers.The_bigger_NAMBEEERS()
