import networkx as nx

graph = nx.Graph()
graph.add_nodes_from("ABCDEFG")
graph.add_edges_from([
    ('A', 'B'),
    ('B', 'C'),
    ('C', 'D'),
    ('F', 'G')
])

# def connected_components(g):
#     return len(list(nx.connected_components(g)))
def connected_components(g):
    num_components = 0
    visited = set()
    for node in graph.nodes:
        if node not in visited:
            num_components += 1
            visited.add(node)
            queue = [node]
            while queue:
                current_node = queue.pop(0)
                for neighbor in graph.neighbors(current_node):
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
    return num_components

print(connected_components(graph))