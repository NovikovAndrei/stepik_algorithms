"""
This module implements some functions based on linear search algo
"""
from typing import List


def min_search(arr: List[int]) -> int:
    """
    Функция для поиска минимума в массиве

    :param arr: Массив целых чисел

    :return: Индекс первого вхождения элемента в массиве
    """
    # TODO реализовать итеративный линейный поиск
    if not arr:
        raise ValueError("список пустой")
    # tmp = list(enumerate(arr))
    # min_ = tmp[0]
    # for i in range(len(arr)):
    #     if tmp[i][1] < min_[1]:
    #         min_ = tmp[i]
    # return min_[0]
    min_ind = 0
    for i in range(1, len(arr)):
        if arr[i] < arr[min_ind]:
            min_ind = i
    return min_ind


if __name__ == '__main__':
    a = [7, 7, 24, 1, 0, 12]

    print(min_search(a))