

def factors(n):
    nums = {}
    for x in range(2, round(n**0.5) + 1):
        division = n / x
        if division.is_integer():
            nums[int(division)] = x
    return(nums)

for x in range(2, int(input(""))):
    g = factors(x)
    if len(g) > 0:
        print(x, g)