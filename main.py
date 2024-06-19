import telebot
import random
import os
from telebot import types
# Замените на ваш токен
bot = telebot.TeleBot('7487162703:AAGYFwixRc4J-vAUpb04tgDxDIDLgj8--2o')

# Список комплиментов
compliments = [
    "Ты сегодня потрясающе выглядишь!",
    "Твоя улыбка освещает весь мир.",
    "Ты очень умная и талантливая.",
    "Ты моя опора и поддержка.",
    "Ты самая красивая девушка на свете.",
    "Твоя доброта вдохновляет меня.",
    "Ты заставляешь меня становиться лучше.",
    "Ты всегда знаешь, как поднять мне настроение.",
    "Твоя сила воли восхищает меня.",
    "Ты – моё счастье.",
    "Ты самая нежная и заботливая.",
    "Ты мой лучик света.",
    "Ты удивительная женщина.",
    "Ты моя любовь.",
    "Ты самая лучшая!",
    "Ты такая милая.",
    "Ты вдохновляешь меня каждый день.",
    "Ты делаешь меня самым счастливым человеком.",
    "Ты – моё всё.",
    "Ты – чудо!"
]

# Путь к папке с фотографиями
photo_dir = r"C:\\lera\\photos"  # Укажите путь к папке с фотографиями

def create_keyboard():
    markup = telebot.types.InlineKeyboardMarkup()
    btn1 = telebot.types.InlineKeyboardButton("Комплимент", callback_data="compliment")
    btn2 = telebot.types.InlineKeyboardButton("Когда грустно", callback_data="photo")
    btn3 = telebot.types.InlineKeyboardButton("Оператор", callback_data="contact")
    markup.add(btn1, btn2, btn3)
    return markup

# Начальная команда
@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton("Комплимент", callback_data="compliment")
    btn2 = types.InlineKeyboardButton("Когда грустно", callback_data="photo")
    btn3 = types.InlineKeyboardButton("Оператор", callback_data="contact")
    markup.add(btn1, btn2, btn3)
    bot.send_message(message.chat.id, "Привет! Выбери опцию:", reply_markup=markup)

# Обработка нажатий на кнопки
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "compliment":
        compliment = random.choice(compliments)
        bot.send_message(call.message.chat.id, compliment)
    elif call.data == "photo":
        photo = random.choice(os.listdir(photo_dir))
        photo_path = os.path.join(photo_dir, photo)
        bot.send_photo(call.message.chat.id, photo=open(photo_path, 'rb'))
    elif call.data == "contact":
        bot.send_contact(call.message.chat.id, phone_number="+79191183824", first_name="Hot pupsik")
    markup = create_keyboard()
    bot.send_message(call.message.chat.id, "Выбери следующую опцию:", reply_markup=markup)

# Запуск бота
bot.infinity_polling(timeout=10, long_polling_timeout=5, interval=0.1)
