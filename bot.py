import telebot
from pandas import read_excel
bot = telebot.TeleBot('')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, я подскажу какие у тебя пары!'
                                      ' Делай запрос в виде: Пары пн')


def el(x, week, sday):
    for index, item in enumerate(sday):
        if x == item:
            return week[index]


@bot.message_handler(content_types=['text'])
def send_text(message):
    message.text = message.text.lower()
    if message.text == 'привет':
        bot.send_sticker(message.chat.id, 'CAADAgADRRcAAishBQABL-BwYvI9TAQWBA')
    elif 'пары' in message.text:
        # find your sheet name at the bottom left of your excel file and assign
        # it to sheet_name
        my_sheet = 'INBO-01-19 - INBO-01-19'
        file_name = 'tm.xlsx'  # name of your excel file
        df = read_excel(file_name, sheet_name=my_sheet)

        day = df['INBO-01-19'].tolist()
        num = df['Unnamed: 1'].tolist()
        pair = df['Unnamed: 2'].tolist()
        hall = df['Unnamed: 3'].tolist()
        sday = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
        week = ['пн', 'вт', 'ср', 'чт', 'пт', 'сб']

        day = [el(x, week, sday) for x in day]

        for item in week:
            if item in message.text:
                ray = ''
                for index, item1 in enumerate(day):
                    if item1 == item:
                        ray += f'{num[index]} пара - {pair[index]} \n'
                bot.send_message(message.chat.id, ray)

    elif message.text == 'пока':
        bot.send_message(message.chat.id, 'Прощай, создатель')


bot.polling()
