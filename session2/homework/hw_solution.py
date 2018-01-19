col = int(input("Enter columns: "))
row = int(input("Enter rows: "))
for y in range(row):
    for x in range(col):
        if (x + y) % 2 == 0:
            print("x", end=" ")
        else:
            print("*", end=" ")
    print()
