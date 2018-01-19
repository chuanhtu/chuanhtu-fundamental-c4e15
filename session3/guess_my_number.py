from random import randint

x = randint(1, 100)

loop = True

while loop:

    num = int(input("nhap mot so"))
    if num == x :
        print("bingo")
        loop = False
    elif num < x:
        print("nho hon mot ty")
    elif num > x:
        print ("lon hon mot ty")

    print()
