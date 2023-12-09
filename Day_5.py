def part1():
    for i in range(7):
        for j in things[i]:
            things[i + 1].append(map(maps[i], j))
    print("Part 1:", min(things[7]))

def map(map, val):
    for j in map:
        if val >= j[1] and val <= j[1] + j[2]:
            dif = val - j[1]
            return j[0] + dif
    return val

def part2():
    things = [[] for i in range(8)]
    things[0] = seeds
    for i in range(7):
        print(things[i])
        print(maps[i])
        for j in range(len(things[i]) // 2):
            if not things[i][j * 2 + 1] == 0:
                things[i + 1] += mapRange(maps[i], things[i][j * 2], things[i][j * 2 + 1])

    things[7] = [things[7][i] if i % 2 == 0 else 10000000000000 for i in range(len(things[7]))]
    things[7] = [i if i != 0 else 10000000000000 for i in things[7]]
    print("Part 2:", min(things[7]))

def mapRange(map, val, count):
    results = [val, count]
    for i in map:
        if val + count >= i[1] and val <= i[1] + i[2]:
            dif = i[1] - i[0]
            start = max(i[1], val)
            rangee = min(i[1] + i[2], val + count) - start
            
            for j in range(len(results) // 2):
                if start <= results[j * 2] and start + rangee >= results[j * 2] + results[j * 2 + 1]: #clear whole thing
                    results[j * 2] = 0
                    results[j * 2 + 1] = 0
                elif start <= results[j * 2] and start + rangee >= results[j * 2]: #clear start
                    new = start + rangee
                    results[j * 2 + 1] -= (new - results[j * 2])
                    results[j * 2] = new
                elif start <= results[j * 2] + results[j * 2 + 1] and start + rangee >= results[j * 2] + results[j * 2 + 1]: #clear end
                    maxVal = results[j * 2] + results[j * 2 + 1]
                    results[j * 2 + 1] = count - (maxVal - start)
                elif start <= results[j * 2] + results[j * 2 + 1] and start + rangee >= results[j * 2]:
                    newEnd = start - results[j * 2]
                    newStart2 = start + rangee
                    newEnd2 = results[j * 2 + 1] + results[j * 2] - start - rangee
                    results[j * 2 + 1] = newEnd
                    results.append(newStart2)
                    results.append(newEnd2)

            results.append(start - dif)
            results.append(rangee)
            
    return results


maps = [[] for i in range(7)]
things = [[] for i in range(8)]

passed = 0
f = open("Day_5_input.txt")
for line in f:
    line = line.replace("\n", "")
    if line == "": 
        passed += 1
        continue
    if "-" in line: continue
    if passed == 0:
        things[0] = line.split(": ")[1].split(" ")
        things[0] = [int(i) for i in things[0]]
    else:
        temp = line.split(" ")
        temp = [int(i) for i in temp]
        maps[passed - 1].append(temp)

seeds = things[0]
part1()
part2()