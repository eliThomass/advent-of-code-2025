# PART 1

input_array = []

with open('input1.txt', 'r') as r:
    for line in r:
        input_array.append(line.strip())
    
dial = 50
res = 0


for rotation in input_array:
    if rotation[0] == 'L':
        dial -= int(rotation[1:])
    else:
        dial += int(rotation[1:])
    
    if dial > 99:
        dial = dial % 100
    elif dial < 0:
        dial = dial % 100
    
    if dial == 0:
        res += 1
    
print(res)

# PART 2

dial = 50
res = 0
for rotation in input_array:
    dir = rotation[0]
    amt = int(rotation[1:])
    for _ in range(amt):
        if dir == 'L':
            dial = (dial - 1) % 100
        else:
            dial = (dial + 1) % 100
        if dial == 0:
            res += 1

print(res)

