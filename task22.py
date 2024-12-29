my_dict = {
    'key1': 'value1',
    'key2': 'value2',
    'key3': 'value3',
    'key4': 'value4',
    'key5': 'value5'
}

keys = list(my_dict.keys())

first_key = keys[0]
last_key = keys[-1]

my_dict[last_key], my_dict[first_key] = my_dict[first_key], my_dict[last_key]

second_key = keys[1]
del my_dict[second_key]

my_dict['new_key'] = 'new_value'
print(my_dict)