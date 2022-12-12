#file = "./input_small.txt"
file = "input.txt"
finput = open(file, 'r')
lines = finput.readlines()

dirs = {'U': (-1, 0), 'D': (1, 0), 'R': (0, 1), 'L': (0, -1)}


def getNextStep(hy, hx, ty, tx):
    if hy == ty:
        tx += 1 if (hx-tx) > 0 else -1
    elif hx == tx:
        ty += 1 if (hy-ty) > 0 else -1
    else:
        tx += 1 if (hx-tx) > 0 else -1
        ty += 1 if (hy-ty) > 0 else -1

    return (ty, tx)


def calculateMotion(knots=2):
    n = len(lines)
    s_x, s_y = 0, 0
    visited = set()
    visited.add((s_y, s_x))
    pos = [0]*(knots)
    h_y, h_x = [pos.copy() for _ in range(2)]
    i = 0
    while i < n:
        line = lines[i].strip('\n')
        dir, step = line.split()
        step = int(step)
        dy, dx = dirs[dir]
        j = 0
        while j < step:
            k = 0
            while k < knots:
                if k > 0 and abs(h_y[k-1] - h_y[k]) <= 1 and abs(h_x[k-1] - h_x[k]) <= 1:
                    break

                if k == 0:
                    h_y[k] += dy
                    h_x[k] += dx
                elif abs(h_y[k-1] - h_y[k]) > 1 or abs(h_x[k-1] - h_x[k]) > 1:
                    h_y[k], h_x[k] = getNextStep(h_y[k-1], h_x[k-1], h_y[k], h_x[k])

                if k == knots-1:
                    visited.add((h_y[k], h_x[k]))
                k += 1
            j += 1
        i += 1
    return len(visited)


# Part 1
moved = calculateMotion(knots=2)
print(moved)

# Part 2
moved = calculateMotion(knots=10)
print(moved)
