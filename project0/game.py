import numpy as np

def random_predict(number:int=1) -> int:
    """рандомно угадываем число

    Args:
        number (int, optional): загаданное число. Defaults to 1.

    Returns:
        int: число попыток
    """
    count = 0
    
    while True:
        count += 1
        predict_number = np.random.randint(1,201)
        if number == predict_number:
            break
    return(count)

def score_game(random_predict) -> int:
    """считаем среднее количество угадываний из 1000 подходов

    Args:
        random_predict (_type_): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1)
    random_array = np.random.randint(1, 101, size=(100))
    
    for number in random_array:
        count_ls.append(random_predict(number))
            
    score = int(np.mean(count_ls))
    
    print(f'ваш алгоритм угадывает число в среднем за {score} раз')
    return(score)

score_game(random_predict)