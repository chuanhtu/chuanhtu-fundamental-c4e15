from getpass import getpass
print("Hi there, this is a superuser gateway")
wrong = 0
while wrong < 3:
    user = "c4e"
    pas = "123456"

    n = input("Username: ")
    m = getpass("Password: ")

    if n == user:
        if m == pas:
            print("Welcome, Mr.bunnycapcap")
            break

        else:
            print("Password is incorrect")
    else:
        print("You are not superuser")
    wrong += 1
else:
    print("You filed to log in 3 times, go away")
