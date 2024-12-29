def useless(s):
    return max(s) / len(s)

print(useless([1, 2, 3, 4, 5]))
print(useless([10, 20, 30]))
print(useless([-1, -2, -3, -4]))
print(useless([0, 0, 0, 0]))