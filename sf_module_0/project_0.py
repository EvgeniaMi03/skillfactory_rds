import numpy as np
#Компьютер загадывает целое число от 1 до 100
number = np.random.randint(1,101)

def game_v3(number):
    count = 0
    i = 1
    j = 100    
    while True:
        count += 1
        predict = (i+j)//2
        if number == predict:
            break
        elif number > predict:
            i = predict+1
        elif number < predict:
            j = predict-1
    return(count)

count1=game_v3(number)
print (f"Вы угадали число {number} за {count1} попыток.")

# Добавила функцию: Повторим 1000 раз, чтоб понять в среднем, насколько быстро решает задачу наш подход.
def score_game(game_v):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1, 101, size=(1000))
    for number in random_array:
        count_ls.append(game_v(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)

# запускаем
score_game(game_v3)