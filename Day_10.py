def part1():
    distance = [[0 for i in j] for j in inputVals]

    row = "".join(inputVals).find("S") // len(inputVals[0])
    col = "".join(inputVals).find("S") % len(inputVals[0])
    q = [(0, row, col)]
    visited = [(row, col)]

    while len(q) > 0:
        cur = q.pop(0)
        adjacent = getAdjacent(cur[1], cur[2])
        for adj in adjacent:
            if adj not in visited:
                visited.append(adj)
                distance[adj[0]][adj[1]] = cur[0] + 1
                q.append((cur[0] + 1, adj[0], adj[1]))
        q.sort()

    print("Part 1:", max([max(i) for i in distance]))

def part2():
    distance = [[0 for i in j] for j in inputVals]

    row = "".join(inputVals).find("S") // len(inputVals[0])
    col = "".join(inputVals).find("S") % len(inputVals[0])
    q = [(0, row, col)]
    visited = [(row, col)]

    while len(q) > 0:
        cur = q.pop(0)
        adjacent = getAdjacent(cur[1], cur[2])
        for adj in adjacent:
            if adj not in visited:
                visited.append(adj)
                distance[adj[0]][adj[1]] = cur[0] + 1
                q.append((cur[0] + 1, adj[0], adj[1]))
        q.sort()

    inputVals[row] = inputVals[row][:col] + "7" + inputVals[row][col + 1:]
    distance[row][col] = 1

    expanded = [["." for i in range(len(inputVals[0]) * 2 + 1)] for j in range(len(inputVals) * 2 + 1)]
    
    for i in range(len(inputVals)):
        for j in range(len(inputVals[i])):
            if distance[i][j] != 0:
                expanded[i * 2 + 1][j * 2 + 1] = "#"
            if blockedRight(i, j):
                expanded[i * 2 + 1][j * 2 + 2] = "#"
            if blockedDown(i, j):
                expanded[i * 2 + 2][j * 2 + 1] = "#"

    q = [(0, 0)]
    visited = [(0, 0)]
    while len(q) > 0:
        cur = q.pop(0)
        if expanded[cur[0]][cur[1]] != "#":
            expanded[cur[0]][cur[1]] = "O"
            if cur[0] < len(expanded) - 1 and (cur[0] + 1, cur[1]) not in visited:
                visited.append((cur[0] + 1, cur[1]))
                q.append((cur[0] + 1, cur[1]))
            if cur[1] < len(expanded[0]) - 1 and (cur[0], cur[1] + 1) not in visited:
                visited.append((cur[0], cur[1] + 1))
                q.append((cur[0], cur[1] + 1))
            if cur[0] > 0 and (cur[0] - 1, cur[1]) not in visited:
                visited.append((cur[0] - 1, cur[1]))
                q.append((cur[0] - 1, cur[1]))
            if cur[1] > 0 and (cur[0], cur[1] - 1) not in visited:
                visited.append((cur[0], cur[1] - 1))
                q.append((cur[0], cur[1] - 1))

    total = 0
    for i in range(len(inputVals)):
        for j in range(len(inputVals[0])):
            if expanded[i * 2 + 1][j * 2 + 1] == ".":
                total += 1

    #for e in expanded:
    #    print(e)
    print("Part 2:", total)

def blockedRight(row, col):
    if col == len(inputVals[0]) - 1: return False
    if inputVals[row][col] in "-LF" and inputVals[row][col + 1] in "-J7": return True
    return False

def blockedDown(row, col):
    if row == len(inputVals) - 1: return False
    if inputVals[row][col] in "|7F" and inputVals[row + 1][col] in "|LJ": return True
    return False

def getAdjacent(row, col):
    val = inputVals[row][col]
    if val == "S": canMoveTo = getAdjacentStart(row, col)
    else:
        canMoveTo = []
        if val in "|LJ": canMoveTo.append("N")
        if val in "|7F": canMoveTo.append("S")
        if val in "-LF": canMoveTo.append("E")
        if val in "-J7": canMoveTo.append("W")

    adjacent = []
    if "N" in canMoveTo and row > 0: adjacent.append((row - 1, col))
    if "S" in canMoveTo and row < len(inputVals) - 1: adjacent.append((row + 1, col))
    if "W" in canMoveTo and col > 0: adjacent.append((row, col - 1))
    if "E" in canMoveTo and col < len(inputVals[row]) - 1: adjacent.append((row, col + 1))
    return adjacent

def getAdjacentStart(row, col):
    canMoveTo = []
    if inputVals[row - 1][col] in "|7F": canMoveTo.append("N")
    if inputVals[row + 1][col] in "|LJ": canMoveTo.append("S")
    if inputVals[row][col - 1] in "-LF": canMoveTo.append("W")
    if inputVals[row][col + 1] in "-J7": canMoveTo.append("E")
    return canMoveTo

inputVals = []
f = open("Day_10_input.txt")
for line in f:
    line = line.replace("\n", "")
    inputVals.append(line)

part1()
part2()