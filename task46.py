def replace_end_punctuation(text):
   
    while text and (text[-1] == '?' or text[-1] == '!'):
        text = text[:-1]  
    if text and text[-1] != ' ':
        return text + '?' 
    return text


print(replace_end_punctuation("Привет!!!"))  
print(replace_end_punctuation("Как дела???"))  
print(replace_end_punctuation("Все хорошо!"))  
print(replace_end_punctuation("Что нового???!!!"))  
print(replace_end_punctuation("Просто текст."))  