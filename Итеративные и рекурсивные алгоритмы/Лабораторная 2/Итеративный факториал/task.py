def factorial_iterative(n: int) -> int:
    """
    Рассчитать факториал числа n итеративным способом

    :param n: Число, факториал которого нужно найти
    :return: n! - факториал числа n
    """
    # TODO реализовать итеративный алгоритм нахождения факториала
    if n < 0:
        raise ValueError("Факториал считается от не отрицательных целых чисел")
    if not isinstance(n, int):
        raise TypeError("Факториал считается от не отрицательных целых чисел")

    res = 1
    if n == 0 or n == 1:
        return res

    for i in range(2, n + 1):
        res *= i
    return res


if __name__ == '__main__':
    for val in range(11):
        print(f"val = {val}, factorial = {factorial_iterative(val)}")
