import telebot
import datetime
import xlovo as xl
from telebot import types
from random import randint

# TOKEN =
GRN = '🟩'
YLW = '🟨'
GRY = '⬛'
bot = telebot.TeleBot(TOKEN)
keymsgs = ['Новая игра', 'Как играть', 'Слово дня', 'Предложить слово']

@bot.message_handler(commands=['start'])
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    newgame_btn = types.KeyboardButton(keymsgs[0])
    howto_btn = types.KeyboardButton(keymsgs[1])
    daily_btn = types.KeyboardButton(keymsgs[2])
    addword_btn = types.KeyboardButton(keymsgs[3])
    markup.add(newgame_btn, howto_btn, daily_btn, addword_btn)

    bot.send_message(message.chat.id,'<b>Добро пожаловать в игру XЛОВО!</b>', parse_mode='html', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def parse_text(message):
    if message.text == keymsgs[1]:
        bot.send_message(message.chat.id, f'<b>Как играть</b>:\n'
                                          f'1. Я загадаю существительное в ед.ч. из 5 букв. Твоя задача - отгадать его за 6 попыток или меньше.\n'
                                          f'2. Введи существительное в ед.ч. из 5 букв, чтобы попробовать отгадать загаданное слово.\n'
                                          f'3. Я отвечу на твое предположение следующим образом:\n'
                                          f'- если буква в твоем слове и буква в загаданном слове совпадают, я выделю её зеленым: {GRN}\n'
                                          f'- если буква в твоем слове есть в загаданном слове, но она стоит не на своем месте, я выделю её желтым: {YLW}\n'
                                          f'- если буквы из твоего слова нет в загаданом слове, я выделю её серым: {GRY}.\n\n'
                                          f'<i>Пример 1.</i> Загадано слово ГОРКА.\n'
                                          f'😀: КОФТА\n'
                                          f'🤖: {xl.guessreply(xl.checkword("КОФТА","ГОРКА"))}\n'
                                          f'😀: кОкОС\n'
                                          f'🤖: {xl.guessreply(xl.checkword("кОкОС", "ГОРКА"))}\n'
                                          f'<i>Пример 2.</i> Загадано слово БЕРЕТ.\n'
                                          f'😀: Зелье\n'
                                          f'🤖: {xl.guessreply(xl.checkword("Зелье","БЕРЕТ"))}\n\n'
                                          f'Если бот не узнает какое-то слово, а должен, то предложи добавить это слово, написав "Предложить слово".\n'
                                          f'Ну что, поиграем? 😉', parse_mode='html')
    elif message.text == keymsgs[0]:
        guessnum = 0
        allguesses = ''
        answer = xl.getanswer()
        print(answer)
        bot.send_message(message.chat.id, 'Поехали! Слово загадано.')
        guessing(message, guessnum, answer, allguesses)
    elif message.text == keymsgs[2]:
        guessnum = 0
        allguesses = ''
        answer = xl.getanswer(gametype='daily')
        print(answer)
        bot.send_message(message.chat.id, f'Поехали! Слово дня {datetime.date.today()} загадано.')
        guessing(message, guessnum, answer, allguesses)
    elif message.text == keymsgs[3]:
        bot.send_message(message.chat.id, 'Пришли мне слово, которое ты хочешь добавить. Мы проверим его и добавим в игру, если все в порядке.')
        bot.register_next_step_handler(message, adding)

def guessing(message, guessnum, answer, allguesses):
    if guessnum < 6:
        bot.send_message(message.chat.id, f'Попыток осталось: {6 - guessnum}')
        bot.register_next_step_handler(message, newguess, guessnum, answer, allguesses)
    else:
        bot.send_message(message.chat.id, f'Извини! Попытки кончились. Правильный ответ: {answer}.')

def newguess(message, guessnum, answer, allguesses):
    global keymsgs
    if message.text not in keymsgs:
        checklist = xl.checkword(message.text, answer)
        if checklist == []:
            bot.send_message(message.chat.id, f'Пожалуйста, пришли допустимое слово из 5 букв.')
            guessing(message, guessnum, answer, allguesses)
        else:
            guessnum += 1
            allguesses += f'{message.text.upper()}\n{xl.guessreply(checklist)}\n'
            bot.send_message(message.chat.id, allguesses)
            if checklist == [2, 2, 2, 2, 2]:
                bot.send_message(message.chat.id, f'Поздравляю, ты победил! Ответ {answer.upper()} отгадан за {guessnum} попыток.')
                bot.register_next_step_handler(message, parse_text)
            else:
                guessing(message, guessnum, answer, allguesses)
    else:
        parse_text(message)

def adding(message):
    if xl.addword(message.text):
        bot.send_message(message.chat.id, f'Спасибо! Слово {message.text.upper()} предложено.')
    else:
        bot.send_message(message.chat.id, f'Слово не соответствует правилам игры или уже добавлено.')


bot.polling(non_stop=True)
