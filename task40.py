def median(numbers):
    if not numbers:
        return None
    
    sorted_numbers = sorted(numbers) 
    n = len(sorted_numbers)
    
    if n % 2 == 1:  
        return sorted_numbers[n // 2]
    else: 
        mid1 = sorted_numbers[n // 2 - 1]
        mid2 = sorted_numbers[n // 2]
        return (mid1 + mid2) / 2


print(median([3, 1, 2])) 
print(median([1, 2, 3, 4]))  
print(median([5, 3, 8, 7, 2]))  
print(median([]))  