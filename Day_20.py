from math import lcm

def part1():
    lowPulses = 0
    highPulses = 0
    for x in range(1000):
        pulses = [["broadcaster", "l", "button"]]
        while len(pulses) > 0:
            cur = pulses.pop(0)
            if cur[1] == "l":
                lowPulses += 1
            else:
                highPulses += 1
            if cur[0] == "rx":
                print()

            if cur[0] not in modules: continue
            if cur[0] == "broadcaster":
                for i in modules[cur[0]][2]:
                    pulses.append([i, cur[1], cur[0]])
            elif modules[cur[0]][0] == "%":
                if cur[1] == "l":
                    pulseType = ""
                    if modules[cur[0]][1] == "off":
                        modules[cur[0]][1] = "on"
                        pulseType = "h"
                    else:
                        modules[cur[0]][1] = "off"
                        pulseType = "l"

                    for i in modules[cur[0]][2]:
                        pulses.append([i, pulseType, cur[0]])
            else:
                modules[cur[0]][1][cur[2]] = cur[1]
                allHigh = True
                for i in modules[cur[0]][1]:
                    if modules[cur[0]][1][i] == "l":
                        allHigh = False

                if allHigh: pulseType = "l"
                else: pulseType = "h"
                for i in modules[cur[0]][2]:
                    pulses.append([i, pulseType, cur[0]])

    
    print("Part 1:", lowPulses * highPulses)

def part2():
    lowPulses = 0
    highPulses = 0
    for x in range(100000):
        pulses = [["broadcaster", "l", "button"]]
        while len(pulses) > 0:
            cur = pulses.pop(0)
            if cur[0] == "nc" and cur[1] == "h":
                print(x + 1, cur[2])
            #if cur[0] == "rx":
            #    print(x)
            #    if cur[1] == "l":
            #        print("Part 2:", x + 1)
            #        return

            if cur[0] not in modules: continue
            if cur[0] == "broadcaster":
                for i in modules[cur[0]][2]:
                    pulses.append([i, cur[1], cur[0]])
            elif modules[cur[0]][0] == "%":
                if cur[1] == "l":
                    pulseType = ""
                    if modules[cur[0]][1] == "off":
                        modules[cur[0]][1] = "on"
                        pulseType = "h"
                    else:
                        modules[cur[0]][1] = "off"
                        pulseType = "l"

                    for i in modules[cur[0]][2]:
                        pulses.append([i, pulseType, cur[0]])
            else:
                modules[cur[0]][1][cur[2]] = cur[1]
                allHigh = True
                for i in modules[cur[0]][1]:
                    if modules[cur[0]][1][i] == "l":
                        allHigh = False

                if allHigh: pulseType = "l"
                else: pulseType = "h"
                for i in modules[cur[0]][2]:
                    pulses.append([i, pulseType, cur[0]])

modules = {}
f = open("Day_20_input.txt")
for line in f:
    line = line.replace("\n", "")
    name = line.split(" -> ")[0]
    t = ""
    if name == "broadcaster":
        t = "b"
    else:
        t = name[0]
        name = name[1:]

    connections = line.split(" -> ")[1].replace(",", "").split(" ")
    if t == "%":
        modules[name] = [t, "off", connections]
    else:
        modules[name] = [t, {}, connections]

for i in modules:
    for j in modules[i][2]:
        if j in modules:
            if modules[j][0] == "&":
                modules[j][1][i] = "l"

#part1()
part2()
print(lcm(3847, 3851, 4003, 4027))