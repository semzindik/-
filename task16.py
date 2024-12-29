def useless(s):
    if len(s) == 0:
        raise ValueError("Список не должен быть пустым.")
    
    max_value = max(s)

    length = len(s)

    useless_value = max_value / length
    
    return useless_value

numbers = [10, 20, 30, 40, 50]
result = useless(numbers)
print(result)