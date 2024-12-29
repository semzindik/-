def is_increasing(numbers):
    for i in range(len(numbers) - 1):
        if numbers[i] >= numbers[i + 1]:
            return False
    return True


print(is_increasing([1, 2, 3, 4, 5])) 
print(is_increasing([1, 2, 2, 4, 5])) 
print(is_increasing([5, 4, 3, 2, 1])) 
print(is_increasing([1, 3, 5, 7, 9])) 