def count_it(sequence):
    count_dict = {}
    
    for char in sequence:
        num = int(char) 
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
    
    sorted_count = sorted(count_dict.items(), key=lambda item: item[1], reverse=True)
    
    top_three = dict(sorted_count[:3])
    
    return top_three

sequence = "123321456789012345678901234567890"
result = count_it(sequence)
print(result)  