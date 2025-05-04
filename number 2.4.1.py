#https://yandex.ru/video/preview/855802827772808546
# Задание 1.
# Разработайте приложение по работе со студентами. Приложение
# должно хранить данные о студентах в базе данных. Сущность
# студента должна описываться в виде класса, у которого будут
# следующие поля:
# 1) Имя
# 2) Фамилия
# 3) Отчество
# 4) Группа
# 5) Оценки(массив из 4 элементов)
# В приложении должен быть следующий функционал:
# 1) Добавление нового студента
# 2) Просмотр всех студентов
# 3) Просмотр одного студента, включая его средний балл
# 4) Редактирование студента
# 5) Удаление студента
# 6) Просмотр среднего балла студентов у конкретной группы

import sqlite3

# Подключаемся к базе данных "StudentsOfEmpire.db"
dbStudent = sqlite3.connect("StudentsOfEmpire.db")
# Создаем курсор для выполнения SQL-запросов
sql_dbStudent = dbStudent.cursor()

class Student:
    def __init__(self, name = "НЕТИМЕНИ!", surname = "НЕТФАМИЛИИ", patronymic = "НЕТОТЧЕСТВА", group = "НЕТГРУППЫ", evaluations = "НЕТОЦЕНОК"):
        self.name = name
        self.surname = surname
        self.patronymic = patronymic
        self.group = group
        self.evaluations = evaluations

    def info_name(self):
        return self.name
    def info_surname(self):
        return self.surname
    def info_patronymic(self):
        return self.patronymic
    def info_group(self):
        return self.group
    def info_evaluations(self):
        return self.evaluations

# Создаем таблицу "student", если она еще не существует.
# Обратите внимание на использование кавычек вокруг "group", т.к. это зарезервированное слово в SQL.
sql_dbStudent.execute(""" CREATE TABLE IF NOT EXISTS student (
    name TEXT,
    surname TEXT,
    patronymic TEXT,
    "group" TEXT,
    evaluations TEXT
)""")
# Фиксируем изменения в базе данных (сохраняем изменения)
dbStudent.commit()

# ЭТО ДЛЯ ВЫХОДА И ВХОДА В ПРОГРАММУ
print("Здравствуйте в Базе данных студентов:","\n","Правила:","\n",
      1, "- начать работу", "\n",
      0, "- выход","\n")
exit_code = int(input("Вы выбрали: "))
while exit_code != 0:
    print("Здравствуйте в Базе данных студентов:", "\n", "Правила:", "\n",
          1, "- ДОБАВИТЬ НОВОГО СТУДЕНТА", "\n",
          2, "- ПРОСМОТР ВСЕХ СТУДЕНТОВ", "\n",
          3, "- ПРОСМОТР 1 СТУДЕНТА ВКЛЮЧАЯ ЕГО СР.БАЛ", "\n",
          4, "- РЕДАКТИРЫВАНИЕ СТУДЕНТА", "\n",
          5, "- УДАЛЕНИЕ СТУДЕНТА", "\n",
          6, "- ПРОСМОТР КОНКРЕТНЫХ СТУДЕНТОВ ОПРЕДЕЛЁННОЙ ГРУППЫ", "\n",
          412, "- ПОСХАЛОЧКА", "\n",
          0, "- выход", "\n")
    choice = int(input("Вы выбрали: "))
    if choice == 1:
        # Создаем экземпляр класса Student с дефолтными значениями.
        Student1 = Student()
    elif choice == 2:
        # Выводим данные таблицы.
        for i in sql_dbStudent.execute("SELECT * FROM student"):
            print(i)
    elif choice == 3:
        pass
    elif choice == 4:
        pass
    elif choice == 5:
        pass
    elif choice == 6:
        pass

    # Если запрос вернул None (пустой результат), значит, таблица пуста.
    sql_dbStudent.fetchone()
    # Добавляем нового студента с дефолтными значениями в таблицу.
    # Используем параметризованный запрос (знаки вопроса), чтобы избежать SQL-инъекций.
    sql_dbStudent.execute(f"INSERT INTO student VALUES (?, ?, ?, ?, ?)",(Student1.info_name(),Student1.info_surname(),Student1.info_patronymic(),Student1.info_group(),Student1.info_evaluations()))
    # Фиксируем изменения (сохраняем добавление).
    dbStudent.commit()

    # Выводим данные таблицы.
    for i in sql_dbStudent.execute("SELECT * FROM student"):
        print(i)


    # ЭТО ДЛЯ ВЫХОДА И ПРОДОЛЖЕНИЯ РАБОТЫ С ПРОГРАММОЙ, ДА Я ЗАБЫЛ ОТЖАТЬ CAPS_LOOK
    print("Здравствуйте в Базе данных студентов:", "\n", "Правила:", "\n",
          1, "- начать работу", "\n",
          0, "- выход", "\n")
    exit_code = int(input("Вы выбрали: "))

# Закрываем соединение с базой данных. Это важно делать!
dbStudent.close()