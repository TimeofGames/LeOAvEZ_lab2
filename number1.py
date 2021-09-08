import numpy as np
import time
import pandas as pd


def multiply(size):
    matrix_1 = np.ones([size, size], dtype=int)
    matrix_2 = np.ones([size, size], dtype=int)
    print(size)
    return timed(lambda: np.dot(matrix_1, matrix_2))


def timed(function):
    def wrapper():
        start_time = time.time()
        value = function()
        duration = time.time() - start_time
        return duration

    return wrapper()


def tests():
    sizes = [100, 200, 400, 1000, 2000, 4000, 10000]

    results = [[timed(lambda: multiply(i)) for i in sizes]]
    results.append([i ** 3 for i in sizes])
    results.append([results[0][i] / results[1][i] for i in range(len(sizes))])
    result = pd.DataFrame(results, index=['Время', 'Кол-во итераций', 'Время на итерацию'],
                          columns=[str(i) for i in sizes])
    result.to_excel("results_1.xlsx", sheet_name="Sheet_first")


tests()
