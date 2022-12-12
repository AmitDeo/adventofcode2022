from collections import deque
import math

#file = "./input_small.txt"
file = "input.txt"
finput = open(file, "r")
lines = finput.readlines()

monkeys = 0
starting_items = []
operators = []
operands = []
test = []
throws_true = []
throws_false = []

i = 0
n = len(lines)
start = True
while i < n:
    line = lines[i].strip("/n").strip()
    if line != "":
        if line.startswith("Monkey"):
            monkeys += 1
        elif line.startswith("Starting items:"):
            line = line[len("Starting items: "):]
            items = line.split(",")
            starting_items.append(items)
        elif line.startswith("Operation: "):
            line = line[len("Operation: new = old "):].split()
            operators.append(line[0])
            operands.append(line[1])
        elif line.startswith("Test: "):
            line = line[len("Test: divisible by "):]
            test.append(int(line))
        elif line.startswith("If true: "):
            line = line[len("If true: throw to monkey "):]
            throws_true.append(int(line))
        elif line.startswith("If false: "):
            line = line[len("If false: throw to monkey "):]
            throws_false.append(int(line))
    i += 1

inspected = [0]*monkeys

#part 1
relief_level = 3
rounds = 20

#part 2 (Comment this for part 1)
relief_level = 1
rounds = 10000

# To keep the number to test lower for faster execution
mod = math.prod(test)

j = 0
while j < rounds:
    m = 0
    while m < monkeys:
        q = deque(starting_items[m])
        while q:
            item = int(q.popleft())
            inspected[m] += 1
            operand = item if operands[m] == "old" else int(operands[m])
            if operators[m] == "*":
                item = item * operand
            elif operators[m] == "+":
                item = item + operand
            item = (item // relief_level) % mod
            if item % test[m]:
                starting_items[throws_false[m]].append(item)
            else:
                starting_items[throws_true[m]].append(item)
        starting_items[m] = []
        m += 1
    j += 1

inspected.sort()
print(inspected[-2]*inspected[-1])