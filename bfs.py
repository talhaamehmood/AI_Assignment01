from collections import deque
import matplotlib.pyplot as plt
from grid import *

def bfs():
    grid = create_grid()
    queue = deque([start])
    visited = {start}
    parent = {}

    plt.figure()

    while queue:
        spawn_dynamic(grid)

        current = queue.popleft()

        if current == target:
            break

        for neighbor in get_neighbors(current, grid):
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = current
                queue.append(neighbor)

        draw(grid, set(queue), visited)

    path = reconstruct(parent)
    draw(grid, set(), visited, path)
    plt.show()

bfs()