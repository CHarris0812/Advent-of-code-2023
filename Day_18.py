def part1():
    digSite = [["." for i in range(1000)] for j in range(1000)]
    cur = [500, 500]
    digSite[cur[0]][cur[1]] = "#"
    for direction in inputVals:
        for i in range(int(direction[1])):
            cur = getNext(cur, direction[0])
            digSite[cur[0]][cur[1]] = "#"

    for i in range(len(digSite)):
        if digSite[i][0] == ".":
            digSite = fill(digSite, i, 0)
        if digSite[i][len(digSite) - 1] == ".":
            digSite = fill(digSite, i, len(digSite) - 1)

    for i in range(len(digSite[0])):
        if digSite[0][i] == ".":
            digSite = fill(digSite, 0, i)
        if digSite[len(digSite) - 1][i] == ".":
            digSite = fill(digSite, len(digSite) - 1, i)

    total = 0
    for i in digSite:
        total += i.count("#") + i.count(".")
    print("Part 1:", total)

def getNext(cur, direction):
    if direction == "U": return [cur[0] - 1, cur[1]]
    if direction == "D": return [cur[0] + 1, cur[1]]
    if direction == "L": return [cur[0], cur[1] - 1]
    if direction == "R": return [cur[0], cur[1] + 1]

def fill(digSite, row, col):
    frontier = [(row, col)]
    visited = set()
    visited.add((row, col))
    while len(frontier) > 0:
        temp = frontier.pop(0)
        if digSite[temp[0]][temp[1]] == ".":
            digSite[temp[0]][temp[1]] = "X"
            cur = getNeighbors(digSite, temp[0], temp[1])
            for i in cur:
                if i not in visited:
                    visited.add(i)
                    frontier.append(i)
    return digSite

def getNeighbors(digSite, row, col):
    n = []
    if row > 0:
        n.append((row - 1, col))
    if row < len(digSite) - 1:
        n.append((row + 1, col))
    if col > 0:
        n.append((row, col - 1))
    if col < len(digSite[0]) - 1:
        n.append((row, col + 1))
    return n

def convert(hex):
    return int(hex, 16)

def part2():
    points = [[0, 0]]
    cur = [0, 0]
    for i in inputVals:
        dist = convert(i[2][2:-2])
        direction = int(i[2][-2])
        if direction == 0:
            cur = [cur[0], cur[1] + dist]
        if direction == 1:
            cur = [cur[0] + dist, cur[1]]
        if direction == 2:
            cur = [cur[0], cur[1] - dist]
        if direction == 3:
            cur = [cur[0] - dist, cur[1]]
        points.append(cur)
    area = calcArea(points)
    boundaryPoints = 0
    points.append([0, 0])
    for i in range(len(points) - 1):
        boundaryPoints += abs(points[i][0] - points[i + 1][0]) + abs(points[i][1] - points[i + 1][1])
    interiorPoints = abs(area + 1 - (boundaryPoints / 2))
    print("Part 2:", int(interiorPoints + boundaryPoints))

def calcArea(points):
    area = 0
    for i in range(1, len(points) - 1):
        area += points[i][0] * (points[i + 1][1] - points[i - 1][1])
    return area / 2

inputVals = []
f = open("Day_18_input.txt")
for line in f:
    line = line.replace("\n", "")
    inputVals.append(line.split(" "))
    
part1()
part2()