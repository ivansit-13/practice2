#https://t.me/KasishonBot
import random
import telebot
import requests as rq
import json
import time


def get_dog_image_url():
    response = rq.get("http://api.thedogapi.com/v1/images/search").text
    return json.loads(response)[0]["url"]


def get_cat_image_url():
    response = rq.get("http://api.thecatapi.com/v1/images/search").text
    return json.loads(response)[0]["url"]
def get_Warhammer():
    response = rq.get('https://api-warhammer40k.onrender.com/quote')
    return response.json()
def get_Warhammer2():
    response = rq.get('https://api-warhammer40k.onrender.com/image')
    return response.json()
def CurrencyRu():
    url = 'https://api.exchangerate-api.com/v4/latest/RUB'
    response = rq.get(url)
    return response.json()
def CurrencyUSD():
    url = 'https://api.exchangerate-api.com/v4/latest/USD'
    response = rq.get(url)
    return response.json()

# Словарь для хранения URL анимаций
n = {
    1: "https://media1.tenor.com/m/A8bHpNinW6wAAAAd/for-the-emperor-hammer-and-bolter.gif",
    2: "https://media1.tenor.com/m/RW0497UNqQ8AAAAd/%D1%80%D0%B5%D0%B7%D0%BD%D1%8F-%D0%B7%D0%B0-%D0%B8%D0%BC%D0%BF%D0%B5%D1%80%D0%B0%D1%82%D0%BE%D1%80%D0%B0-%D1%80%D0%B5%D0%B7%D0%BD%D1%8F.gif",
    3: "https://media1.tenor.com/m/mwTjdw-dHg8AAAAd/slap-bet-chisa-iori.gif",
    4: "https://steamuserimages-a.akamaihd.net/ugc/938338536460946383/A4B8C5C7790C5427D55FAEBA30E371EF7EB1505F/?imw=512&amp;imh=288&amp;ima=fit&amp;impolicy=Letterbox&amp;imcolor=%23000000&amp;letterbox=true",
    5: "https://media.tenor.com/DckqsVCpt-0AAAAM/warhammer40k-ultramarines.gif",
    6: "https://itunes.apple.com/app/apple-store/id917932200?pt=39040802&ct=Media1GIFV2&mt=8"
}



# Токен для подключения к Telegram Bot API
token = "Мудл"
bot = telebot.TeleBot(token)

# Создание клавиатуры для взаимодействия с пользователем
keyworld = telebot.types.ReplyKeyboardMarkup()
keyworld.row("ДАЙ МНЕ КОТИКОВ!!")
keyworld.row("ЗА ИМПЕРАТОРА!")
keyworld.row("Ответ на всё.")
keyworld.row("ХОЧУ СОБАЧКУ!")
keyworld.row("ДенсимЧуваки")
keyworld.row("Дa!")
keyworld.row("дай картинку!")
keyworld.row("Курс Рубля")
keyworld.row("Курс Доллара")

last_message_time0 = {}

def can_send_message1(user_id):
    current_time = time.time()
    if user_id not in last_message_time0:
        last_message_time0[user_id] = current_time
        return True
    elif current_time - last_message_time0[user_id] > 3: # 3 секунды
        last_message_time0[user_id] = current_time
        return True
    else:
        return False


last_message_time1 = {}

def can_send_message2(user_id):
    current_time = time.time()
    if user_id not in last_message_time0:
        last_message_time0[user_id] = current_time
        return True
    elif current_time - last_message_time0[user_id] > 3: # 3 секунды
        last_message_time0[user_id] = current_time
        return True
    else:
        return False


@bot.message_handler(commands=['start', 'help'])
def welcome(message):
    bot.send_message(message.chat.id, "Привецтвую земляки!", reply_markup=keyworld)


@bot.message_handler(func=lambda message: True)
def handle_message(message):
    # Обработка запроса
    if message.text == "ДАЙ МНЕ КОТИКОВ!!":
        if can_send_message1(message.chat.id):
            cat_url = get_cat_image_url()
            bot.send_photo(message.chat.id, photo=cat_url)
        else:
            bot.send_message(message.chat.id, "не спамь!жди 3 секунды")
    if message.text == "ХОЧУ СОБАЧКУ!":
        if can_send_message1(message.chat.id):
            cat_url = get_dog_image_url()
            bot.send_photo(message.chat.id, photo=cat_url)
        else:
            bot.send_message(message.chat.id, "не спамь!жди 3 секунды")
    if message.text == "ЗА ИМПЕРАТОРА!" and can_send_message1(message.chat.id):
        bot.send_animation(message.chat.id, n[random.randint(1, 2)])
    if message.text == "Ответ на всё." and can_send_message2(message.chat.id):
        bot.send_animation(message.chat.id, n[3])
    if message.text == "ДенсимЧуваки" and can_send_message2(message.chat.id):
        bot.send_animation(message.chat.id, n[random.randint(4, 6)])
    if message.text == "Дa!":
        warhammer_quote = get_Warhammer()
        bot.send_message(message.chat.id, warhammer_quote.get('quote', 'Нет цитаты'))
    if message.text == "дай картинку!":
        warhammer_image = get_Warhammer2()
        bot.send_photo(message.chat.id, photo=warhammer_image.get('image', ''))
    if message.text == "Курс Рубля":
        curs = CurrencyRu()
        curs = curs['rates']
        dollar_rate = curs.get('USD', 'Недоступно')
        euro_rate = curs.get('EUR', 'Недоступно')
        bot.send_message(message.chat.id, f"Курс рубля:\n1 USD = {dollar_rate} RUB\n1 EUR = {euro_rate} RUB")
    if message.text == "Курс Доллара":
        curs = CurrencyUSD()
        curs = curs['rates']
        RUB_rate = curs.get('RUB', 'Недоступно')
        euro_rate = curs.get('EUR', 'Недоступно')
        bot.send_message(message.chat.id, f"Курс доллара:\n1 RUB = {RUB_rate} RUB\n1 EUR = {euro_rate} USD")

    print(message)  # Вывод информации о сообщении в консоль


# Запуск бота
bot.polling(non_stop=True, interval=0)
