import copy

def part1():
    frontier = [(0, 1, 0, [(0, 1)])]
    goal = (len(inputVals) - 1, len(inputVals[0]) - 2)
    longest = 0
    graph = buildGraph(goal)
    while len(frontier) > 0:
        cur = frontier.pop(0)
        neighbors = graph[(cur[0], cur[1])]
        for n in neighbors:
            if (n[0], n[1]) not in cur[3]:
                temp = cur[3] + [(n[0], n[1])]
                if (n[0], n[1]) == goal:
                    longest = max(longest, cur[2] + n[2])
                else:
                    frontier.append((n[0], n[1], cur[2] + n[2], temp))
                    
    print("Part 1:", longest)

def part2():
    frontier = [(0, 1, 0, [(0, 1)])]
    goal = (len(inputVals) - 1, len(inputVals[0]) - 2)
    longest = 0
    graph = buildGraph2(goal)
    while len(frontier) > 0:
        frontier.sort()
        cur = frontier.pop(0)
        neighbors = graph[(cur[2], cur[1])]
        for n in neighbors:
            if (n[0], n[1]) not in cur[3]:
                temp = cur[3] + [(n[0], n[1])]
                if (n[0], n[1]) == goal:
                    longest = min(longest, cur[0] + n[2])
                    print(-1 * longest)
                    
                else:
                    frontier.append((cur[0] + n[2], n[1], n[0], temp))
                    
    print("Part 2:", longest)

def getIntersections(goal):
    intersections = [(0, 1), goal]
    for i in range(len(inputVals)):
        for j in range(len(inputVals[0])):
            if getNeighboringDots(i, j) > 2:
                intersections.append((i, j))
    return intersections

def getNeighboringDots(row, col):
    count = 0
    if inputVals[row][col] == "#": return 0
    if row > 0:
        if inputVals[row - 1][col] != "#":
            count += 1
    if row < len(inputVals) - 1:
        if inputVals[row + 1][col] != "#":
            count += 1
    if col > 0:
        if inputVals[row][col - 1] != "#":
            count += 1
    if col < len(inputVals[0]) - 1:
        if inputVals[row][col + 1] != "#":
            count += 1
    return count

def getPaths(row, col, intersections):
    frontier = [(row, col, 0)]
    visited = {(row, col)}
    canVisit = []
    while len(frontier) > 0:
        cur = frontier.pop(0)
        neighbors = getNeighbors(cur[0], cur[1])
        for n in neighbors:
            if n not in visited:
                visited.add(n)
                if n in intersections:
                    canVisit.append((n[0], n[1], cur[2] + 1))
                else:
                    frontier.append((n[0], n[1], cur[2] + 1))
    return canVisit

def getPaths2(row, col, intersections):
    frontier = [(row, col, 0)]
    visited = {(row, col)}
    canVisit = []
    while len(frontier) > 0:
        cur = frontier.pop(0)
        neighbors = getNeighbors2(cur[0], cur[1])
        for n in neighbors:
            if n not in visited:
                visited.add(n)
                if n in intersections:
                    canVisit.append((n[0], n[1], cur[2] - 1))
                else:
                    frontier.append((n[0], n[1], cur[2] - 1))
    return canVisit

def getNeighbors(row, col):
    neighbors = []
    if row > 0:
        if inputVals[row - 1][col] in ".^":
            neighbors.append((row - 1, col))
    if row < len(inputVals) - 1:
        if inputVals[row + 1][col] in ".v":
            neighbors.append((row + 1, col))
    if col > 0:
        if inputVals[row][col - 1] in ".<":
            neighbors.append((row, col - 1))
    if col < len(inputVals[0]) - 1:
        if inputVals[row][col + 1] in ".>":
            neighbors.append((row, col + 1))
    return neighbors

def getNeighbors2(row, col):
    neighbors = []
    if row > 0:
        if inputVals[row - 1][col] != "#":
            neighbors.append((row - 1, col))
    if row < len(inputVals) - 1:
        if inputVals[row + 1][col] != "#":
            neighbors.append((row + 1, col))
    if col > 0:
        if inputVals[row][col - 1] != "#":
            neighbors.append((row, col - 1))
    if col < len(inputVals[0]) - 1:
        if inputVals[row][col + 1] != "#":
            neighbors.append((row, col + 1))
    return neighbors

def buildGraph(goal):
    intersections = getIntersections(goal)
    graph = {}
    for intersection in intersections:
        graph[intersection] = getPaths(intersection[0], intersection[1], intersections)
    return graph

def buildGraph2(goal):
    intersections = getIntersections(goal)
    graph = {}
    for intersection in intersections:
        graph[intersection] = getPaths2(intersection[0], intersection[1], intersections)

    return graph

inputVals = []
f = open("Day_23_input.txt")
for line in f:
    line = line.replace("\n", "")
    inputVals.append([i for i in line])

dp = {}

part1()
part2()