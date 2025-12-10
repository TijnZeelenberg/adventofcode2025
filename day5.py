file = "day5_input.txt"

with open(file) as f:
    lines = f.read()
rangeIDSplit = lines.split("\n\n")

freshRanges = [
    [int(rangestr.split("-")[0]), int(rangestr.split("-")[1])]
    for rangestr in rangeIDSplit[0].split("\n")
]
produceIDs = [int(ID) for ID in rangeIDSplit[1].split("\n")[:-1]]

print("freshRanges = ", freshRanges)
print("\n\n\n ProduceIDs = ", produceIDs)

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

print(freshIDs)
print("Part one answer = ", len(freshIDs))
