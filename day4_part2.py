import numpy as np
import numpy.ma as ma

file = "day4_input.txt"
text = np.loadtxt(file, dtype=str)

# Put characters into 2D np.array
char_lists = [[char for char in line] for line in text]
char_array = np.array(char_lists)
nrows = char_array.shape[0]
ncols = char_array.shape[1]


# list of accessible roll indexes
def find_accessible(char_array):
    i_accessible = []

    for i, line in enumerate(char_array):
        for j, char in enumerate(line):
            surroundcount = 0

            if char == "@":
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

    return i_accessible


remove_count = 0
while len(find_accessible(char_array)) > 0:
    i_accessible = find_accessible(char_array)
    mask = np.zeros((nrows, ncols), dtype=bool)

    for index in i_accessible:
        mask[index] = True
    remove_count += np.count_nonzero(mask)
    print("Amount of removed rolls = ", remove_count)
    char_array[mask] = "."
