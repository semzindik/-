def all_eq(Ist):
    max_length = max(len(s) for s in Ist)
    return [s.ljust(max_length, '_') for s in Ist]

result = all_eq(['apple', 'banana', 'kiwi', 'grape'])
print(result)