lines = 10
for i in range(1, lines):
    # prinnt the tabs first
    tabs = lines - i
    for t in range(tabs):
        print("\t", end="")
    for j in range(i):
        print("*\t\t", end="")
    print("\n")

# function definition for constructing triangles with varying heights