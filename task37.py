def hacker_encode(text):
    hacker_dict = {
        'a': '4',
        'e': '3',
        'i': '1',
        'o': '0',
        's': '5',
        't': '7'
    }
    
    encoded_text = ''.join(hacker_dict.get(char, char) for char in text)
    return encoded_text

input_str = "This is an example string."
result = hacker_encode(input_str)
print(result)