def list_sum(nums):
    summa = 0
    for i in nums:
        summa = summa + i
        return summa

numerot = [1,3,5,7,9]
print("Summa", list_sum(numerot))