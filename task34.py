def multiply_numbers(numbers_str):
    numbers = map(float, numbers_str.split(', '))
    
    result = 1
    for number in numbers:
        result *= number
    
    return result

input_str = "2, 3, 4"
result = multiply_numbers(input_str)
print(result) 