import telebot
from telebot import types
from bs4 import BeautifulSoup
import requests
import random


bot = telebot.TeleBot('5069290749:AAFjhEyaaJ4rRUTItyihd_FBTOwiUD-3n-M')


admin1 = '@Yalyk'
admin2 = '@samehadasanemi'


def parser_sp():
    urls = 'https://www.superjob.ru/vakansii/it-internet-svyaz-telekom/'
    r = requests.get(urls)
    soup = BeautifulSoup(r.text, 'html.parser')

    jobs = soup.find_all('div', class_=[
                         '_1M4pN _1O2dw _6kSO2 fmJDo', '_1M4pN _2SZOi _3NbN3 _3iACx _3JtJ8 fmJDo'])
    sp = [c.text for c in jobs]
    sp_izmen = []
    i = 0
    sch = len(sp)
    while sch > i:
        sp_izmen.append(sp[0] + '\n' + sp[1])
        sp.pop(0)
        sp.pop(0)
        sch = sch - 2
    random.shuffle(sp_izmen)
    z = sp_izmen[0]
    return z


# данный декоратор start отвечает за команду /startв меню бота
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item2 = types.KeyboardButton('сообщить об ошибке')
    item3 = types.KeyboardButton('связь с администрацией')
    markup.add(item2, item3)
    bot.send_message(message.chat.id, 'Привет, {0.first_name}! Cнизу предоставлен список актуальных кнопок для взаимодейтсвия с ботом!\nБот создан в рамках хакатона "Поколение IT" на тему "Поиск работы для молодых профессионалов города Москвы"'.format(
        message.from_user), reply_markup=markup)


# данный декоратор questionarisотвечает за команду /questionaris в меню бота
@bot.message_handler(commands=['questionaris'])
def questionaris(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('откликнутся')
    item2 = types.KeyboardButton('следующая вакансия')
    markup.add(item1, item2)
    bot.send_message(message.chat.id, 'Привет, {0.first_name}! Cнизу предоставлен список актуальных кнопок для взаимодейтсвия с ботом!'.format(
        message.from_user), reply_markup=markup)


# данный декоратор help отвечает за команду /help в меню бота
@bot.message_handler(commands=['help'])
def help(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item3 = types.KeyboardButton('связь с администрацией')
    item4 = types.KeyboardButton('список команд')
    item5 = types.KeyboardButton('сообщить об ошибке')
    markup.add(item3, item4, item5)
    bot.send_message(message.chat.id, 'Привет, {0.first_name}!Снизу предоставлены команды для помощи пользователю!'.format(
        message.from_user), reply_markup=markup)


@bot.message_handler(content_types=['text'])
def bot_messages(message):
    if message.chat.type == 'private':
        if message.text == 'связь с администрацией':
            bot.send_message(
                message.chat.id, f"Почта для сотрудничества: koksharov.andrew23@yandex.ru\nblazeman2121@gmail.com")
        elif message.text == 'откликнутся':
            bot.send_message(message.chat.id, "В разработке")
        elif message.text == 'следующая вакансия':
            bot.send_message(message.chat.id, parser_sp())
        elif message.text == 'список команд':
            bot.send_message(
                message.chat.id, 'Весь список актуальынх команд:\n/start\n/help\n/questionaris')
        elif message.text == 'сообщить об ошибке':
            bot.send_message(
                message.chat.id, f'Администрация:\n{admin1}\n{admin2}')


while True:  # создание бесконечного цикла, который отвечает за то, чтобы бот не прекращал свою работу
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        print(e)
        bot.polling(none_stop=True)