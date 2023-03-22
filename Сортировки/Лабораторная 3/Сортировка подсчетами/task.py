from typing import Sequence


def sort(container: Sequence[int]) -> Sequence[int]:
    """
    Сортировка подсчетами

    1. Определите максимальное значение в массиве и заполните вспомогательный массив с подсчетом количества элементов.
    2. Посчитайте количество каждого объекта
    3. Зная количество каждого объекта, восстановите отсортированный массив

    :param container: Массив, который надо отсортировать
    :return: Отсортированный в порядке возрастания массив
    """
    # TODO реализовать алгоритм сортировки подсчетами
    if not container:
        return container
    max_c = max(container)
    new_array = [0] * (max_c + 1)
    for i in container:
        new_array[i] += 1
    res = []
    for i in range(max_c + 1):
        res += [i] * new_array[i]
    return 1

if __name__ == '__main__':

    b = [1,2,1,2,5,5,0,0]
    print(sort(b))