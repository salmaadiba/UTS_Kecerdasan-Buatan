from collections import deque

# DEFINISI GRAPH (WAJIB ADA)
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': [],
    'G': []
}

# FUNGSI BFS
def bfs(graph, start, goal):
    visited = set()
    queue = deque([start])

    while queue:
        node = queue.popleft()
        print(node, end=" ")

        if node == goal:
            print("\nGoal ditemukan:", goal)
            return True

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    print("\nGoal tidak ditemukan.")
    return False


# PEMANGGILAN FUNGSI BFS
print("BFS dari A ke G:")
bfs(graph, 'A', 'G')
