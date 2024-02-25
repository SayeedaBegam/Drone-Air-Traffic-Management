import heapq

class Node:
    def __init__(self, position, parent=None):
        self.position = position
        self.parent = parent
        self.g = 0  # Cost from start to current node
        self.h = 0  # Heuristic cost from current node to goal
        self.f = 0  # Total cost

    def __lt__(self, other):
        return self.f < other.f

def astar(start, goal, neighbors_func, heuristic_func):
    open_set = []
    heapq.heappush(open_set, (0, start))  # Priority queue by f value
    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic_func(start, goal)}

    while open_set:
        current = heapq.heappop(open_set)[1]

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            return path[::-1]  # Return reversed path

        for neighbor in neighbors_func(current):
            tentative_g_score = g_score[current] + 1  # Assuming uniform cost for simplicity

            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = g_score[neighbor] + heuristic_func(neighbor, goal)
                if neighbor not in [i[1] for i in open_set]:
                    heapq.heappush(open_set, (f_score[neighbor], neighbor))

    return []

def heuristic(a, b):
    # Example heuristic: Manhattan distance
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# Example usage
start = (0, 0)  # Starting node
goal = (4, 5)  # Goal node
def neighbors(node):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 4-way connectivity
    result = []
    for d in directions:
        neighbor = (node[0] + d[0], node[1] + d[1])
        if 0 <= neighbor[0] < 6 and 0 <= neighbor[1] < 6:  # Assuming grid size of 6x6 for example
            result.append(neighbor)
    return result

path = astar(start, goal, neighbors, heuristic)
print("Path from start to goal:", path)
