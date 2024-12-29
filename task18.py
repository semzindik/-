def alLeq(Ist):

    max_length = max(len(s) for s in Ist)
    

    result = [s.ljust(max_length, '_') for s in Ist]
    
    return result

strings = ["apple", "banana", "kiwi", "grape"]
result = alLeq(strings)
print(result)