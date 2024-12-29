def list_sort(Ist):
    sorted_list = sorted(Ist, key=abs, reverse=True)
    return sorted_list

numbers = [-10, 2, -3, 5, 8, -15]
sorted_numbers = list_sort(numbers)
print(sorted_numbers)