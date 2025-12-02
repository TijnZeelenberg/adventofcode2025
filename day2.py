import numpy as np
import math

file = "day2_input.txt"
ID_array = np.genfromtxt(file, dtype=str, delimiter=",")

#### PART ONE ####
answer1 = 0

for IDrange in ID_array:
    IDrange = IDrange.split("-")
    RangeStart = int(IDrange[0])
    RangeEnd = int(IDrange[1])

    # If the range  only contains uneven length then it cannot consist of 2 identical string
    if (len(str(RangeStart)) == len(str(RangeEnd))) and (len(str(RangeStart)) % 2 == 1):
        # print(f"Skipping range {RangeStart}-{RangeEnd}")
        continue

    for ID in range(RangeStart, RangeEnd + 1):
        ID_str = str(ID)
        if ID_str == (2 * ID_str[0 : int(0.5 * len(ID_str))]):
            # print("Wrong ID: ", ID_str)
            answer1 += ID

print("Answer 1 is: ", answer1)


#### PART TWO ####
answer2 = 0


def divisors(x):
    return [i for i in range(1, x) if ((x % i) == 0)]


# ID_array = np.array(["2-222"])
for IDrange in ID_array:
    IDrange = IDrange.split("-")
    RangeStart = int(IDrange[0])
    RangeEnd = int(IDrange[1])

    for ID in range(RangeStart, RangeEnd + 1):
        invalid = False
        ID_str = str(ID)

        # Problem: a string like 333333 can be interpreted as 2 * '333', 2 * '33', and 6 *'3'
        # This results in this one wrong ID being counted 3 times for the answer
        # Solution: make sure each ID is only counted once in the answer

        if len(ID_str) == 1:  # Single digit ID's cannot have repeating patterns
            print("Skipping single digit ID ", ID)
            continue

        for patternlength in divisors(len(ID_str)):
            patternrepeats = int(len(ID_str) / patternlength)
            if ID_str == (patternrepeats * ID_str[0:patternlength]):
                invalid = True
        if invalid:
            print("Wrong ID: ", ID)
            answer2 += ID

print("Answer 2 is: ", answer2)
