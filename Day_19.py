def part1():
    total = 0
    for p in parts:
        x = p[0]
        m = p[1]
        a = p[2]
        s = p[3]
        cur = "in"
        accepted = 0

        while accepted == 0:
            for i in workflows[cur]:
                if len(i) == 1:
                    if i[0] == "A":
                        total += sum(p)
                        accepted = 1
                    elif i[0] == "R":
                        accepted = -1
                    else:
                        cur = i[0]
                    break
                elif eval(i[0]):
                    cur = i[1]
                    if cur == "A":
                        total += sum(p)
                        accepted = 1
                    elif cur == "R":
                        accepted = -1
                    break
    
    print("Part 1:", total)

def part2():
    unknown = [["in", [1, 4001], [1, 4001], [1, 4001], [1, 4001]]]
    accepted = 0
    lettersToPositions = {"x":0, "m":1, "a":2, "s":3}
    while len(unknown) > 0:
        temp = unknown.pop(0)
        cur = temp[0]
        if cur == "A":
            numberAccepted = 1
            for j in temp[1:]:
                numberAccepted *= (j[1] - j[0])
            accepted += numberAccepted
            continue
        elif cur == "R":
            continue


        temp = [temp]
        for i in workflows[cur]:
            if len(i) == 1:
                for j in temp:
                    unknown.append([i[0], j[1], j[2], j[3], j[4]])
                break

            necessaryVal = int(i[0][2:])
            greaterOrLess = i[0][1]
            component = lettersToPositions[i[0][0]]

            if greaterOrLess == "<":
                for k in temp:
                    if k[component + 1][0] < necessaryVal:
                        toAppend = [i[1], [k[1][0], k[1][1]], [k[2][0], k[2][1]], [k[3][0], k[3][1]], [k[4][0], k[4][1]]]
                        toAppend[component + 1][1] = min(necessaryVal, k[component + 1][1])
                        if k[component + 1][1] < necessaryVal:
                            for j in range(4):
                                k[j + 1][0] = 4000
                                k[j + 1][1] = 0
                        else:
                            k[component + 1][0] = necessaryVal
                        unknown.append(toAppend)
            else:
                for k in temp:
                    if k[component + 1][1] > necessaryVal:
                        toAppend = [i[1], [k[1][0], k[1][1]], [k[2][0], k[2][1]], [k[3][0], k[3][1]], [k[4][0], k[4][1]]]
                        toAppend[component + 1][0] = max(necessaryVal + 1, k[component + 1][0])
                        if k[component + 1][0] > necessaryVal:
                            for j in range(4):
                                k[j + 1][0] = 4000
                                k[j + 1][1] = 0
                        else:
                            k[component + 1][1] = necessaryVal + 1
                        unknown.append(toAppend)
    print("Part 2:", accepted)



workflows = {}
parts = []
switchedToParts = False
f = open("Day_19_input.txt")
for line in f:
    if line == "\n":
        switchedToParts = True
        continue

    line = line.replace("\n", "")
    if switchedToParts:
        line = line.replace("{", "")
        line = line.replace("}", "")
        line = line.split(",")
        parts.append([int(i[2:]) for i in line])
    else:
        label = line.split("{")[0]
        line = line.split("{")[1]
        line = line.replace("}", "")
        line = line.split(",")
        workflows[label] = [i.split(":") for i in line]
part1()
part2()