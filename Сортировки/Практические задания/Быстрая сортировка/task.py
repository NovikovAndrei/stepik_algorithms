from typing import List


def sort(container: List[int]) -> List[int]:
    """
    Алгоритм быстрой сортировки.

    1. Выбираем опорный элемент. Например, первый элемент.
    2. В левую часть отправляем всё что меньше опорного элемента, в правую всё что больше.
    3. К левой и правой части рекурсивно применяет алгоритм быстрой сортировки.

    :param container: последовательность, которую надо отсортировать
    :return: Отсортированная в порядке возрастания последовательность
    """
    ...  # TODO реализовать алгоритм быстрой сортировки
    # if len(container) <= 1:
    #     return container
    #
    # pivot = container[0]
    # left = []
    # right = []
    #
    # for element in container[1:]:
    #     if element <= pivot:
    #         left.append(element)
    #     else:
    #         right.append(element)
    #
    # return sort(left) + [pivot] + sort(right)

    if not container:
        return container

    pivot = container[0]
    return (
            sort([item for item in container if item < pivot]) +
            [item for item in container if item == pivot] +
            sort([item for item in container if item > pivot])
    )


a = [77, 5, 2, 99, 14, 55, 3, 8, 6, 12]
print(sort(a))
