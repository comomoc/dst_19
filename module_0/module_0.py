import random
import numpy as np

def game_core(number):
    '''Пишем функцию бинарного поиска для угадывания числа из диапазона от 1 до 100'''
    low_num = 1          # Начальная граница диапазона
    high_num = 101       # Конечная граница диапазона
    predict = 50         # Задаем первое число, как середину диапазона
    count = 1            # Количество попыток
    
    while number != predict: # Проверяем числа изменяя границы диапазона  
        if predict > number:
            high_num = predict
        elif predict < number: 
            low_num = predict
        predict = (low_num + high_num)//2 # Задаем новое число, как середину диапазона
        count += 1
    return(count) # Выход из цикла, если угадали

def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # Фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1,101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f'Алгоритм угадывает число в среднем за {score} попыток')
    return(score)

print(score_game(game_core))
