n = 6
j = 1
li = ["A", "E", "I", "O", "U"]
count = 0
j2 = 2
for col in range(n):
    for space in range(n - col - 1):
        print(' ', end='')
    if col % 2 == 0:
        for row in range(1 * col + 1):
            print(j, end=" ")
            j = j + 2
    else:
        for row in range(1 * col + 1):
            print(j2, end=" ")
            j2 = j2 + 2
    print()
