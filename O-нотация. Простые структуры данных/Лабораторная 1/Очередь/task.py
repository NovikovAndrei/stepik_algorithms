"""
My little Queue
"""
from typing import Any


class Queue:
    def __init__(self):
        """
        Очередь с помощью python list
        TODO Описать где начало и конец очереди
        queue[0] - первый элемент очереди
        queue[-1] - последний элемент очереди
        """
        # TODO инициализировать список
        self._queue = list()
        self._len = 0

    def enqueue(self, elem: Any) -> None:
        """
        Добавление элемент в конец очереди

        :param elem: Элемент, который должен быть добавлен
        """
        # TODO реализовать метод enqueue
        self._queue.append(elem)
        self._len += 1

    def dequeue(self) -> Any:
        """
        Извлечение элемента из начала очереди.

        :raise: IndexError - Ошибка, если очередь пуста

        :return: Извлеченный с начала очереди элемент.
        """
        # TODO реализовать метод dequeue
        if not self._queue:
            raise IndexError("очередь пустая")
        self._len -= 1
        return self._queue.pop(0)

    def peek(self, ind: int = 0) -> Any:
        """
        Просмотр произвольного элемента, находящегося в очереди, без его извлечения.

        :param ind: индекс элемента (отсчет с начала, 0 - первый с начала элемент в очереди,
        1 - второй с начала элемент в очереди, и т.д.)

        :raise: TypeError - если указан не целочисленный тип индекса
        :raise: IndexError - если индекс вне границ очереди

        :return: Значение просмотренного элемента
        """
        # TODO реализовать метод peek
        if not isinstance(ind, int):
            raise TypeError("указан не целочисленный тип индекса")
        if not 0 <= ind <= len(self._queue):
            raise IndexError("индекс вне границ очереди")
        return self._queue[ind]

    def clear(self) -> None:
        """ Очистка очереди. """
        # TODO реализовать метод clear
        self._queue.clear()
        self._len = 0

    def __len__(self):
        """ Количество элементов в очереди. """
        # TODO реализовать метод __len__
        return self._len

