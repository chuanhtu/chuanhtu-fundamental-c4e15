number = int(input("nhap mot so"))
digits = 0
while number > 0:
    number = number // 10
    digits = digits + 1
print  ("so so hang la",digits)
