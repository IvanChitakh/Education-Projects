import random
import Dictionary
import Stages


def play():
    while True:
        hid_word = random.choice(Dictionary.Dict())
        tries = 6
        print('Давайте сыграем в Виселицу.')
        print(Stages.display_hangman(tries))
        word_completion = []
        temp_word = ['_' for _ in range(len(hid_word))]  #Временная переменная для замены '_' в слове
        for _ in hid_word:
            word_completion += '_'
        print(f'В слове {len(word_completion)} букв')
        print(''.join(word_completion))
        while True:
            print('Введите букву или слово целиком.')
            ans = input().upper()
            if len(ans) == 1:    #Действия которые выполняются, если была введена буква
                if ans in hid_word:
                    for i in range(len(hid_word)):
                        if hid_word[i] == ans:
                            temp_word[i] = ans
                    word_completion = temp_word
                else:
                    print('Такой буквы нет.')
                    tries -= 1
                print(''.join(word_completion))
            elif len(ans) > 1:    #Действия которые выполняются, если было введено слово
                if ans == hid_word:
                    print('Ты выиграл!!!')
                    break
                else:
                    print('Такого слова нет.')
                    tries -= 1
            if ''.join(word_completion) == hid_word:    #Проверка, все ли буквы совпадают с загаданным словом
                print('Ты выиграл!!!')
                break
            if tries == 0:
                print('Ты проиграл!')
                print(f'Загаданное слово было: {hid_word}')
                break
            else:
                print(Stages.display_hangman(tries))
        print('Хотите сыграть еще раз?')
        print('Введите что-угодно если да, а если нет, то введите "n"')
        req = input().lower()
        if req == 'n':
            break


play()
