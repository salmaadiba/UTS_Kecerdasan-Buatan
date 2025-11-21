import heapq

def a_star(graph, h, start, goal):
    pq = [(0 + h[start], start)]
    visited = set()
    g_cost = {start: 0}

    while pq:
        f, node = heapq.heappop(pq)

        if node == goal:
            print("Path found to", goal)
            return True

        visited.add(node)
        print(node, end=" ")

        for neighbor, cost in graph[node]:
            temp_g = g_cost[node] + cost

            if neighbor not in g_cost or temp_g < g_cost[neighbor]:
                g_cost[neighbor] = temp_g
                f_cost = temp_g + h[neighbor]
                heapq.heappush(pq, (f_cost, neighbor))

    return False


graph_cost = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 1)],
    'D': [],
    'E': [('G', 1)],
    'F': [('G', 3)],
    'G': []
}

heuristic = {
    'A': 7, 'B': 6, 'C': 2,
    'D': 10, 'E': 1, 'F': 1,
    'G': 0
}

print("\n\nA* Search dari A ke G:")
a_star(graph_cost, heuristic, 'A', 'G')
