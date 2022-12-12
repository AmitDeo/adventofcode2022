#file = "./input_small.txt"
file = "input.txt"
finput=open(file, 'r')
lines = finput.readlines()

# Start Position
s_x, s_y = 0, 0
# # Farthest it can go right and left along x axis
# x_min, x_max = float('inf'), float('-inf')
# # Farthest it can go up and down along y axis
# y_min, y_max = float('inf'), float('-inf')
# x, y = 0, 0

# n = len(lines)
# i = 0
# # First pass get the matrix size and start
# # position
# while i < n:
#     line = lines[i].strip('\n')
#     dir, step = line.split()
#     step = int(step)
#     if dir == "U":
#         x -= step
#     elif dir == 'D':
#         x += step
#     elif dir == 'L':
#         y += step
#     elif dir == 'R':
#         y -= step

#     x_max = max(x, x_max)
#     x_min = min(x, x_min)
#     y_max = max(y, y_max)
#     y_min = min(y, y_min)
#     i += 1

# cols = x_max + abs(x_min) + 1
# rows = y_max + abs(y_min) + 1
# s_x = abs(x_min)
# s_y = abs(y_min)
# #print(rows, 'x', cols)
# #print(x_max, x_min, y_max, y_min)
# #print(s_x, s_y)

# matrix = [[0]*cols for _ in range(rows)]

visited = set()
visited.add((s_y, s_x))

i = 0

# Second pass get the visited nodes of tail
i = 0
n = len(lines)
dirs = {'U': (-1, 0), 'D': (1, 0), 'R': (0, 1), 'L': (0, -1)}
h_x, h_y , t_x, t_y = 0, 0, 0, 0
p_y, p_x = 0, 0
change_in_row = False
while i < n:
    line = lines[i].strip('\n')
    dir, step = line.split()
    step = int(step)
    dy , dx = dirs[dir]

    j = 0
    #print(dir, step)
    #print(h_y, h_x)
    #print('---')


    if t_y != h_y and t_x != h_x:
        change_in_row = True

    while j < step:
        h_y += dy
        h_x += dx
        if abs(t_y - h_y) > 1 or abs(t_x - h_x) > 1:
            t_y , t_x = p_y, p_x
            visited.add((t_y, t_x))
        p_y, p_x = h_y, h_x
        j += 1
    
    i += 1
    #print(t_y, t_x)
    #print(h_y, h_x)
    #print("====")

print(len(visited))
