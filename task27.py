def shortener(st):
    stack = []
    result = []
    
    for char in st:
        if char == '(':
            stack.append(len(result)) 
        elif char == ')':
            if stack:
                start_index = stack.pop()  
                result = result[:start_index] 
        else:
            if not stack:  
                result.append(char)
    
    return ''.join(result)

text = "Это пример (текста с (вложенными) скобками) для теста."
result = shortener(text)
print(result)