def list_sort(Ist):
    return sorted(Ist, key=abs, reverse=True)

result = list_sort([-3, 1, -2, 4, -5])
print(result)