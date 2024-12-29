import re

def sum_of_numbers(s):
    
    numbers = re.findall(r'\d+', s)
    total_sum = sum(int(num) for num in numbers)
    return total_sum


input_str1 = "abc123def456"
input_str2 = "1a2b3c"
input_str3 = "no numbers here"
input_str4 = "12abc34def56"

print(sum_of_numbers(input_str1))  
print(sum_of_numbers(input_str2)) 
print(sum_of_numbers(input_str3)) 
print(sum_of_numbers(input_str4))  