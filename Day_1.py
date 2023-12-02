#Part 1
def part1():
    total = 0
    for val in inputVals:
        firstDigit = -1
        lastDigit = -1
        i = 0

        while firstDigit == -1:
            if val[i] in "1234567890":
                firstDigit = int(val[i])
            i += 1

        i = -1
        while lastDigit == -1:
            if val[i] in "1234567890":
                lastDigit = int(val[i])
            i -= 1

        total += firstDigit * 10 + lastDigit

    print("Part 1:", total)

def part2():
    numbersToDigits = {"one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9", "zero":"0"}
    total = 0
    for val in inputVals:
        firstDigit = -1
        lastDigit = -1
        i = 0

        for key, value in numbersToDigits.items():
            val = val.replace(key, key[0] + value + key[-1])

        while firstDigit == -1:
            if val[i] in "1234567890":
                firstDigit = int(val[i])
            i += 1

        i = -1
        while lastDigit == -1:
            if val[i] in "1234567890":
                lastDigit = int(val[i])
            i -= 1

        total += firstDigit * 10 + lastDigit

    print("Part 2:", total)

inputVals = []
f = open("Day_1_input.txt")
for line in f:
    inputVals.append(line)

part1()
part2()