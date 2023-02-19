from typing import Any


class Stack:
    def __init__(self):
        ...  # TODO использовать python list для реализации стека
        self._stack = list()
        self._len = 0

    def push(self, elem: Any) -> None:
        """
        Добавление элемента в вершину стека

        :param elem: Элемент, который должен быть добавлен
        """
        self._stack.append(elem)  # TODO реализовать операцию push
        self._len += 1

    def pop(self) -> Any:
        """
        Извлечение элемента из вершины стека.

        :raise: IndexError - Ошибка, если стек пуст

        :return: Извлеченный с вершины стека элемент.
        """
        if not self._stack:
            raise IndexError("стек пустой")
        # TODO реализовать операцию pop
        self._len -= 1
        return self._stack.pop()

    def peek(self, ind: int = 0) -> Any:
        """
        Просмотр произвольного элемента, находящегося в стеке, без его извлечения.

        :param ind: индекс элемента (отсчет с вершины, 0 - вершина, последний добавленный элемент, 1 - предпоследний элемент, и т.д.)

        :raise: TypeError - если указан не целочисленный тип индекса
        :raise: IndexError - если индекс вне границ стека

        :return: Значение просмотренного элемента
        """
        if not isinstance(ind, int):
            raise TypeError("может быть только int")
        if not 0 <= ind <= len(self._stack):
            raise IndexError("вне границ стека")

        inv_ind = -1 - ind
        return self._stack[inv_ind]  # TODO реализовать операцию peek

    def clear(self) -> None:
        """ Очистка стека. """
        self._stack.clear()  # TODO реализовать операцию clear
        self._len = 0

    def __len__(self) -> int:
        """ Количество элементов в стеке. """
        return self._len  # TODO реализовать операцию __len__
