import numpy as np

# Define known variables
file = "day1_input.txt"
testfile = "testinput.txt"
dial = 50

# Convert strings to array of signed turn numbers
turnarray = np.genfromtxt(file, dtype=str)
numarray = np.empty(len(turnarray), dtype=int)
sign = 1

for i, turn in enumerate(turnarray):
    if turn[0] == "R":
        sign = 1
    elif turn[0] == "L":
        sign = -1
    numarray[i] = int(turn[1:]) * sign

print("signed array of turns:", numarray)


# Perform the turns and count the zeros while looping 99+1->0
password = 0

for turn in numarray:
    dial += turn
    dial = dial % 100
    if dial == 0:
        password += 1

print("The first password is:", password)


# Compute the second password
dial = 50
zeropassings = 0
password = 0
testvar = 0
for turn in numarray:
    # password: 6423
    # dial: 94
    # turn: -474
    # password: 6428
    print("dial:", dial)
    print("turn:", turn)
    if dial == 0:
        zeropassings = abs(turn) // 100
        print("--------ZERO HERE---------")

    elif turn > 0:
        zeropassings = (dial + turn) // 100

    elif turn < 0:
        if abs(turn) > dial:
            if abs(turn) % 100 == 0:
                zeropassings = abs(turn) // 100
            if abs(turn) % 100 < dial:
                zeropassings = abs(turn) // 100
            if abs(turn) % 100 >= dial:
                zeropassings = 1 + (abs(turn) // 100)

        if abs(turn) < dial:
            zeropassings = 0

        if abs(turn) == dial:
            zeropassings = 1

    password += zeropassings
    print("password:", password)
    zeropassings = 0
    dial += turn
    dial = dial % 100

print("The second password is:", password)
