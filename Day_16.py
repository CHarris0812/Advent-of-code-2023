import time

def part1():
    t = time.time()
    frontier = [(0, 0, "r")]
    energized = [[0 for j in i] for i in inputVals]
    visited = set()
    while len(frontier) > 0:
        row, col, direction = frontier.pop(0)
        if (row, col, direction) in visited:
            continue
        visited.add((row, col, direction))
        energized[row][col] = 1
        if inputVals[row][col] == ".":
            nextPlace = getNextEmpty(row, col, direction)
            if nextPlace and nextPlace not in visited:
                frontier.append(nextPlace)
        elif inputVals[row][col] in "-|":
            for i in getNextSplitter(row, col, direction):
                if i not in visited:
                    frontier.append(i)
        else:
            nextPlace = getNextMirror(row, col, direction)
            if nextPlace and nextPlace not in visited:
                frontier.append(nextPlace)

    total = 0
    for i in energized:
        for j in i:
            if j != 0:
                total += 1
                
    print("Part 1:", total)
    print(time.time() - t)

def part2():
    maxVal = 0
    for i in range(len(inputVals)):
        maxVal = max(maxVal, getEnergized((i, 0, "r")))
        maxVal = max(maxVal, getEnergized((i, len(inputVals[0]) - 1, "l")))

    for i in range(len(inputVals[0])):
        maxVal = max(maxVal, getEnergized((0, i, "d")))
        maxVal = max(maxVal, getEnergized((len(inputVals) - 1, i, "u")))
    print("Part 2:", maxVal)

def getEnergized(start):
    frontier = [start]
    energized = [[0 for j in i] for i in inputVals]
    visited = set()
    while len(frontier) > 0:
        row, col, direction = frontier.pop(0)
        if (row, col, direction) in visited:
            continue
        visited.add((row, col, direction))
        energized[row][col] = 1
        if inputVals[row][col] == ".":
            nextPlace = getNextEmpty(row, col, direction)
            if nextPlace and nextPlace not in visited:
                frontier.append(nextPlace)
        elif inputVals[row][col] in "-|":
            for i in getNextSplitter(row, col, direction):
                if i not in visited:
                    frontier.append(i)
        else:
            nextPlace = getNextMirror(row, col, direction)
            if nextPlace and nextPlace not in visited:
                frontier.append(nextPlace)

    total = 0
    for i in energized:
        for j in i:
            if j != 0:
                total += 1
    return total

def getNextEmpty(row, col, direction):
    if direction == "l":
        if col > 0:
            return (row, col - 1, direction)
        else:
            return None
        
    if direction == "r":
        if col < len(inputVals[0]) - 1:
            return (row, col + 1, direction)
        else:
            return None
        
    if direction == "u":
        if row > 0:
            return (row - 1, col, direction)
        else:
            return None
        
    if direction == "d":
        if row < len(inputVals) - 1:
            return (row + 1, col, direction)
        else:
            return None

def getNextSplitter(row, col, direction):
    if (inputVals[row][col] == "|" and direction in "ud") or (inputVals[row][col] == "-" and direction in "lr"):
        temp = getNextEmpty(row, col, direction)
        if temp == None:
            return []
        else:
            return [temp]
    if inputVals[row][col] == "|":
        return [(row, col, "u"), (row, col, "d")]
    else:
        return [(row, col, "l"), (row, col, "r")]

def getNextMirror(row, col, direction):
    new = {"u":"l", "r":"d", "d":"r", "l":"u"}
    if inputVals[row][col] == "\\":
        newDir = new[direction]
        return getNextEmpty(row, col, newDir)

    new = {"u":"r", "r":"u", "d":"l", "l":"d"}
    if inputVals[row][col] == "/":
        newDir = new[direction]
        return getNextEmpty(row, col, newDir)

inputVals = []
f = open("Day_16_input.txt")
for line in f:
    line = line.replace("\n", "")
    inputVals.append([i for i in line])
    
part1()
part2()