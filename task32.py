def remove_extra_spaces(st):
    return ' '.join(st.split())

text = "  Это   пример   строки с   лишними пробелами.   "
result = remove_extra_spaces(text)
print(f"'{result}'") 