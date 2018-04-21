#import pdb
from helpers import normalize, blur

def initialize_beliefs(grid):
    height = len(grid)
    width = len(grid[0])
    area = height * width
    belief_per_cell = 1.0 / area
    beliefs = []
    for i in range(height):
        row = []
        for j in range(width):
            row.append(belief_per_cell)
        beliefs.append(row)
    return beliefs

def sense(color, grid, beliefs, p_hit, p_miss):
    new_beliefs = []
    norm_new_beliefs = []

    #
    # TODO - implement this in part 2
    #
    height = len(beliefs)
    width = len(beliefs[0])

    for j in range(height):
        row = []
        for i in range(width):
            belief = beliefs[j][i]
            if color == grid[j][i]:
                row.append(belief * p_hit)
            else:
                row.append(belief * p_miss)
        new_beliefs.append(row)

    total = 0
    for j in range(height):
        for i in range(width):
            total = total + new_beliefs[j][i]
    
    for j in range(0,height):
        row = []
        for i in range(0,width):
            row.append(new_beliefs[j][i]/total)
        norm_new_beliefs.append(row)
        
    return norm_new_beliefs

def move(dy, dx, beliefs, blurring):
    height = len(beliefs)
    width = len(beliefs[0])
    new_G = [[0.0 for i in range(width)] for j in range(height)]
    for i, row in enumerate(beliefs):
        for j, cell in enumerate(row):
            new_i = (i + dy) % height
            new_j = (j + dx) % width
            #pdb.set_trace()
            new_G[int(new_i)][int(new_j)] = cell
    return blur(new_G, blurring)