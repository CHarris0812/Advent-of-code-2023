def part1():
    total = 0
    for line in inputVals:
        total += getCombinationsDP(line[0], tuple(line[1]), 0, 0, 0, {})
    print("Part 1:", total)

def part2():
    total = 0
    for line in inputVals:
        newRow = "?".join([line[0] for i in range(5)])
        total += getCombinationsDP(newRow, tuple(line[1] * 5), 0, 0, 0, {})
    print("Part 2:", total)

def getCombinations(row, groups):
    if row.count("?") == 0:
        g = getGroups(row)
        if len(g) != len(groups): return 0
        for i in range(len(g)):
            if g[i][1] - g[i][0] != groups[i]:
                return 0
        return 1
    
    pos = row.find("?")
    return getCombinations(row[:pos] + "#" + row[pos + 1:], groups) + getCombinations(row[:pos] + "." + row[pos + 1:], groups)

def getGroups(row):
    groups = []
    start = row.find("#")
    cur = start - 1
    for i in range(start, len(row)):
        if row[i] == "#": cur += 1
        else:
            if start - cur != 1:
                groups.append((start, cur + 1))
            start = i + 1
            cur = i
    if row[-1] == "#":
        groups.append((start, cur + 1))
    return groups

def getCombinationsDP(row, groups, pos, finishedGroups, positionInGroup, ways):
    if (pos, finishedGroups, positionInGroup) in ways: return ways[(pos, finishedGroups, positionInGroup)]
    if finishedGroups == len(groups):
        for i in range(pos, len(row)):
            if row[i] == "#":
                ways[(pos, finishedGroups, positionInGroup)] = 0
                return 0
        ways[(pos, finishedGroups, positionInGroup)] = 1
        return 1
    if pos >= len(row): return 0

    if row[pos] == ".": 
        if positionInGroup != 0:
            ways[(pos, finishedGroups, positionInGroup)] = 0
            return 0
        else:
            validSequences = getCombinationsDP(row, groups, pos + 1, finishedGroups, 0, ways)
            ways[(pos, finishedGroups, positionInGroup)] = validSequences
            return validSequences
    if row[pos] == "#":
        if positionInGroup == groups[finishedGroups] - 1:
            if pos < len(row) - 1 and row[pos + 1] == "#":
                ways[(pos, finishedGroups, positionInGroup)] = 0
                return 0
            validSequences = getCombinationsDP(row, groups, pos + 2, finishedGroups + 1, 0, ways)
            ways[(pos, finishedGroups, positionInGroup)] = validSequences
            return validSequences
        else:
            validSequences = getCombinationsDP(row, groups, pos + 1, finishedGroups, positionInGroup + 1, ways)
            ways[(pos, finishedGroups, positionInGroup)] = validSequences
            return validSequences
    if row[pos] == "?":
        if positionInGroup == 0:
            total = getCombinationsDP(row, groups, pos + 1, finishedGroups, 0, ways)
            if positionInGroup == groups[finishedGroups] - 1:
                if not (pos < len(row) - 1 and row[pos + 1] == "#"):
                    total += getCombinationsDP(row, groups, pos + 2, finishedGroups + 1, 0, ways)
            else:
                total += getCombinationsDP(row, groups, pos + 1, finishedGroups, positionInGroup + 1, ways)
            ways[(pos, finishedGroups, positionInGroup)] = total
            return total
        elif positionInGroup == groups[finishedGroups] - 1:
            if pos < len(row) - 1 and row[pos + 1] == "#":
                ways[(pos, finishedGroups, positionInGroup)] = 0
                return 0
            validSequences = getCombinationsDP(row, groups, pos + 2, finishedGroups + 1, 0, ways)
            ways[(pos, finishedGroups, positionInGroup)] = validSequences
            return validSequences
        else:
            validSequences = getCombinationsDP(row, groups, pos + 1, finishedGroups, positionInGroup + 1, ways)
            ways[(pos, finishedGroups, positionInGroup)] = validSequences
            return validSequences
        

inputVals = []
f = open("Day_12_input.txt")
for line in f:
    line = line.replace("\n", "")
    temp = line.split(" ")[1].split(",")
    temp = [int(i) for i in temp]
    inputVals.append([line.split(" ")[0], temp])

part1()
part2()