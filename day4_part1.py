import numpy as np

file = "day4_input.txt"
text = np.loadtxt(file, dtype=str)

# TODO: Solve this using a convolution kernel of 3x3 over the input as a boolean matrix with 1 layer of zeropadding

# Put characters into 2D np.array
char_lists = [[char for char in line] for line in text]
char_array = np.array(char_lists)
nrows = char_array.shape[0]
ncols = char_array.shape[1]
print("nrows", nrows, "ncols", ncols)
print("char_array = ", char_array)

# list of accessible roll indexes
i_accessible = []

for i, line in enumerate(char_array):
    for j, char in enumerate(line):
        surroundcount = 0

        if char_array[i, j] == "@":
            # print("index", (i, j), "with value", char_array[i, j], "is equal to @")
            if i != 0:  # topleft
                if char_array[i - 1, j - 1] == "@" and j != 0:
                    surroundcount += 1
                # topmiddle
                if char_array[i - 1, j] == "@":
                    surroundcount += 1
                # topright
                if j != (ncols - 1):
                    if char_array[i - 1, j + 1] == "@":
                        surroundcount += 1

            # midleft
            if char_array[i, j - 1] == "@" and j != 0:
                surroundcount += 1
            # midright
            if j != (ncols - 1):
                if char_array[i, j + 1] == "@":
                    surroundcount += 1

            if i != (nrows - 1):
                # bottomleft
                if char_array[i + 1, j - 1] == "@" and j != 0:
                    surroundcount += 1
                # bottommiddle
                if char_array[i + 1, j] == "@":
                    surroundcount += 1
                # bottomright
                if j != (ncols - 1):
                    if char_array[i + 1, j + 1] == "@":
                        surroundcount += 1

            if surroundcount < 4:
                i_accessible.append((i, j))

print(i_accessible)
print("amount of accessible rolls = ", len(i_accessible))
