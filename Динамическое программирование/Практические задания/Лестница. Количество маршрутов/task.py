def stairway_path(count_stairs: int) -> int:
    """
    Вычислить количество маршрутов до каждой ступени,
    если мальчик умеет наступать на следующую ступень и перешагивать через одну.

    :param count_stairs: Количество ступеней
    :return: Количество маршрутов до вершины
    """
    # TODO найти количество маршрутов до каждой ступени
    if count_stairs < 0:
        raise ValueError("Количество ступеней не может быть меньше 0")
    if count_stairs == 0:
        return 1
    if count_stairs == 1:
        return 2

    dp = [0] * (count_stairs + 1)
    dp[0] = 1
    dp[1] = 2

    for i in range(2, count_stairs + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[-1]


if __name__ == '__main__':
    print(stairway_path(0))  # 1
    print(stairway_path(5))  # 13
