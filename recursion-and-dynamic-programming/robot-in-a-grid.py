#Imagine a robot sitting on the upper left corner of a grid with r rows and c columns. The robot can only move in two directions, right and down, but certain cells are 'off limits' such that the robot cannot step on them. Design an algorithm to find a path for the robot from the top left to the bottom right.
import random
width = 10
height = 10
#filling 2D array with 1's (90% chance) and 0's (10% chance)
grid = [[(1 if random.random() < 0.9 else 0) for x in range (width)] for y in range(height)]
#guaranteeing beginning and end points are traversable
grid[0][0], grid[height - 1][width - 1] = 1, 1
#iterative DFS
def traverse(grid, start):
    frontier = [] 
    frontier.append(start)
    while frontier:
        point = frontier.pop()
        print point
        if isGoal(point):
            print 'reached'
            break
        for next_point in next(point):
            frontier.append(next_point)


def isGoal(point):
    x, y = point
    return (x == len(grid) - 1) and (y == len(grid[0]) - 1)

def next(point):
    row, col = point
    next_points = []
    if row < len(grid) - 1 and grid[row + 1][col]:
        next_points.append((row + 1, col))
    if col < len(grid[0]) - 1 and grid[row][col + 1]:
        next_points.append((row, col + 1))
    return next_points

def printGrid(grid):
    for row in grid:
        print row

printGrid(grid)
traverse(grid, (0,0))
