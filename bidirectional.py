import matplotlib.pyplot as plt
from grid import *

def bidirectional():
    grid = create_grid()

    front1 = {start}
    front2 = {target}

    visited1 = {start}
    visited2 = {target}

    parent1 = {}
    parent2 = {}

    meet_node = None

    plt.figure()

    while front1 and front2:

        spawn_dynamic(grid)

        next_front1 = set()
        for node in front1:
            for neighbor in get_neighbors(node, grid):
                if neighbor not in visited1:
                    visited1.add(neighbor)
                    parent1[neighbor] = node
                    next_front1.add(neighbor)

        front1 = next_front1

        intersection = front1 & visited2
        if intersection:
            meet_node = intersection.pop()
            break

        next_front2 = set()
        for node in front2:
            for neighbor in get_neighbors(node, grid):
                if neighbor not in visited2:
                    visited2.add(neighbor)
                    parent2[neighbor] = node
                    next_front2.add(neighbor)

        front2 = next_front2

        intersection = front2 & visited1
        if intersection:
            meet_node = intersection.pop()
            break

        draw(grid, front1 | front2, visited1 | visited2)

    if not meet_node:
        print("No Path Found")
        plt.show()
        return

    path = set()

    node = meet_node
    while node in parent1:
        path.add(node)
        node = parent1[node]
    path.add(start)

    node = meet_node
    while node in parent2:
        path.add(node)
        node = parent2[node]
    path.add(target)

    draw(grid, set(), visited1 | visited2, path)
    plt.show()

bidirectional()