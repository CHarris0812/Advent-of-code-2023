def part1():
    total = 0
    for i in inputVals:
        hashed = 0
        for c in i:
            hashed += ord(c)
            hashed *= 17
            hashed %= 256
        total += hashed
    print("Part 1:", total)

def part2():    
    boxes = [[] for i in range(256)]
    for i in inputVals:
        if "=" in i:
            box = hash(i.split("=")[0])
            replaced = False
            for j in range(len(boxes[box])):
                if i.split("=")[0] in boxes[box][j]:
                    boxes[box][j] = i
                    replaced = True

            if not replaced:
                boxes[box].append(i)
        else:
            box = hash(i[:-1])
            for j in range(len(boxes[box])):
                if boxes[box][j].split("=")[0] == i[:-1]:
                    boxes[box].pop(j)
                    break
    
    total = 0
    for box in range(len(boxes)):
        for i in range(len(boxes[box])):
            total += (box + 1) * (i + 1) * int(boxes[box][i].split("=")[1])
    print("Part 2:", total)

def hash(i):
    hashed = 0
    for c in i:
        hashed += ord(c)
        hashed *= 17
        hashed %= 256
    return hashed


inputVals = []
f = open("Day_15_input.txt")
for line in f:
    line = line.replace("\n", "")
    inputVals.append(line.split(","))
inputVals = inputVals[0]

part1()
part2()