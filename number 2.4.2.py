# Задание 2.
# Разработайте приложение „I love drink“, со следующим
# функционалом:
# 1) Учет напитков:
# 1.1) Хранение данных об алкогольных напитках и ингредиентах
# 1.2) Учет остатков на складе
# 2) Управление коктейлями:
# 2.1) Хранение данных о коктейлях(название,
# крепость(автоматический расчет исходя из крепости алкогольных
# напитков), состав, цена)
# 3) Операции
# 3.1) Продажа коктейлей и алкогольных напитков
# 3.2) Пополнение запасов
# В приложении должна использоваться база данных для хранения
# информации.
#
#!!!!!!!!!!Программа очень чувствительна к правильному написанию текстов!!!!!!!!!!!!!!!!!
#
import sqlite3

class DataBas:
    def __init__(self, db_name="ILoveDrink.db"):
        self.db_name = db_name
        self.connection = None
        self.cursor = None
        self.connect_db()
        self.create_table()

    def connect_db(self):
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()

    def create_table(self):
        self.cursor.execute(""" CREATE TABLE IF NOT EXISTS ingredients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE,
            quantity REAL,
            unit TEXT
        )""")
        self.cursor.execute(""" CREATE TABLE IF NOT EXISTS drinks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE,
            alcohol_strength,
            quantity REAL,
            unit TEXT
        )""")
        self.cursor.execute(""" CREATE TABLE IF NOT EXISTS cocktails (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE,
            structure TEXT,
            alcohol_strength REAL,
            price REAL
        )""")
        self.connection.commit()

    def close(self):
        if self.connection:
            self.connection.close()

    def add_ingredients(self, name, quantity, unit):
        self.cursor.execute("""
        INSERT OR REPLACE INTO ingredients (name, quantity, unit) VALUES (?, ?, ?)""", (name, quantity, unit))
        self.connection.commit()

    def add_drink(self, name,alcohol_strength, quantity, unit):
        self.cursor.execute("""
        INSERT OR REPLACE INTO drinks (name,alcohol_strength, quantity, unit) VALUES (?, ?, ?, ?)""", (name, alcohol_strength, quantity, unit))
        self.connection.commit()

    def add_cocktail(self,name, structure,alcohol_strength, price):
        self.cursor.execute("""
                INSERT OR REPLACE INTO cocktails (name,structure, alcohol_strength, price) VALUES (?, ?, ?, ?)""",
                            (name, structure, alcohol_strength, price))
        self.connection.commit()

    def all_drinks(self):
        print("_________________________Напитки_________________________")
        self.cursor.execute("SELECT * FROM drinks")
        drinks = self.cursor.fetchall()
        if drinks:
            for j in drinks:
                print(j)
        else:
            print("А может гранату бросить? -Так ведь нет никого...")

    def all_ingredients(self):
        print("________________________Ингредиенты_______________________")
        self.cursor.execute("SELECT * FROM ingredients")
        ingredients = self.cursor.fetchall()
        if ingredients:
            for j in ingredients:
                print(j)
        else:
            print("А может гранату бросить? -Так ведь нет никого...")

    def all_cocktails(self):
        print("________________________Коктейли_______________________")
        self.cursor.execute("SELECT * FROM cocktails")
        cocktail = self.cursor.fetchall()
        if cocktail:
            for j in cocktail:
                print(j)
        else:
            print("А может гранату бросить? -Так ведь нет никого...")

    def sell_drinks(self, choice_drinks,name,quantity):
        self.cursor.execute(f"SELECT quantity FROM {choice_drinks} WHERE name=?", (name,))
        row = self.cursor.fetchone()
        if row:
            current_quantity = row[0]
            if current_quantity >= quantity:
                new_quantity = current_quantity - quantity
                self.cursor.execute(f"UPDATE {choice_drinks} SET quantity=? WHERE name=?", (new_quantity, name))
                self.connection.commit()
        else:
            print("Или вам не хватает или такого продукта у нас нет(")

    def add_drinks(self, choice_drinks,name,quantity):
        self.cursor.execute(f"SELECT quantity FROM {choice_drinks} WHERE name=?", (name,))
        row = self.cursor.fetchone()
        if row:
            current_quantity = row[0]
            if current_quantity >= quantity:
                new_quantity = current_quantity + quantity
                self.cursor.execute(f"UPDATE {choice_drinks} SET quantity=? WHERE name=?", (new_quantity, name))
                self.connection.commit()
        else:
            print("Такого продукта у нас нет(")



ILD_manadger = DataBas()
alcohol_strength = {"Водка": 36, "Квас": 2, "Светлое Пиво": 4, "Крепкое Пиво": 8, "Джин-тоник": 7,
                    "Шампанское": 9, "Вино": 9, "Портвейн": 17, "Настойка сладкая": 18, "Настойка горькая": 30,
                    "Ликер": 15, "Бренди": 38, "Водка русская": 40, "Коньяк": 45, "Джин": 35, "Текила": 35, "Чача": 45,
                    "Виски": 40, "Ром": 65, "Самогон": 80, "Абсент": 75}

print("_Здравствуйте вы в приложении 'Я люблю напитки'_", "\n", "Правила:", "\n",
        1, "- начать работу", "\n",
        0, "- выход", "\n")

exit_code = int(input("Вы выбрали: "))

while exit_code != 0:
    print("\nЗдравствуйте вы в приложении 'Я люблю напитки':")
    print("1 - Добавить ингредиент")
    print("2 - Добавить напиток")
    print("3 - Создать коктейль")
    print("4 - Продать товар")
    print("5 - Посмотреть остатки")
    print("6 - Пополнить запасы")
    print("0 - Выйти")

    choice = int(input("Вы выбрали: "))
    if choice == 1:
        name = input("Введите название ингредиента: ")
        quantity = input("Введите количество ингредиента в  миллилитрах: ")
        unit = "мил."
        ILD_manadger.add_ingredients(name,quantity, unit)
    elif choice == 2:
        name = input("Введите название напитка: ")
        quantity = input("Введите количество напитка в миллилитрах: ")
        unit = "мил."
        alcohol_strength_n = 10
        for key, value in alcohol_strength.items():
            if name == key:
                alcohol_strength_n = alcohol_strength[key]
                ILD_manadger.add_drink(name, alcohol_strength_n, quantity, unit)
                break
    elif choice == 3:
        # Крепость коктейля можно вычислить по формуле: ABV
        # коктейля = ∑(Объём каждого алкогольного ингредиента × Крепость ингредиента) / Общий объём коктейля × 100.
        quantity_volume = 0
        alcohol_strength_volume = 0
        name = input("Введите название коктейля: ")
        price = float(input("Введите цену коктейля: "))
        print("Введите состав коктейля. Для завершения введите 'стоп'.")
        structure = []
        while True:
            alcohol_strength_n = 0
            print("Вот список имеющихся ингредиентов и алкогольных напитков")
            ILD_manadger.all_drinks()
            ILD_manadger.all_ingredients()
            ing_name = input("Ингредиент что вы хотите добавить: ")
            for key, value in alcohol_strength.items():
                if ing_name == key:
                    alcohol_strength_n = alcohol_strength[key]
                    break
            if ing_name.lower() == 'стоп':
                break
            amount = float(input("Количество(миллилитры): "))
            quantity_volume += amount
            alcohol_strength_volume += amount * alcohol_strength_n
            structure.append((ing_name, amount))
        alcohol_strength_cocktail = alcohol_strength_volume/quantity_volume
        ILD_manadger.add_cocktail(name, str(structure),alcohol_strength_cocktail, price)
    elif choice == 4:
        print("Что вы хотите продать:")
        print("1 - ингредиент")
        print("2 - напиток")
        print("3 - коктейль")
        choice_drinks = int(input("Ваш выбор - "))
        if choice_drinks == 1:
            choice_drinks = "ingredients"
            ILD_manadger.all_ingredients()
        elif choice_drinks == 2:
            choice_drinks = "drinks"
            ILD_manadger.all_drinks()
        elif choice_drinks ==3:
            choice_drinks = "cocktails"
            ILD_manadger.all_cocktails()
        else:
            print("Не правильно, попробуйте ещё раз")
        name = input("Название: ")
        quantity = float(input("Количество: "))
        ILD_manadger.sell_drinks(choice_drinks,name,quantity)
    elif choice == 5:
        ILD_manadger.all_ingredients()
        ILD_manadger.all_drinks()
        ILD_manadger.all_cocktails()
        print("_________________________________________________________")
    elif choice == 6:
        print("Что вы хотите пополнить:")
        print("1 - ингредиент")
        print("2 - напиток")
        print("3 - коктейль")
        choice_drinks = int(input("Ваш выбор - "))
        if choice_drinks == 1:
            choice_drinks = "ingredients"
            ILD_manadger.all_ingredients()
        elif choice_drinks == 2:
            choice_drinks = "drinks"
            ILD_manadger.all_drinks()
        elif choice_drinks == 3:
            choice_drinks = "cocktails"
            ILD_manadger.all_cocktails()
        else:
            print("Не правильно, попробуйте ещё раз")
        name = input("Название: ")
        quantity = float(input("Количество: "))
        ILD_manadger.add_drinks(choice_drinks, name, quantity)
    elif choice == 0:
        break
    else:
        print("Некорректный выбор. Пожалуйста, выберите номер из меню.")

ILD_manadger.close()
print("Программа завершена. Или нет...")
