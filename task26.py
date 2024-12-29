def camel(st):
    result = []
    upper = True

    for char in st:
        if char.isalpha():
            if upper:
                result.append(char.upper())
            else:
                result.append(char.lower())
            upper = not upper 
        else:
            result.append(char) 

    return ''.join(result)

text = "Привет, как дела? Надеюсь, все хорошо!"
result = camel(text)
print(result) 