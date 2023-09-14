# Route Between Nodes: Given a directed graph, design an algorithm to find out
# whether there is a route between two nodes.

import collections


def does_route_exist(graph: dict[int, list[int]], node1: int, node2: int) -> bool:
    queue = collections.deque([node1])
    visited = set([node1])

    while queue:
        node = queue.pop()
        print(f"Visiting {node}")
        if node == node2:
            print(f"Found {node2}!")
            return True

        for child in graph.get(node, []):
            if child not in visited:
                queue.append(child)
                visited.add(child)

    return False


graph = {
    1: [2],
    2: [3],
    3: [4],
    4: [1, 5],
    5: [6, 7, 8, 9],

    10: [11],
    11: [12],
}

result = does_route_exist(graph, 10, 11)
print(result)
