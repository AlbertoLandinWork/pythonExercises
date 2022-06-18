import time
import os
import random
import unicodedata


def clear():
    os.system('clear')


def word():
    with open("./archivos/data.txt", "r", encoding="UTF-8") as f:
        random_word = random.choice(list(f))
    return random_word


def treatment(word):
    accents = unicodedata.normalize('NFKD', word).encode('ASCII', 'ignore').decode()
    normalized_word = accents.upper()
    normalized_word = normalized_word.rstrip('\n')
    return normalized_word


def interface(treatment):
    len_word = len(treatment)
    display = ['_ ' for i in range(len_word)]
    print('La palabra que vas a adivinar tiene {} letras: '.format(len_word))
    time.sleep(1)
    print('\n')
    time.sleep(1)
    print(''.join(display))


def run():
    clear()
    print('¡Vienvenido al juego del ahorcado!')
    time.sleep(1)
    print('\n')
    normalized_word = treatment(word())
    interface(normalized_word)
    print('\n')
    letter = input('Ingresa una letra para saber si está en la palabra: ')
    letter = letter.upper()

if __name__ == '__main__':
    run()


# find()	Searches the string for a specified value and returns the position of where it was found