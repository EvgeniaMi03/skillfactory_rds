import numpy as np
#Компьютер загадывает целое число от 1 до 100
number = np.random.randint(1,100)

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
            i = predict
        elif number < predict:
            j = predict
    return(count)

count1=game_v3(number)
print (f"Вы угадали число {number} за {count1} попыток.")