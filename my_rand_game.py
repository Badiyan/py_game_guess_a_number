import random
from art import text2art

TITLE = '_GUESS\n ___A__ \n NUMBER'
SUBTITLE = '_____THE GAME_____'
START_STRINGS = ['Привет, давай сыграем игру Угадай число?',
                             'Хочешь попытаться угадать число?',
                             'Играть игру угадай число?',
                             'Йо, ты хочешь сыграть игру Угадай число?',
                             'Ммм, хочешь угадать число?']
NEG_STRING = ['ЕХ, жаль',
              'ПРиходи еще',
              'А, ну пока']

attempt = 0

def title_art():
    print(text2art(TITLE, font='block', chr_ignore=True))
    print(text2art(SUBTITLE))

def get_name():
    user_name =''
    while user_name == '':
        user_name = input('Введите свое имя или никнейм:')
    else:
        return user_name

def guess():

def add_result(user_name, result):
    file = open('results.csv', 'a')
    file.write('\n'+user_name+' - '+result)
    file.close()

def show_results():
    file = open('results.csv', 'r')
    print(text2art('Players:\n'),file.read())

def start_game():
    title_art()
    start_string = random.choice(START_STRINGS)
    neg_string = random.choice(NEG_STRING)
    if input(start_string, 'да/не') == 'да':
        user_name = get_name()
        result = guess()
        show_results()
        add_result(user_name, result)
    else
        print(neg_string)
        if input('Показать результаты?', 'да/не') == 'да':
            show_results()
        break

start_game()