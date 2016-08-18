# Given a circular array, of relative indices, find if it has a single commplete cycle.
circularArray = [1, -2, 1]

def isCyclical(circularArray):
    indexDictionary = {}
    for i in range(len(circularArray)):
        indexDictionary[i] = False
    currentIndex = 0
    iterationNumber = 0
    while iterationNumber <= len(circularArray):
        if iterationNumber > 0:
            indexDictionary[currentIndex] = True
        currentIndex = (currentIndex + circularArray[currentIndex]) % len(circularArray) 
        iterationNumber += 1
    for key in indexDictionary:
        if indexDictionary[key] == False:
            return False
    return True

print isCyclical(circularArray)



def hasSingleCompleteCycle(offset):
    visited = set()
    startPosition = 0
    position = startPosition
    while not foundCycle(position, visited):  # TODO
        # Guaranteed to find cycle in <= len(offsets).
        visited.add(position)
        position = step(position, offset)  # TODO
    return visitedAll(visited, offset) and position == startPosition  # TODO

def foundCycle(position, visited):
    return position in visited

def step(position, offset):
    return (position + offset[position]) % len(offset)

def visitedAll(visited, offset):
    return len(visited) == len(offset)

print hasSingleCompleteCycle(circularArray)

