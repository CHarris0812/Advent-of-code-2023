def part1():
    frontier = [(0, 0, 0, "r", 0), (0, 0, 0, "d", 0)]
    visited = set()
    goal = (len(inputVals) - 1, len(inputVals[0]) - 1)
    minDist = [[-1 for i in j] for j in inputVals]
    while len(frontier) > 0:
        frontier.sort()
        cost, row, col, direction, movedAlready = frontier.pop(0)
        minDist[row][col] = cost
        if (row, col) == goal:
            #for i in minDist:
            #    print(i)
            print("Part 1:", cost)
            break

        if movedAlready < 3:
            temp = getNext(cost, row, col, direction, movedAlready)
            if temp and (temp[1], temp[2], temp[3], temp[4]) not in visited:
                visited.add((temp[1], temp[2], temp[3], temp[4]))
                frontier.append(temp)

        otherOptions = getOptions(cost, row, col, direction)
        for i in otherOptions:
            if (i[1], i[2], i[3], i[4]) not in visited:
                frontier.append(i)
                visited.add((i[1], i[2], i[3], i[4]))

def part2():
    frontier = [(0, 0, 0, "r", 0), (0, 0, 0, "d", 0)]
    visited = set()
    goal = (len(inputVals) - 1, len(inputVals[0]) - 1)
    minDist = [[-1 for i in j] for j in inputVals]
    while len(frontier) > 0:
        frontier.sort()
        cost, row, col, direction, movedAlready = frontier.pop(0)
        minDist[row][col] = cost
        if (row, col) == goal:
            if movedAlready > 3:
                #for i in minDist:
                #    print(i)
                print("Part 2:", cost)
                break

        if movedAlready < 10:
            temp = getNext(cost, row, col, direction, movedAlready)
            if temp and (temp[1], temp[2], temp[3], temp[4]) not in visited:
                visited.add((temp[1], temp[2], temp[3], temp[4]))
                frontier.append(temp)

        if movedAlready > 3:
            otherOptions = getOptions(cost, row, col, direction)
            for i in otherOptions:
                if (i[1], i[2], i[3], i[4]) not in visited:
                    frontier.append(i)
                    visited.add((i[1], i[2], i[3], i[4]))

def getNext(cost, row, col, direction, movedAlready):
    if direction == "l":
        if col > 0:
            return (cost + inputVals[row][col - 1], row, col - 1, direction, movedAlready + 1)
    if direction == "r":
        if col < len(inputVals[0]) - 1:
            return (cost + inputVals[row][col + 1], row, col + 1, direction, movedAlready + 1)
    if direction == "u":
        if row > 0:
            return (cost + inputVals[row - 1][col], row - 1, col, direction, movedAlready + 1)
    if direction == "d":
        if row < len(inputVals) - 1:
            return (cost + inputVals[row + 1][col], row + 1, col, direction, movedAlready + 1)
    return None

def getOptions(cost, row, col, direction):
    temp = []
    if direction in "lr":
        x = getNext(cost, row, col, "u", 0)
        if x:
            temp.append(x)
        x = getNext(cost, row, col, "d", 0)
        if x:
            temp.append(x)
    else:
        x = getNext(cost, row, col, "l", 0)
        if x:
            temp.append(x)
        x = getNext(cost, row, col, "r", 0)
        if x:
            temp.append(x)
    return temp

inputVals = []
f = open("Day_17_input.txt")
for line in f:
    line = line.replace("\n", "")
    inputVals.append([int(i) for i in line])
    
#part1()
part2()