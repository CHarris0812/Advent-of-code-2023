def part1():
    emptyRows = [1 if i == "." * len(i) else 0 for i in inputVals]
    emptyCols = []
    for i in range(len(inputVals[0])):
        empty = True
        for j in range(len(inputVals)):
            if inputVals[j][i] != ".": empty = False
        if empty: 
            emptyCols.append(1)
        else:
            emptyCols.append(0)
            
    emptyRowsPassed = 0
    emptyColsPassed = 0
    galaxys = []

    for i in range(len(inputVals)):
        if emptyRows[i] == 1: emptyRowsPassed += 1
        emptyColsPassed = 0
        for j in range(len(inputVals[i])):
            if emptyCols[j] == 1: emptyColsPassed += 1
            if inputVals[i][j] == "#":
                galaxys.append((i + emptyRowsPassed, j + emptyColsPassed))
    
    totalDist = 0
    for i in range(len(galaxys)):
        for j in range(i + 1, len(galaxys)):
            totalDist += abs(galaxys[i][0] - galaxys[j][0]) + abs(galaxys[i][1] - galaxys[j][1])

    print("Part 1:", totalDist)


def part2():
    emptyRows = [1 if i == "." * len(i) else 0 for i in inputVals]
    emptyCols = []
    for i in range(len(inputVals[0])):
        empty = True
        for j in range(len(inputVals)):
            if inputVals[j][i] != ".": empty = False
        if empty: 
            emptyCols.append(1)
        else:
            emptyCols.append(0)
            
    emptyRowsPassed = 0
    emptyColsPassed = 0
    galaxys = []

    for i in range(len(inputVals)):
        if emptyRows[i] == 1: emptyRowsPassed += 1000000 - 1
        emptyColsPassed = 0
        for j in range(len(inputVals[i])):
            if emptyCols[j] == 1: emptyColsPassed += 1000000 - 1
            if inputVals[i][j] == "#":
                galaxys.append((i + emptyRowsPassed, j + emptyColsPassed))
    
    totalDist = 0
    for i in range(len(galaxys)):
        for j in range(i + 1, len(galaxys)):
            totalDist += abs(galaxys[i][0] - galaxys[j][0]) + abs(galaxys[i][1] - galaxys[j][1])
    print("Part 2:", totalDist)


inputVals = []
f = open("Day_11_input.txt")
for line in f:
    line = line.replace("\n", "")
    inputVals.append(line)

part1()
part2()