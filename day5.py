file = "day5_input.txt"

with open(file) as f:
    lines = f.read()
rangeIDSplit = lines.split("\n\n")

freshRanges = [
    [int(rangestr.split("-")[0]), int(rangestr.split("-")[1])]
    for rangestr in rangeIDSplit[0].split("\n")
]
produceIDs = [int(ID) for ID in rangeIDSplit[1].split("\n")[:-1]]

### PART ONE ###
fresh = False
freshIDs = []
for ID in produceIDs:
    for rangelist in freshRanges:
        if (ID >= rangelist[0]) and (ID <= rangelist[1]):
            fresh = True
            break
    if fresh == True:
        freshIDs.append(ID)
    fresh = False

print("Part one answer = ", len(freshIDs))

### PART TWO ###
print("\n\n ### PART TWO ###")


def cleanranges(ranges):
    # print("freshRanges = ", ranges)
    cleanedRanges = [ranges[0]]
    for rangeList in ranges:
        if rangeList[0] > rangeList[1]:
            print(f"Range {rangeList} is interesting...")
        uniqueRange = True
        # print("Considering the range ", rangeList)
        for i, cleanedRangeList in enumerate(cleanedRanges):
            if (cleanedRangeList[0] <= rangeList[0] <= cleanedRangeList[1]) and (
                rangeList[1] > cleanedRangeList[1]
            ):
                # print(f"{rangeList} overlaps with {cleanedRangeList}")
                cleanedRanges[i][1] = rangeList[1]
                uniqueRange = False
                break
            elif (cleanedRangeList[0] <= rangeList[1] <= cleanedRangeList[1]) and (
                rangeList[0] < cleanedRangeList[0]
            ):
                # print(f"{rangeList} overlaps with {cleanedRangeList}")
                cleanedRanges[i][0] = rangeList[0]
                uniqueRange = False
                break
            elif (rangeList[0] >= cleanedRangeList[0]) and (
                rangeList[1] <= cleanedRangeList[1]
            ):
                # print(f"{rangeList} is a subset of {cleanedRangeList}")
                uniqueRange = False
                break
            elif (rangeList[0] < cleanedRangeList[0]) and (
                rangeList[1] > cleanedRangeList[1]
            ):
                # print(f"{rangeList} is a superset of {cleanedRangeList}")
                uniqueRange = False
                cleanedRanges[i] = rangeList
                break
            else:
                # print(f"Range {rangeList} not overlapping with {cleanedRangeList}")
                uniqueRange = True

        # If no overlap is found add the new rane to the cleanedRangeList
        if uniqueRange == True:
            cleanedRanges.append(rangeList)
        #     print("no overlap found, appending to cleanedRanges")
        # print("Current cleanedRanges = ", cleanedRanges)
    return cleanedRanges


for i in range(3):
    print(len(freshRanges))
    freshRanges = cleanranges(freshRanges)

countID = 0
for rangeList in sorted(freshRanges):
    print(rangeList)
    countID += (rangeList[1] - rangeList[0]) + 1
print("Answer to part TWO = ", countID)
