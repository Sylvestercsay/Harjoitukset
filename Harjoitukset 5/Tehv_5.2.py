nums =[]


while True:
    arvo = int(input("Syötä numero u(Syötä stop): "))

    if arvo == "":
        break
    nums.append(int(arvo))

nums.sort(reverse=True)

print("Viisi suurinta lukua")
for i in range(5):
    print(nums[i])