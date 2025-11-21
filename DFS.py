def dfs(graph, start, goal, visited=None):
    if visited is None:
        visited = set()

    visited.add(start)
    print(start, end=" ")

    if start == goal:
        return True

    for neighbor in graph[start]:
        if neighbor not in visited:
            if dfs(graph, neighbor, goal, visited):
                return True

    return False


graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': [],
    'G': []
}

print("DFS dari A ke G:")
dfs(graph, 'A', 'G')
