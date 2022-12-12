#file = "./input_small.txt"
file = "input.txt"
finput = open(file, 'r')
lines = finput.readlines()

cmds = {"addx": 2, "noop": 1}

i = 0
n = len(lines)
X = 1
T = 0
C = 0
matrix = [["."]*40 for _ in range(6)]

while i < n:
    cmd = lines[i].strip("\n").split()
    cycles = cmds[cmd[0]]
    j = 0
    while j < cycles:
        row = C // 40
        col = C % 40
        if abs(col-X) <= 1:
            matrix[row][col] = "#"
        C += 1
        if (C-20)%40 == 0:
            T += X*C
        j += 1
    if cmd[0] == "addx":
        X += int(cmd[1])
    i += 1

# Part 1
print(T)

# Part 2
for r in range(len(matrix)):
    print("".join(matrix[r]))
