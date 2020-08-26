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
    attempt = 0
    guess = -1
    secret = random.randint(1, 100)
    while guess != secret:
        guess_string = input('Угадай загаданное число: ')
        try:
            guess = int(guess_string)
        except:
            continue
        attempt += 1
        if guess < secret:
            print('Я загадал число больше, попробуй еще раз.')
        elif guess > secret:
            print('Я загадал число меньше, попробуй еще раз.')
    return attempt

def add_result(user_name, result):
    file = open('results.csv', 'a',  encoding='utf-8')
    file.write('\n'+user_name+' - '+str(result))
    file.close()

def show_results():
    file = open('results.csv', 'r',  encoding='utf-8')
    print(text2art('Players:\n'),file.read())

def start_game():
    title_art()
    start_string = random.choice(START_STRINGS)
    neg_string = random.choice(NEG_STRING)
    if input(start_string+' (да/не) \n') == 'да':
        user_name = get_name()
        result = guess()
        print('Поздравляю, ты угадал число за {} попытки(ок)'.format(result))
        add_result(user_name, result)
        show_results()
    else:
        print(neg_string)
        if input('Показать результаты?'+' (да/не) \n') == 'да':
            show_results()
        else:
            exit()

start_game()