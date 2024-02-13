lines = 10
for i in range(1, lines):
    # calculate number of tabs to print based on the current line
    tabs = lines - i

    # print the tabs first
    for t in range(tabs):
        print("\t", end="")

    # print each line star and the ensuing tab after the star
    for j in range(i):
        print("*\t\t", end="")

    # print new line to begin next line on triangle
    print("\n")

# function definition for constructing triangles with varying heights