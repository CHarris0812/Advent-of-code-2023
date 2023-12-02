def part1():
    maxRed = 12
    maxGreen = 13
    maxBlue = 14
    total = 0

    for val in inputVals:
        ID = int(val.split(": ")[0].split(" ")[1])
        turns = val.split(": ")[1].split("; ")
        valid = True

        for turn in turns:
            red = 0
            green = 0
            blue = 0

            blockTypes = turn.split(", ")
            for block in blockTypes:
                num = int(block.split(" ")[0])
                if "red" in block:
                    red = num
                if "green" in block:
                    green = num
                if "blue" in block:
                    blue = num

            if red > maxRed or green > maxGreen or blue > maxBlue:
                valid = False

        if valid: total += ID

    print("Part 1:", total)

def part2():
    total = 0

    for val in inputVals:
        turns = val.split(": ")[1].split("; ")

        red = 0
        green = 0
        blue = 0

        for turn in turns:
            blockTypes = turn.split(", ")
            for block in blockTypes:
                num = int(block.split(" ")[0])
                if "red" in block:
                    red = max(red, num)
                if "green" in block:
                    green = max(green, num)
                if "blue" in block:
                    blue = max(blue, num)

        total += red * green * blue

    print("Part 2:", total)


inputVals = []
f = open("Day_2_input.txt")
for line in f:
    inputVals.append(line[:-1])

part1()
part2()