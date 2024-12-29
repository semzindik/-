def biggest_dict(**kwargs):

    my_dict = {'first_one': 'we can do it'}
    
    my_dict.update(kwargs)
    
    return my_dict

result = biggest_dict(key1='value1', key2='value2', key3='value3')
print(result)