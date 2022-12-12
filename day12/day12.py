from collections import defaultdict, deque

#file = "./input_small.txt"
file = "input.txt"
finput = open(file, "r")
lines = finput.readlines()

rows = len(lines)
cols = len(list(lines[0].strip("\n")))
matrix = [[""]*cols for _ in range(rows)]

for r in range(rows):
    matrix[r] = list(lines[r].strip("\n"))

adjacent = defaultdict(set)

sources = []
S = None
E = None
dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
for r in range(rows):
    for c in range(cols):
        if matrix[r][c] == "S":
            S = (r, c)
            sources.append((r, c))
        elif matrix[r][c] == "a":
            sources.append((r, c))
        elif matrix[r][c] == "E":
            E = (r, c)

        for dy, dx in dirs:
            nr = r + dy
            nc = c + dx

            if nr >= 0 and nr < rows and nc >= 0 and nc < cols and matrix[nr][nc] != "S":
                # From starting we can only go to a
                source = matrix[r][c]
                dest = matrix[nr][nc]
                if source == "S":
                    source = "a"
                if dest == "E":
                    dest = "z"

                elevation = ord(dest) - ord(source)

                if elevation <= 1:
                    adjacent[(r, c)].add((nr, nc))


def dfs(source, destination):
    """
    Breadth first search will guarantee shortest path
    Time complexity: O(V+E)
    Space complexity: O(V+E)
    """
    q = deque([(source[0], source[1], 0)])
    visited = set()
    visited.add(source)
    while q:
        r, c, distance = q.popleft()
        if (r, c) == destination:
            return distance
        for nr, nc in adjacent[(r, c)]:
            if (nr, nc) not in visited:
                visited.add((nr, nc))
                q.append((nr, nc, distance+1))

    return float("inf")


# Part 1
print(dfs(S, E))

# Part 2
min_distance = float('inf')
for source in sources:
    min_distance = min(min_distance, dfs(source, E))

print(min_distance)
