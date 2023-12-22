import copy

def part1():
    finalPlacements = [[[0 for i in range(300)] for j in range(10)] for k in range(10)]
    endBlocks = []
    for i in inputVals:
        start = i[1]
        end = i[2]
        while canMoveDown(start, end, finalPlacements):
            start[2] -= 1
            end[2] -= 1
        finalPlacements = add(start, end, finalPlacements)
        endBlocks.append([start, end])

    canBeRemoved = 0
    for i in endBlocks:
        start = i[0]
        end = i[1]
        tempPos = [[[k for k in j] for j in l] for l in finalPlacements]
        for j in range(start[0], end[0] + 1):
            for k in range(start[1], end[1] + 1):
                for l in range(start[2], end[2] + 1):
                    tempPos[j][k][l] = 0

        valid = 1
        for j in endBlocks:
            if canMoveDown(j[0], j[1], tempPos): valid = 0
        canBeRemoved += valid
    print("Part 1:", canBeRemoved)


def part2():
    finalPlacements = [[[0 for i in range(300)] for j in range(10)] for k in range(10)]
    endBlocks = []
    for i in inputVals:
        start = i[1]
        end = i[2]
        while canMoveDown(start, end, finalPlacements):
            start[2] -= 1
            end[2] -= 1
        
        finalPlacements = add(start, end, finalPlacements)
        endBlocks.append([start, end])

        
    canBeRemoved = 0
    for i in endBlocks:
        start = i[0]
        end = i[1]
        canBeRemoved += doThings(copy.deepcopy(endBlocks), copy.deepcopy(start), copy.deepcopy(end), copy.deepcopy(finalPlacements))
    print("Part 2:", canBeRemoved)

def doThings(endBlocks, start, end, finalPlacements):
    tempPos = clear(start, end, finalPlacements)

    canBeRemoved = 0
    for j in endBlocks:
        if canMoveDown(j[0], j[1], tempPos):
            canBeRemoved += 1
            tempPos = clear(j[0], j[1], tempPos)
            while canMoveDown(j[0], j[1], tempPos):
                j[0][2] -= 1
                j[1][2] -= 1
            tempPos = add(j[0], j[1], tempPos)
    return canBeRemoved

def clear(start, end, arr):
    for j in range(start[0], end[0] + 1):
            for k in range(start[1], end[1] + 1):
                for l in range(start[2], end[2] + 1):
                    arr[j][k][l] = 0
    return arr

def add(start, end, arr):
    for j in range(start[0], end[0] + 1):
            for k in range(start[1], end[1] + 1):
                for l in range(start[2], end[2] + 1):
                    arr[j][k][l] = 1
    return arr

def canMoveDown(start, end, finalPlacements):
    for i in range(start[0], end[0] + 1):
        for j in range(start[1], end[1] + 1):
            if start[2] == 0 or finalPlacements[i][j][start[2] - 1] != 0: return False
    return True

inputVals = []
f = open("Day_22_input.txt")
for line in f:
    line = line.replace("\n", "")
    temp = [i.split(",") for i in line.split("~")]
    temp = [[int(i) for i in j] for j in temp]
    temp = [min(temp[0][2], temp[1][2])] + temp
    inputVals.append(temp)
inputVals.sort()

part1()
part2()