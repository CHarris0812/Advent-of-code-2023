def part1():
    hands = []
    for i in inputVals:
        hands.append([0, i.split(" ")[0], i.split(" ")[1]])

    vals = {"A":14, "K":13, "Q":12, "J":11, "T":10}
    for i in range(10):
        vals[str(i)] = i

    for h in range(len(hands)):
        val = getRank(hands[h][1])
        newVal = val * 10000000000 + vals[hands[h][1][0]] * 100000000 + vals[hands[h][1][1]] * 1000000 + vals[hands[h][1][2]] * 10000 + vals[hands[h][1][3]] * 100 + vals[hands[h][1][4]]
        hands[h][0] = newVal

    total = 0
    for i in range(len(hands), 0, -1):
        maxNum = maxVal(hands)
        total += i * int(hands[maxNum][2])
        hands[maxNum][0] = 0
    
    print("Part 1:", total)

def part2():
    hands = []
    for i in inputVals:
        hands.append([0, i.split(" ")[0], i.split(" ")[1]])

    vals = {"A":14, "K":13, "Q":12, "J":0, "T":10}
    for i in range(10):
        vals[str(i)] = i

    for h in range(len(hands)):
        val = getRank(hands[h][1])

        perms = permutations(hands[h][1])
        for p in perms:
            val = max(val, getRank(p))


        newVal = val * 10000000000 + vals[hands[h][1][0]] * 100000000 + vals[hands[h][1][1]] * 1000000 + vals[hands[h][1][2]] * 10000 + vals[hands[h][1][3]] * 100 + vals[hands[h][1][4]]
        hands[h][0] = newVal

    total = 0
    for i in range(len(hands), 0, -1):
        maxNum = maxVal(hands)
        total += i * int(hands[maxNum][2])
        hands[maxNum][0] = 0
    
    print("Part 2:", total)

def permutations(hand):
    if hand.count("J") == 0: return [hand]
    
    perms = []
    if hand[0] != "J":
        temp = permutations(hand[1:])
        for h in temp:
            perms.append(hand[0] + h)
        return perms
    
    for char in "AKQT98765432":
        for h in permutations(hand[1:]):
            perms.append(char + h)
    return perms

def maxVal(hands):
    maxScore = 0
    maxIndex = 0
    for i in range(len(hands)):
        if hands[i][0] > maxScore:
            maxScore = hands[i][0]
            maxIndex = i
    return maxIndex

def getRank(hand):
    if hand.count(hand[0]) == 5:
        return 6
    if hand.count(hand[0]) == 4 or hand.count(hand[1]) == 4:
        return 5
    if hand.count(hand[0]) == 3 or hand.count(hand[1]) == 3 or hand.count(hand[2]) == 3:
        if hand.count(hand[0]) == 2 or hand.count(hand[1]) == 2 or hand.count(hand[2]) == 2 or hand.count(hand[3]) == 2:
            return 4
        return 3

    pairs = ""    
    for i in hand:
        if hand.count(i) == 2 and i not in pairs:
            pairs += i

    if len(pairs) == 2:
        return 2
    if len(pairs) == 1:
        return 1
    return 0


inputVals = []
f = open("Day_7_input.txt")
for line in f:
    inputVals.append(line.replace("\n", ""))

part1()
part2()