file = "input_day8.txt"
finput=open(file, 'r')
lines = finput.readlines()

n = len(lines)
i = 0
first = list(lines[0].strip("\n"))
m = len(first)

matrix = [[0] * m for _ in range(n)]

while i < n:
    row = list(lines[i].strip("\n"))
    j = 0
    while j < m:
        matrix[i][j] = row[j]
        j+=1
    i+=1

dp = [[[0]*4 for _ in range(m)] for _ in range(n)]
top = 0
left = 1
down = 2
right = 3

# From left to right
for i in range(n):
    for j in range(m):
        if j == 0:
            dp[i][j][3] = matrix[i][j]
        else:
            dp[i][j][3] = max(dp[i][j-1][3], matrix[i][j])

# From right to left
for i in range(n):
    for j in range(m-1, -1, -1):
        if j == m-1:
            dp[i][j][1] = matrix[i][j]
        else:
            dp[i][j][1] = max(dp[i][j+1][1], matrix[i][j])

# From top to bottom
for j in range(m):
    for i in range(n):
        if i == 0:
            dp[i][j][0] = matrix[i][j]
        else:
            dp[i][j][0] = max(dp[i-1][j][0], matrix[i][j])

# From bottom to top
for j in range(m):
    for i in range(n-1, -1, -1):
        if i == n-1:
            dp[i][j][2] = matrix[i][j]
        else:
            dp[i][j][2] = max(dp[i+1][j][2], matrix[i][j])


total = 2*m + 2*n - 4

for i in range(1, n-1):
    for j in range(1, m-1):
        # test the way out
        if dp[i-1][j][top] < matrix[i][j] \
            or dp[i][j+1][left] < matrix[i][j] \
            or dp[i+1][j][down] < matrix[i][j] \
            or dp[i][j-1][right] < matrix[i][j]:
            total += 1

print(total)

scenic_beauty = float('-inf')

for i in range(1, n-1):
    for j in range(1, m-1):
        t = 0
        d = 0
        l = 0
        r = 0

        up = i - 1
        while up >= 0:
            t += 1
            if matrix[up][j] >= matrix[i][j]:
                break
            up -= 1

        bottom = i + 1
        while bottom < n:
            d += 1
            if matrix[bottom][j] >= matrix[i][j]:
                break
            bottom += 1

        left = j - 1
        while left >= 0:
            l += 1
            if matrix[i][left] >= matrix[i][j]:
                break
            left -= 1

        right = j + 1
        while right < m:
            r += 1
            if matrix[i][right] >= matrix[i][j]:
                break
            right += 1

        scenic_beauty = max(scenic_beauty, t*d*l*r)

print(scenic_beauty)
