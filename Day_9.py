def part1():
    total = 0
    for val in inputVals:
        total += getNext(val)
    print("Part 1:", total)

def part2():
    total = 0
    for val in inputVals:
        total += getNext(val[::-1])
    print("Part 2:", total)

def getNext(val):
    if sum([0 if i == 0 else 1 for i in val]) == 0: return 0
    difference = [val[i] - val[i - 1] for i in range(1, len(val))]
    return val[-1] + getNext(difference)



inputVals = []
f = open("Day_9_input.txt")
for line in f:
    line = line.replace("\n", "").split(" ")
    line = [int(i) for i in line]
    inputVals.append(line)

part1()
part2()