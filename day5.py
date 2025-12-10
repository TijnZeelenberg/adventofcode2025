file = "testinput.txt"

with open(file) as f:
  lines = f.read()

freshRanges = [range.split("-") for range in lines.split("\n\n")[0].split("\n")]
print(freshRanges)
