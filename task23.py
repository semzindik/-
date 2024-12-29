def search_substr(subst, st):
    subst_lower = subst.lower()
    st_lower = st.lower()
    
    if subst_lower in st_lower:
        return "Есть контакт!"
    else:
        return "Мимо!"

result1 = search_substr("hello", "Hello, how are you?")
print(result1)

result2 = search_substr("world", "Goodbye, cruel world!")
print(result2)

result3 = search_substr("test", "This is a sample string.")
print(result3)