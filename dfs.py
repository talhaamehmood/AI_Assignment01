import matplotlib.pyplot as plt
from grid import *

def dfs():
    grid = create_grid()
    stack = [start]
    visited = {start}
    parent = {}

    plt.figure()

    while stack:
        spawn_dynamic(grid)

        current = stack.pop()

        if current == target:
            break

        for neighbor in get_neighbors(current, grid):
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = current
                stack.append(neighbor)

        draw(grid, set(stack), visited)

    path = reconstruct(parent)
    draw(grid, set(), visited, path)
    plt.show()

dfs()