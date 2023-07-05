import random
import time
print('Добро пожаловать в угадайку!')
time.sleep(1)
print('Вам предстоит угадать число от 1 до выбранного вами.')
time.sleep(1)


def ugadaika():
    print('Введите максимальное случайное число')
    number = random.randint(1, int(input()))
    print('А теперь угадывайте число')
    counter = 0
    while True:
        x = int(input())
        if x == number:
            print('Поздравляю, ты угадал!')
            break
        if x < number:
            print('Слишком мало!')
        elif x > number:
            print('Слишком много!')
        counter += 1
    print(f'Ты угадал за {counter + 1} попыток')
    print('Хочешь попробовать ещё раз?')


ugadaika()
while True:
    ans = str(input())
    if ans.lower() == 'yes':
        ugadaika()
    elif ans.lower() == 'no':
        break
    else:
        print('Введите пожалуйста yes или no')
