def cleaned_str(st):
    result = []
    
    for char in st:
        if char == '@':
            if result:
                result.pop()
        else:
            result.append(char)
    return ''.join(result)

text = "гр@oo@лк@оц@ва"
result = cleaned_str(text)
print(result)