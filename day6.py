import numpy as np
import math

file = "day6_input.txt"

with open(file) as f:
    lines = f.read()
    lines = [line.split() for line in lines.split("\n")[:-1]]
    operators = lines[-1]  # Take all lines except the operators
    numbers = lines[:-1]  # Take the operators
    # Convert the numbers to ints
    numbers = [[int(string) for string in stringlist] for stringlist in numbers]

numbers = np.array(numbers)
results = []
for col in range(len(numbers[0])):
    if operators[col] == "+":
        results.append(numbers[:, col].sum())
    if operators[col] == "*":
        results.append(np.prod(numbers[:, col]))

print("Answer part one = ", sum(results))

with open(file) as f:
    lines = f.readlines()

operatorlist = lines[-1].split()
charlist = [[char for char in line.rstrip("\n")] for line in lines[:-1]]

# readlines() strips the spaces from the last row so we re-append those
diff = len(charlist[-2]) - len(charlist[-1])
if diff > 0:
    for i in range(diff):
        charlist[-1].append(" ")

rl_shift = np.flip(np.transpose(charlist), axis=0)
operatorlist = list(reversed(operatorlist))
print(rl_shift)
print(operatorlist)
equations = []
nums = []
for row in rl_shift:
    if all(char == " " for char in row):
        equations.append(nums)
        nums = []
    else:
        nums.append(int("".join(row)))
equations.append(nums)  # Append the last equation
print(equations)

results = []
for i, operator in enumerate(operatorlist):
    if operator == "+":
        results.append(sum(equations[i]))
    elif operator == "*":
        results.append(math.prod(equations[i]))
print(sum(results))
