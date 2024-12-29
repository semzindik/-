def is_surrounded_by_plus(s):
    if len(s) < 3:
        return False
    
    for i in range(1, len(s) - 1):
        if s[i].isalpha(): 
        
            if s[i - 1] != '+' or s[i + 1] != '+':
                return False
    return True


print(is_surrounded_by_plus("+a+b+c+"))  
print(is_surrounded_by_plus("+a+b+c"))  
print(is_surrounded_by_plus("++a++"))    
print(is_surrounded_by_plus("a+b+c+"))   
print(is_surrounded_by_plus("+a+b+c+"))  
print(is_surrounded_by_plus("+"))        