from functools import cache
count = 0

@cache
def fib_recursive(n: int) -> int:
    """
    Вычислить n-е число последовательности Фибоначчи, используя рекурсивный алгоритм.

    :param n: Номер числа последовательности Фибоначии. Нумерация чисел с 0
    :return: n-е число последовательности Фибоначчи
    """
    # TODO реализовать рекурсивный алгоритм
    global count
    count += 1
    if n < 0:
        raise ValueError("число не должно быть отрицательным")
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib_recursive(n - 1) + fib_recursive(n - 2)


if __name__ == '__main__':
    # print(fib_recursive(2))  # 1
    # print(fib_recursive(15))  # 610
    for i in range(30):
        count = 0
        print(f"i = {i}, res = {fib_recursive(i)}, c = {count}, n^2 = {i**2}, 2^n = {2**i}")