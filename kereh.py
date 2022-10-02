# username : kereh
# github : https://github.com/kereh
#hacktoberfest2022

GRAPH = {
    'A': ['B','C'],
    'B': ['D','E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

def bfs_algorithm(nodes, start):
    
    queue = [start]
    visited = []

    while queue:

        current_node = queue.pop(-1)

        if current_node in visited:
            continue

        neighbors = nodes[current_node]

        for neighbor in neighbors:

            queue.append(neighbor)

        visited.append(current_node)

    return visited

print(bfs_algorithm(GRAPH, 'A'))
