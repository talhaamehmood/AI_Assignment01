import matplotlib.pyplot as plt
from grid import *

def dls(limit=10):
    grid = create_grid()
    stack = [(start, 0)]
    visited = {start}
    parent = {}

    plt.figure()

    while stack:
        spawn_dynamic(grid)

        current, depth = stack.pop()

        if current == target:
            break

        if depth < limit:
            for neighbor in get_neighbors(current, grid):
                if neighbor not in visited:
                    visited.add(neighbor)
                    parent[neighbor] = current
                    stack.append((neighbor, depth+1))

        frontier = {node for node, _ in stack}
        draw(grid, frontier, visited)

    path = reconstruct(parent)
    draw(grid, set(), visited, path)
    plt.show()

dls()