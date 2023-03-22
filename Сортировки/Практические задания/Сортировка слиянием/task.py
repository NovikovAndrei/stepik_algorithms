from typing import List


def sort(container: List[int]) -> List[int]:
    """
    Алгоритм сортировки слиянием.

    1. Если массив состоит из 1 элемента – он отсортирован
    2. Иначе массив разбивается на две части, которые сортируются рекурсивно
    3. После сортировки двух частей массива к ним применяется процедура слияния

    :param container: Массив, который надо отсортировать
    :return: Отсортированный в порядке возрастания массив
    """

    # TODO реализуйте сортировку слиянием
    # def _merge(left_c: list, right_c: list) -> list:
    #     result = []
    #     while True:
    #         if left_c[0] <= right_c[0]:
    #             result.append(left_c.pop(0))
    #         else:
    #             result.append(right_c.pop(0))
    #         if not left_c:
    #             result += right_c
    #             break
    #         if not right_c:
    #             result += left_c
    #             break
    #     return result
    if len(container) < 2:
        return container

    mid = len(container) // 2

    new_l = sort(container[:mid])
    new_r = sort(container[mid:])

    return merge(new_l, new_r)


def merge(left_c: list, right_c: list) -> list:
    result = []
    while True:
        if left_c[0] <= right_c[0]:
            result.append(left_c.pop(0))
        else:
            result.append(right_c.pop(0))
        if not left_c:
            result += right_c
            break
        if not right_c:
            result += left_c
            break
    return result

# def merge2(left_c: list, right_c: list) -> list:
#     result = []
#     i = 0
#     j = 0
#     while True:
#         if left_c[i] <= right_c[j]:
#             result.append(left_c[i])
#             i += 1
#         else:
#             result.append(right_c[j])
#             j += 1
#
#         if i == len(left_c):
#             result += right_c[j:]
#             break
#         elif j == len(right_c):
#             result += left_c[i:]
#             break
#     return result

# print(merge([1,2,7], [8,34,99]))
# print((merge([1,5], [4])))
# print(merge2([1,2,7], [8,34,99]))
# print((merge2([1,5], [4])))
