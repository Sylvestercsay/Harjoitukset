def poista_parilliset_luvut(nums):
    even_list = []
    for n in nums:
        if n % 2 == 0:
            even_list.append(n)
    return even_list

nums = [10,15,20,25,30]
Trimmed = poista_parilliset_luvut(nums)
print("Alkuperäinen luettelo", nums)
print("Lyhennetty luettelo ", Trimmed)