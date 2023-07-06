import random
digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_. '


def create_pass():
    char = ''
    while char == '':
        print('Хотите использовать цифры?')
        ans_dig = input()
        if ans_dig.lower() == 'yes':
            char += digits
        print('Хотите использовать строчные буквы?')
        ans_llet = input()
        if ans_llet.lower() == 'yes':
            char += lowercase_letters
        print('Хотите использовать заглавные буквы?')
        ans_ulet = input()
        if ans_ulet.lower() == 'yes':
            char += uppercase_letters
        print('Хотите использовать знаки пунктуации?')
        ans_punc = input()
        if ans_punc.lower() == 'yes':
            char += punctuation
        if char == '':
            print('Пожалуйста выберите из каких символов хотите создать пароль.')
        else:
            print('Какой длины хотите пароль?')
            length = int(input())
            print('Сколько паролей хотите сгенерировать?')
            amm = int(input())
            for i in range(1, amm + 1):
                _Pass = ''
                for j in range(length):
                    elem = random.choice(char)
                    _Pass += elem
                print(f'Пароль №{i}:')
                print(_Pass)


create_pass()
