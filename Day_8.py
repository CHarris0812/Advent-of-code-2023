def part1():
    moves = 0
    cur = "AAA"
    while cur != "ZZZ":
        direction = instructions[moves % len(instructions)]
        if direction == "L": cur = neighbors[cur][0]
        else: cur = neighbors[cur][1]
        moves += 1
    print("Part 1:", moves)

def part2():
    moves = 0
    cur = []
    for i in neighbors:
        if i[2] == "A":
            cur.append(i)

    print(cur)

    results = [0 for i in cur]
    results2 = [0 for i in cur]

    while 0 in results2:
        for i in range(len(cur)):
            if cur[i][2] == "Z" and results[i] == 0:
                results[i] = moves
            elif cur[i][2] == "Z" and results2[i] == 0:
                results2[i] = moves
        direction = instructions[moves % len(instructions)]
        if direction == "L": 
            for i in range(len(cur)):
                cur[i] = neighbors[cur[i]][0]
        else: 
            for i in range(len(cur)):
                cur[i] = neighbors[cur[i]][1]
        moves += 1

    print("Part 2:", findLCM(results))

def findLCM(nums):
    primeFactors = [primeFactorize(num) for num in nums]
    result = 1
    for p in primes:
        if p != "":
            maxNum = 0
            for pf in primeFactors:
                if int(p) in pf:
                    maxNum = max(maxNum, pf[int(p)])
            result *= int(p) ** maxNum
    return result

def lcm(nums):
    lcm = 1
    for i in nums:
        lcm *= i
    return simplify(lcm, nums)

def simplify(num, nums):
    for i in primes:
        if i != "":
            i = int(i)
            if num % i == 0: 
                valid = True
                newNum = num // i
                for n in nums:
                    temp = newNum % n
                    if temp != 0:
                        valid = False
                
                if valid:
                    return simplify(num // 2, nums)
    return num

def primeFactorize(num):
    primeFactors = {}
    while num != 1:
        for p in primes:
            if p != "":
                p  = int(p)
                if num % p == 0:
                    if p in primeFactors:
                        primeFactors[p] += 1
                    else:
                        primeFactors[p] = 1
                    num = num // p
    return primeFactors


def finished(nodes):
    for n in nodes:
        if n[2] != "Z": return False
    return True

inputVals = []
f = open("Day_8_input.txt")
instructions = "LLLRLRLRLLRRRLRRRLRRRLLLRLRLLRRLLRRLRLRLLRLRLRRLLRRRLRLLRRLRRRLRRLLLRRRLRRRLRRRLLLLRRLRRRLRLRRRLRRLLRLRLRRRLRRRLRRLRRRLLLLLLRLRRRLLLLRLRRRLRRRLRLRRLRLRLRLRLRRRLLRRLRLRRLRRLRRLLRLLLRRLRLLRRLRLRRLRRRLRRLLRLRLRLRRLLRLLRRLLLRLRLRRRLRRLLRRRLRLRLRRLLRLRLRLRRLRLRLRRLRRLLRRLRRRLRRRLLLRRRR"
#instructions = "LR"
neighbors = {}
for line in f:
    line = line.replace("\n", "")
    node = line.split(" = ")[0]
    edges = line.split(" = ")[1][1:-1]
    edges = edges.split(", ")
    neighbors[node] = edges

f = open("primes.txt")
primes = []
for line in f:
    p = line.replace("\n", "")
    primes += (p.split(" "))

#print(primeFactorize(100))

#part2()
num = 0
while num < 1338527266:
    num += 2
print("done")