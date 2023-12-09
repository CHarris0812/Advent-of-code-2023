from math import ceil, floor, sqrt


def part1():
    ways = [0 for i in times]
    for i in range(len(times)):
        for j in range(times[i]):
            if findDistance(j, times[i]) > distances[i]:
                ways[i] += 1
    
    total = 1
    for i in ways:
        total *= i

    print("Part 1", total)

def part2():
    time = ""
    distance = ""
    for i in range(len(times)):
        time += str(times[i])
        distance += str(distances[i])
    time = int(time)
    distance = int(distance)


    x = (-1 * time + sqrt(time * time - 4 * -1 * -1 * distance)) / -2
    y = (-1 * time - sqrt(time * time - 4 * -1 * -1 * distance)) / -2
    print("Part 2", int(y - x))

    ways = 0
    for i in range(time):
        if findDistance(i, time) > distance:
            ways += 1
    print(ways)
    #hold * time - hold * hold = distance


def findDistance(hold, time):
    return hold * (time - hold)

inputVals = []
f = open("Day_6_input.txt")
for line in f:
    inputVals.append(line.replace("\n", ""))

t = inputVals[0][5:].split(" ")
d = inputVals[1][10:].split(" ")

times = []
for i in t:
    if i != "":
        times.append(int(i))

distances = []
for i in d:
    if i != "":
        distances.append(int(i))

part1()
part2()