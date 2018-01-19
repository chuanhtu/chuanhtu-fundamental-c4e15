from random import randint
from getpass import getpass
print("Guess your numbergame")
n = int(getpass('Now think of a number from 0 to 100, then press Enter', ))
print("All you have to do is to answer to my guess")
print("'c' if my guess is 'C'orrect")
print("'s' if my guess is 'S'maller tan your number")
print("'l' if my guess is 'L'arger than your number'")

maxn = 100
minn = 0
x = randint(0, 100)
while x != n:
    answer=print("Is", x, "your number?",end="")
    if x > n:
        input()
        maxn = x
        x = (maxn + minn) // 2
        print('Larger than your number')

    elif x < n:
        input()
        minn = x
        x = (maxn + minn) // 2
        print('smaller tan your number')
else:
    answer=print("Is", x, "your number?",end='')
    print('c')

print('I knew it')
