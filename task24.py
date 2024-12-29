def first_last(letter, st):
    first_index = st.find(letter)
    
    if first_index == -1:
        return (None, None)
    
    last_index = st.rfind(letter)
    
    return (first_index, last_index)

result1 = first_last('a', 'banana')
print(result1)

result2 = first_last('z', 'banana')
print(result2)

result3 = first_last('n', 'banana')
print(result3)