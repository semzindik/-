def has_adjacent_duplicates(word):
    for i in range(len(word) - 1):
        if word[i] == word[i + 1]: 
            return True
    return False  

print(has_adjacent_duplicates("hello"))  
print(has_adjacent_duplicates("world")) 
print(has_adjacent_duplicates("bookkeeper")) 
print(has_adjacent_duplicates("python"))  