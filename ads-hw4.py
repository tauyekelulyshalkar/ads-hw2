'''
# TASK 1 Graph Representation
graph = {}

def add_edge(v, w, weight):

    if v not in graph:
        graph[v] = []

    if w not in graph:
        graph[w] = []

    # undirected graph
    graph[v].append((w, weight))
    graph[w].append((v, weight))


# edges
add_edge('B', 'A', 12)
add_edge('C', 'A', 7)
add_edge('D', 'A', 6)
add_edge('E', 'C', 14)
add_edge('F', 'D', 8)
add_edge('C', 'B', 15)
add_edge('A', 'F', 1)

# print adjacency list
for vertex in graph:
    print(vertex, ">>>", graph[vertex])
'''

'''
# TASK 2 - DFS and BFS

from collections import deque

graph = {
    'A': ['B', 'C', 'D', 'F'],
    'B': ['A', 'C'],
    'C': ['A', 'E', 'B'],
    'D': ['A', 'F'],
    'E': ['C'],
    'F': ['D', 'A']
}

# DFS

visited = set()

def dfs(vertex):

    visited.add(vertex)

    print(vertex, end=" ")

    for neighbor in graph[vertex]:

        if neighbor not in visited:
            dfs(neighbor)

print("DFS:")
dfs('B')

# BFS

print("\n")

visited = set()

queue = deque(['B'])

visited.add('B')

print("BFS:")

while queue:

    vertex = queue.popleft()

    print(vertex, end=" ")

    for neighbor in graph[vertex]:

        if neighbor not in visited:

            visited.add(neighbor)

            queue.append(neighbor)
'''

'''
# TASK 3 - Dijkstra Algorithm

graph = {
    'A': [('B', 12), ('C', 7), ('D', 6), ('F', 1)],
    'B': [('A', 12), ('C', 15)],
    'C': [('A', 7), ('E', 14), ('B', 15)],
    'D': [('A', 6), ('F', 8)],
    'E': [('C', 14)],
    'F': [('D', 8), ('A', 1)]
}

distances = {}

# infinity
for vertex in graph:
    distances[vertex] = float('inf')

distances['A'] = 0

visited = []

while len(visited) < len(graph):

    min_vertex = None

    for vertex in graph:

        if vertex not in visited:

            if min_vertex is None or distances[vertex] < distances[min_vertex]:
                min_vertex = vertex

    visited.append(min_vertex)

    for neighbor, weight in graph[min_vertex]:

        new_distance = distances[min_vertex] + weight

        if new_distance < distances[neighbor]:
            distances[neighbor] = new_distance


print("Shortest distances from A:\n")

for vertex in distances:
    print(f"A -> {vertex} = {distances[vertex]}")
'''
