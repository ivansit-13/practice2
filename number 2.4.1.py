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

dbStudent = sqlite3.connect("Students_of_Empire.db")
sql_dbStudent = dbStudent.cursor()

class Student:
    def __init__(self, name = "НЕТИМЕНИ!", surname = "", patronymic = "", group = "", evaluations = ""):
        self.name = name
        self.surname = surname
        self.patronymic = patronymic
        self.group = group
        self.evaluations = evaluations

# добавляем строки в таблицу
sql_dbStudent.execute(""" CREATE TABLE IF NOT EXISTS student (
    name TEXT,
    

)""")