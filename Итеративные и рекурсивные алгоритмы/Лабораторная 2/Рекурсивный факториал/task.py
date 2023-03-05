def factorial_recursive(n: int) -> int:
    """
    Рассчитать факториал числа n рекурсивным способом

    :param n: Число, факториал которого нужно найти
    :return: n! - факториал числа n
    """
    # TODO реализовать рекурсивный алгоритм нахождения факториала
    if n < 0:
        raise ValueError("Факториал считается от не отрицательных целых чисел")
    if not isinstance(n, int):
        raise TypeError("Факториал считается от не отрицательных целых чисел")

    res = 1
    if n == 0 or n == 1:
        return res

    return factorial_recursive(n - 1) * n

if __name__ == '__main__':
    for val in range(11):
        print(f"val = {val}, factorial = {factorial_recursive(val)}")