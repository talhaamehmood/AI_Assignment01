import matplotlib.pyplot as plt
import numpy as np
import random

ROWS = 10
COLS = 10
def create_grid():
    grid = np.zeros((ROWS, COLS))
    grid[2:8, 5] = -1  
    return grid

start = (5, 2)
target = (8, 8)

directions = [
    (-1, 0),   
    (0, 1),   
    (1, 0),    
    (1, 1),    
    (0, -1),   
    (-1, -1),  
    (-1, 1),   
    (1, -1)    
]

def get_neighbors(node, grid):
    neighbors = []
    for dr, dc in directions:
        r, c = node[0] + dr, node[1] + dc
        if 0 <= r < ROWS and 0 <= c < COLS:
            if grid[r][c] != -1:
                neighbors.append((r, c))
    return neighbors

def draw(grid, frontier=set(), explored=set(), path=set()):
    display = np.copy(grid)

    for r, c in frontier:
        display[r][c] = 2
    for r, c in explored:
        display[r][c] = 3
    for r, c in path:
        display[r][c] = 4

    display[start] = 5
    display[target] = 6

    plt.clf()
    plt.imshow(display)
    plt.pause(0.2)

def reconstruct(parent):
    path = set()
    node = target
    while node in parent:
        path.add(node)
        node = parent[node]
    return path

def spawn_dynamic(grid):
    if random.random() < 0.05:
        r = random.randint(0, ROWS-1)
        c = random.randint(0, COLS-1)
        if grid[r][c] == 0 and (r, c) != start and (r, c) != target:
            grid[r][c] = -1