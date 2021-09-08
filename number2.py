from random import randint
import time
import pandas as pd


def shell_sort(data):
    data = data.copy()
    last_index = len(data) - 1
    step = len(data) // 2
    while step > 0:
        for i in range(step, last_index + 1, 1):
            j = i
            delta = j - step
            while delta >= 0 and data[delta] > data[j]:
                data[delta], data[j] = data[j], data[delta]
                j = delta
                delta = j - step
        step //= 2
    return data

def quick_sort_normal(array):
    if len(array) <= 1:
        return array

    support_element = array[0]

    left = list(filter(lambda x: x < support_element, array))
    center = [i for i in array if i == support_element]
    right = list(filter(lambda x: x > support_element, array))

    return quick_sort_normal(left) + center + quick_sort_normal(right)


def quick_sort_median(array):
    if len(array) <= 1:
        return array

    support_element = (array[0] + array[-1] + array[len(array) // 2]) // 3

    left = list(filter(lambda x: x < support_element, array))
    center = [i for i in array if i == support_element]
    right = list(filter(lambda x: x > support_element, array))

    return quick_sort_median(left) + center + quick_sort_median(right)


def random_elements(lenght, minimum, maximum):
    return [randint(minimum, maximum) for _ in range(lenght)]


def growing_elements(lenght):
    return [i for i in range(lenght)]


def decrease_elements(lenght):
    return [i for i in range(lenght, 0, -1)]


def growing_decrease_elements(lenght):
    return [i for i in range(int(lenght / 2))] + [i for i in range(int(lenght / 2), 0, -1)]


def timed(function):
    def wrapper():
        start_time = time.time()
        value = function()
        duration = time.time() - start_time
        return duration

    return wrapper()


def tests(lenghts, minimum, maximum):
    indexs = ['Сортировка Шелла', 'Быстрая сортировка', 'Быстрая медианная сортировка', 'Встроенная сортировка']
    place = "results_2.xlsx"
    massives = [[random_elements(i*100, minimum, maximum) for i in lenghts], [growing_elements(i) for i in lenghts],
                [decrease_elements(i) for i in lenghts],
                [growing_decrease_elements(i) for i in lenghts]]
    results = [[[timed(lambda: shell_sort(j)) for j in i] for i in massives],
               [[timed(lambda: quick_sort_normal(j)) for j in i] for i in massives],
               [[timed(lambda: quick_sort_median(j)) for j in i] for i in massives],
               [[timed(lambda: sorted(j)) for j in i] for i in massives]]
    result = pd.DataFrame([results[i][0] for i in range(len(results))], index=[indexs],
                          columns=[str(len(i)) for i in massives[0]])
    result.to_excel(place, sheet_name="random_elements")

    result = pd.DataFrame([results[i][1] for i in range(len(results))], index=[indexs],
                          columns=[str(len(i)) for i in massives[1]])
    with pd.ExcelWriter(place, mode='a') as writer:
        result.to_excel(writer, sheet_name='growing_elements')

    result = pd.DataFrame([results[i][2] for i in range(len(results))], index=[indexs],
                          columns=[str(len(i)) for i in massives[2]])
    with pd.ExcelWriter(place, mode='a') as writer:
        result.to_excel(writer, sheet_name='decrease_elements')

    result = pd.DataFrame([results[i][3] for i in range(len(results))], index=[indexs],
                          columns=[str(len(i)) for i in massives[3]])
    with pd.ExcelWriter(place, mode='a') as writer:
        result.to_excel(writer, sheet_name='growing_decrease_elements')


lenghts = [i for i in range(100, 1000, 100)]
tests(lenghts, 0, 1000)
