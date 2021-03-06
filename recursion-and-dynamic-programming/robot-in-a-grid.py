# Imagine a robot sitting on the upper left corner of a grid with r rows and c columns.
# The robot can only move in two directions, right and down, but certain cells are 'off limits' such that the robot cannot step on them.
# Design an algorithm to find a path for the robot from the top left to the bottom right.
import random
width = 10
height = 10
#filling 2D array with 1's (90% chance) and 0's (10% chance)
grid = [[(1 if random.random() < 0.8 else 0) for x in range (width)] for y in range(height)]
#guaranteeing beginning and end points are traversable
grid[0][0], grid[height - 1][width - 1] = 1, 1
#iterative BFS
class Frontier:
    def append(value):
        raise NotImplementedError()
    def pop():
        raise NotImplementedError()

class Queue(Frontier):
    def __init__(self, values=[]):
        self.queue = values
    def append(self, value):
        self.queue.append(value)
    def pop(self):
        return self.queue.pop(0)
    def __len__(self):
        return len(self.queue)

def traverse(grid, start):
    visited = set([start])
    path = []
    frontier = Queue() 
    frontier.append(start)
    steps = 0
    while frontier:
        steps += 1
        point = frontier.pop()
        visited.add(point)
        if isGoal(point):
            print 'reached'
            print 'steps:', steps
            print 'visited:', visited
            return
        for next_point in next(point, visited):
            frontier.append(next_point)
    print 'failed'

def isGoal(point):
    x, y = point
    return (x == len(grid) - 1) and (y == len(grid[0]) - 1)

def next(point, visited):
    row, col = point
    next_points = []
    if row < len(grid) - 1 and grid[row + 1][col] and not (row + 1, col) in visited:
        next_points.append((row + 1, col))
    if col < len(grid[0]) - 1 and grid[row][col + 1] and not (row, col + 1) in visited:
        next_points.append((row, col + 1))
    return next_points

def printGrid(grid):
    for row in grid:
        print row

printGrid(grid)
traverse(grid, (0,0))
# To find the path you took, simply create a point class with x and y coordinates, and also a parent coordinate. 
# Every time you append a point to next_points, pass in a point with the next search coordinates, alongwith the current point value. 
# Then, trace backwards in parent points after reaching the goal node.
