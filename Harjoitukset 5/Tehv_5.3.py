num = int(input("Syötä kokonaisluku:"))

if num <= 1:
    print("Ei Alkuluku")
else:
    for x in range(2, num):
        if num % x == 0:
            print("Ei Alkuluku")
            break

    else:
        print("Alkuluku")