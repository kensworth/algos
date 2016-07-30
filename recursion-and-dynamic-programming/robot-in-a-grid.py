#Imagine a robot sitting on the upper left corner of a grid with r rows and c columns. The robot can only move in two directions, right and down, but certain cells are 'off limits' such that the robot cannot step on them. Design an algorithm to find a path for the robot from the top left to the bottom right.
import random
width = 10
height = 10
#filling 2D array with 1's (90% chance) and 0's (10% chance)
grid = [[(1 if random.random() < 0.9 else 0) for x in range (width)] for y in range(height)]
#guaranteeing beginning and end nodes are traversable
grid[0][0], grid[height - 1][width - 1] = 1, 1
#iterative DFS
def traverse(grid):
    stack, visited, path, steps = [], [], [], 0
    stack.append([0, 0])
    while stack:
        steps += 1
        node = stack.pop()
        vertical, lateral = node[0], node[1]
        if (node[0] + 1 < len(grid)) and grid[node[0] + 1][node[1]]:
            stack.append([node[0] + 1, node[1]])
        if (node[1] + 1 < len(grid[0])) and grid[node[0]][node[1] + 1]:
            stack.append([node[0], node[1] + 1])
    print steps

traverse(grid)

def printGrid(grid):
    for i in range(len(grid)):
        print grid[i]
printGrid(grid)
