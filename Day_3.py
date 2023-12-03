def part1():
    cur = ""
    curStart = -1
    total = 0
    nextToSymbol = False
    for i in range(len(inputVals)):
        for j in range(len(inputVals[0])):
            if inputVals[i][j] in "1234567890":
                cur += inputVals[i][j]
                if curStart == -1: curStart = j
            else:
                if cur != "":
                    for k in range(curStart, j):
                        if adjacent(i, k): nextToSymbol = True
                    if nextToSymbol: 
                        total += int(cur)
                    cur = ""
                    curStart = -1
                    nextToSymbol = False

        if cur != "":
            for k in range(curStart, len(inputVals[0])):
                if adjacent(i, k): nextToSymbol = True
            if nextToSymbol: total += int(cur)
            cur = ""
            curStart = -1
            nextToSymbol = False
    print("Part 1:", total)

def adjacent(row, col):
    symbols = "+-*/@#%$=&"
    if (row > 0 and inputVals[row - 1][col] in symbols) or (row < len(inputVals) - 1 and inputVals[row + 1][col] in symbols):
        return True
    if (col > 0 and inputVals[row][col - 1] in symbols) or (col < len(inputVals[0]) - 1 and inputVals[row][col + 1] in symbols):
        return True
    if row > 0 and col > 0 and inputVals[row - 1][col - 1] in symbols:
        return True
    if row > 0 and col < len(inputVals[0]) - 1 and inputVals[row - 1][col + 1] in symbols:
        return True
    if row < len(inputVals) - 1 and col > 0 and inputVals[row + 1][col - 1] in symbols:
        return True
    if row < len(inputVals) - 1 and col < len(inputVals[0]) - 1 and inputVals[row + 1][col + 1] in symbols:
        return True
    return False

def part2():
    modifiedInputs = replaceInputsWithNumber()
    total = 0
    for i in range(len(inputVals)):
        for j in range(len(inputVals[0])):
            if modifiedInputs[i][j] == "*":
                total += adjacencyScore(i, j, modifiedInputs)
    print("Part 2:", total)

def replaceInputsWithNumber():
    newInputVals = [[j for j in i] for i in inputVals]
    cur = ""
    curStart = -1
    for i in range(len(inputVals)):
        for j in range(len(inputVals[0])):
            if inputVals[i][j] in "1234567890":
                cur += inputVals[i][j]
                if curStart == -1: curStart = j
            else:
                if cur != "":
                    for k in range(curStart, j):
                        newInputVals[i][k] = cur
                    cur = ""
                    curStart = -1

        if cur != "":
            for k in range(curStart, j):
                newInputVals[i][k] = cur
            cur = ""
            curStart = -1
    return newInputVals

def adjacencyScore(row, col, inp):
    adjacencies = []
    if col > 0 and inp[row][col - 1].isdigit():
        adjacencies.append(inp[row][col - 1])
    if col < len(inp[0]) - 1 and inp[row][col + 1].isdigit():
        adjacencies.append(inp[row][col + 1])
    if row > 0:
        if col > 0:
            if inp[row - 1][col - 1].isdigit():
                adjacencies.append(inp[row - 1][col - 1])
        if inp[row - 1][col].isdigit() and (col == 0 or not inp[row - 1][col - 1].isdigit()):
            adjacencies.append(inp[row - 1][col])
        if col < len(inp[0]) - 1:
            if inp[row - 1][col + 1].isdigit() and not inp[row - 1][col].isdigit():
                adjacencies.append(inp[row - 1][col + 1])
    if row < len(inp) - 1:
        if col > 0:
            if inp[row + 1][col - 1].isdigit():
                adjacencies.append(inp[row + 1][col - 1])
        if inp[row + 1][col].isdigit() and (col == 0 or not inp[row + 1][col - 1].isdigit()):
            adjacencies.append(inp[row + 1][col])
        if col < len(inp[0]) - 1:
            if inp[row + 1][col + 1].isdigit() and not inp[row + 1][col].isdigit():
                adjacencies.append(inp[row + 1][col + 1])

    if len(adjacencies) == 2:
        return int(adjacencies[0]) * int(adjacencies[1])
    return 0

inputVals = []
f = open("Day_3_input.txt")
for line in f:
    inputVals.append(line.replace("\n", ""))

part1()
part2()