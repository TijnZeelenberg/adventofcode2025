import numpy as np

file = "day3_input.txt"
input = np.loadtxt(file, dtype=str)
jolts = np.zeros(len(input), dtype=int)

# for i, line in enumerate(input_arr):
#     firstint = line[0]
#     firstindex = 0
#     secondint = line[-1]
#     for index, char in enumerate(line[0:-1]):
#         if int(char) > int(firstint):
#             firstint = char
#             firstindex = index
#     for char in line[firstindex + 1 :]:
#         if int(char) > int(secondint):
#             secondint = char
#     jolts[i] = int(firstint + secondint)
#
# print(jolts)
# print(np.sum(jolts))
for i, line in enumerate(input):
    maxindex = 0
    joltstring = ""
    line_arr = np.array(list(line))

    for k in range(0, 12):
        if k == 0:
            maxindex = np.argmax(line_arr[:-11])
        elif k == 11:
            maxindex = maxindex + np.argmax(line_arr[maxindex + 1 :]) + 1
        else:
            maxindex = maxindex + np.argmax(line_arr[maxindex + 1 : -11 + k]) + 1

        maxval = line[maxindex]
        joltstring += maxval

    jolts[i] = int(joltstring)

print(np.sum(jolts))
