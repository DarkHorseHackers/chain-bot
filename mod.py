def get_multiplicative_group(n):
    ans = set({1})

    for i in range(1, 30):
        broke = False
        for j in range(2, i+1):
            if 30 % j == 0 and i % j == 0:
                broke = True
        if not broke:
            ans.add(i)

    return ans

print(get_multiplicative_group(30))