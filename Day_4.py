def part1():
    winners = []
    for i in inputVals:
        total = 0
        temp = i[8:]
        winner = temp.split(" | ")[0].split(" ")
        numbers = temp.split(" | ")[1].split(" ")
        for j in numbers:
            if j != "" and j in winner:
                total += 1
        
        if total == 0: winners.append(0)
        elif total == 1: winners.append(1)
        else: winners.append(2 ** (total - 1))
    
    print("Part 1:", sum(winners))

def part2():
    cards = [1 for i in inputVals]
    for i in range(len(inputVals)):
        winningNumbers = val(inputVals[i])
        for j in range(i + 1, min(i + winningNumbers + 1, len(inputVals))):
            cards[j] += cards[i]
    print("Part 2:", sum(cards))

def val(i):
    total = 0
    temp = i[8:]
    winner = temp.split(" | ")[0].split(" ")
    numbers = temp.split(" | ")[1].split(" ")
    for j in numbers:
        if j != "" and j in winner:
            total += 1
    return total

inputVals = []
f = open("Day_4_input.txt")
for line in f:
    inputVals.append(line.replace("\n", ""))

part1()
part2()