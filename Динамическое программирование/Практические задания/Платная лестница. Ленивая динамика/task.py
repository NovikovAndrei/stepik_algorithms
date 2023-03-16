from typing import Union, Sequence
from functools import lru_cache


def stairway_path(stairway: Sequence[Union[float, int]]) -> Union[float, int]:
    """
    Рассчитайте минимальную стоимость подъема на верхнюю ступень,
    если мальчик умеет наступать на следующую ступень и перешагивать через одну.

    :param stairway: список целых чисел, где каждое целое число является стоимостью конкретной ступени
    :return: минимальная стоимость подъема на верхнюю ступень
    """
    # TODO реализовать ленивую динамику
    @lru_cache
    def rec_stair(n):
        if n == 0 or n == 1:
            return stairway[n]
        return stairway[n] + min(rec_stair(n-1),
                                 rec_stair(n-2))
    return rec_stair(len(stairway) - 1)

def stairway_path1(stairway: Sequence[Union[float, int]]) -> Union[float, int]:
    cache = {0: stairway[0], 1: stairway[1]}
    def rec_stair(n):
        if cache.get(n):
            return cache[n]
        cache[n] = stairway[n] + min(rec_stair(n-1),
                                 rec_stair(n-2))
        return cache[n]
    return rec_stair(len(stairway) - 1)


if __name__ == '__main__':
    print(stairway_path1((1, 3, 1, 5)))  # 7
