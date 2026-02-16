import heapq
import matplotlib.pyplot as plt
from grid import *

def ucs():
    grid = create_grid()
    pq = []
    heapq.heappush(pq, (0, start))

    visited = set()
    parent = {}
    cost = {start: 0}

    plt.figure()

    while pq:
        spawn_dynamic(grid)

        curr_cost, current = heapq.heappop(pq)

        if current in visited:
            continue

        visited.add(current)

        if current == target:
            break

        for neighbor in get_neighbors(current, grid):
            new_cost = curr_cost + 1
            if neighbor not in cost or new_cost < cost[neighbor]:
                cost[neighbor] = new_cost
                parent[neighbor] = current
                heapq.heappush(pq, (new_cost, neighbor))

        frontier = {node for _, node in pq}
        draw(grid, frontier, visited)

    path = reconstruct(parent)
    draw(grid, set(), visited, path)
    plt.show()

ucs()