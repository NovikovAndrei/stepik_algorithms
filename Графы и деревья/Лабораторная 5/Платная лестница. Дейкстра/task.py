
from typing import Union
import heapq
import networkx as nx

def stairway_path(graph: nx.DiGraph) -> Union[float, int]:
    """
    Рассчитайте минимальную стоимость подъема на верхнюю ступень,
    если мальчик умеет наступать на следующую ступень и перешагивать через одну.

    :param graph: Взвешенный направленный граф NetworkX, по которому надо рассчитать стоимости кратчайших путей
    :return: минимальная стоимость подъема на верхнюю ступень
    """
    # TODO c помощью функции из модуля networkx найти стоимость кратчайшего пути до последней лестницы
    min_distance = {node: float("inf") for node in graph.nodes}
    starting_node = 0
    min_distance[starting_node] = 0

    queue = [(0, starting_node)]

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if current_distance > min_distance[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight["weight"]
            if distance < min_distance[neighbor]:
                min_distance[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))

    return min_distance[(len(min_distance)-1)]



if __name__ == '__main__':
    stairway = (5, 11, 43, 2, 23, 43, 22, 12, 6, 8)

    def stairway_graph(stairway):
        stairway_graph = nx.DiGraph()
        for i in range(len(stairway) - 1):
            stairway_graph.add_edge(i, i + 1, weight=stairway[i])
            stairway_graph.add_edge(i, i + 2, weight=stairway[i + 1])
        stairway_graph.add_edge(len(stairway) - 1, len(stairway), weight=stairway[-1])
        return stairway_graph


    stairway_graph = stairway_graph(stairway)  # TODO записать взвешенный граф, а лучше написать функцию, которая формирует граф по стоимости ступеней



    print(stairway_path(stairway_graph))  # 72
