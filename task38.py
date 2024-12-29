def cumulative_sum(numbers):
    result = []
    total = 0
    
    for number in numbers:
        total += number
        result.append(total)  
    
    return result

input_list = [1, 2, 3, 4]
result = cumulative_sum(input_list)
print(result)