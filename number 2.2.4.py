# Задание 4. Описать класс, реализующий счетчик, который может увеличивать или
# уменьшать свое значение на единицу. Предусмотреть инициализацию счетчика со
# значением по умолчанию и произвольным значением. Счетчик имеет два метода:
# увеличения и уменьшения, — и свойство, позволяющее получить его текущее состояние.
# Написать программу, демонстрирующую все возможности класса;
#А? Чё? Я ничё не понял

from random import randint

class Counter:
    def __init__(self,number):
        self.number = number
    def increase_number(self):
        self.number += 1
    def reduce_number(self):
        self.number -= 1
    def info(self):
        print(f"Ваше число на данный момент: {self.number}")
    def randomNumber(self):
        self.number = randint(1,100)
    def default(self,number):
        self.number = number
x = int(input("Введите ваше число для счётчика "))
number = Counter(x)
exit_program = int(input("Если 1 - то вы хотите начать работу с счётчиком, иначе 0 - "))
while exit_program == 1:
    print("Правила счётчика","\n",
          "1 - Счётчик+","\n",
          "2 - Счётчик-","\n",
          "3 - Счётчик информация на текущий момент","\n",
          "4 - Назначить рандомное значение", "\n",
          "5 - Назначить число по умолчанию", "\n",
          "0 - Выход")
    a = int(input())
    if a == 1:
        number.increase_number()
        number.info()
    elif a == 2:
        number.reduce_number()
        number.info()
    elif a == 3:
        number.info()
    elif a == 4:
        number.randomNumber()
        number.info()
    elif a == 5:
        number.default(x)
        number.info()
    elif a == 0:
        exit_program = int(input("Вы точно уверенны что хотите выйти? 1 - нет|| 0 - да "))