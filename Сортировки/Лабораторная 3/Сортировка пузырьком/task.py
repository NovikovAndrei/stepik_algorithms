from typing import Sequence


def sort(container: Sequence[int]) -> Sequence[int]:
    """
    Сортировка пузырьком

    1. Пройти по всему массиву, сравнивая каждые два соседних элемента.
    2. Если элементы не находятся в нужном порядке, меняйте их местами.
    3. Повторяйте шаг 2, пока не пройдете весь массив без изменений.
    4. Повторяйте шаги 1-3, пока не отсортируете весь массив.

    :param container: Массив, который надо отсортировать
    :return: Отсортированный в порядке возрастания массив
    """
    # TODO реализовать алгоритм сортировки пузырьком
    len_c = len(container) - 1
    while len_c > 1:
        for i in range(len_c):
            if container[i] > container[i + 1]:
                container[i], container[i + 1] = container[i + 1], container[i]
        len_c -= 1
    return container
if __name__ == '__main__':

    a = [77, 14, 5, 88, 13, 7, 2, 8]
    print(sort(a))