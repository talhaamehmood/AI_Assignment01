import matplotlib.pyplot as plt
from grid import *
from dls import dls

def iddfs(max_depth=15):
    for depth in range(max_depth):
        print("Depth:", depth)
        dls(depth)

iddfs()