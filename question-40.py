rows = 5
for i in range(1, rows + 1):
    for j in range(rows - i):
        print(" ", end="")
    for k in range(i):
        print(chr(65 + k), end="")
    for l in range(i - 2, -1, -1):
        print(chr(65 + l), end="")
    print()