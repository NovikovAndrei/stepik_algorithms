def fib_iterative(n: int) -> int:
    """
    Вычислить n-е число последовательности Фибоначчи, используя итеративный алгоритм.

    :param n: Номер числа последовательности Фибоначчи. Нумерация чисел с 0
    :return: n-е число последовательности Фибоначчи
    """
    # TODO написать итеративный алгоритм чисел Фибоначчи
    if n < 0:
        raise ValueError("число не должно быть отрицательным")

    a, b = 0, 1

    if n == 0:
        return a
    if n == 1:
        return b

    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


if __name__ == '__main__':
    print(fib_iterative(2))  # 1
    print(fib_iterative(5))  # 5
