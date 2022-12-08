from collections import deque
import heapq

class TreeNode:
    def __init__(self, name):
        self.name = name
        self.parent = None
        self.children = {}
        self.files = []
        self.size = 0

    def __str__(self):
        files = ' '.join([file for file, _ in self.files])
        return f'Directory name is {self.name} and size is {self.size} and files are {files}'

def directoryCrawler(file):
    finput=open(file, 'r')
    root = TreeNode('/')
    current = root

    lines = finput.readlines()
    n = len(lines)
    i = 0
    while i < n:
        line = lines[i]
        command = line.strip('\n').split()
        if command[0] == '$':
            # Command
            if command[1] == 'cd':
                if command[2] == '/':
                    current = root
                elif command[2] == '..':
                    current = current.parent
                else:
                    current = current.children.get(command[2], None)
                i += 1
            elif command[1] == 'ls':
                i += 1
                while i < n:
                    line = lines[i]
                    line = line.strip('\n')
                    if line.strip() != "" and not line.startswith('$'):
                        contents = line.split()
                        if contents[0] == 'dir':
                            node = TreeNode(str(contents[1]))
                            node.parent = current
                            current.children[contents[1]] = node
                        else:
                            current.files.append((str(contents[1]), int(contents[0])))
                        i += 1
                    elif line.startswith('$'):
                        break

    return root

def fileSize(node):
    global ans
    if node is None:
        return 0

    currentSize = 0
    for _, size in node.files:
        currentSize += size

    for child in node.children.values():
        currentSize += fileSize(child)

    node.size = currentSize

    if currentSize <= limit:
        ans += currentSize

    return node.size


def printRoot(root):
    q = deque([root])
    while q:
        node = q.popleft()
        print("-------")
        print(node)
        print("-------")
        for child in node.children.values():
            q.append(child)

def eligiblefilelist(root):
    q = deque([root])
    elegible_list = []
    while q:
        node = q.popleft()
        if node.size > extra_space_needed:
            heapq.heappush(elegible_list, node.size)
        for child in node.children.values():
            q.append(child)
    return heapq.heappop(elegible_list)

if __name__ == "__main__":
    ans = 0
    limit = 100000
    root = directoryCrawler("input_day7.txt")
    fileSize(root)
    #Part 2
    print(root.size)
    capacity = 70000000
    total_free_size = capacity - root.size
    space_needed = 30000000
    extra_space_needed = space_needed - total_free_size
    print(extra_space_needed)
    print("Eligible File to be deleted "+str(eligiblefilelist(root)))