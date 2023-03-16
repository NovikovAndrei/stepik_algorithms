from typing import Union, Sequence


def stairway_path(stairway: Sequence[Union[float, int]]) -> Union[float, int]:
    """
    Рассчитайте минимальную стоимость подъема на верхнюю ступень,
    если мальчик умеет наступать на следующую ступень и перешагивать через одну.

    :param stairway: список целых чисел, где каждое целое число является стоимостью конкретной ступени
    :return: минимальная стоимость подъема на верхнюю ступень
    """
    # TODO реализовать прямой метод расчета
    count_stairs = len(stairway)
    if count_stairs == 1:
        return stairway[0]
    if count_stairs == 2:
        return stairway[1]

    cost = [0] * len(stairway)
    cost[0] = stairway[0]
    cost[1] = stairway[1]
    # cost = stairway[0:2] + [0] * (len(stairway) - 2)

    for i in range(2, count_stairs):
        cost[i] = stairway[i] + min(cost[i - 1],
                                    cost[i - 2])
    return cost[-1]


def stairway_path1(stairway: Sequence[Union[float, int]]) -> Union[float, int]:
    count_stairs = len(stairway)
    if count_stairs == 1:
        return stairway[0]
    if count_stairs == 2:
        return stairway[1]

    cost = [0, stairway[0], stairway[1]]
    for i in range(2, count_stairs):
        cost.pop(0)
        cost.append(stairway[i] + min(cost[0],
                                      cost[1]))
    return cost[-1]

def stairway_path2(stairway: Sequence[Union[float, int]]) -> Union[float, int]:
    count_stairs = len(stairway)
    if count_stairs == 1:
        return stairway[0]
    if count_stairs == 2:
        return stairway[1]

    a,b,c = stairway[0], stairway[1], 0
    for i in range(2, count_stairs):
        c = stairway[i] + min(a,b)
        a, b = b, c
    return c

if __name__ == '__main__':
    print(stairway_path2([1, 3, 1, 5]))  # 7
