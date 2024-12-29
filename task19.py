def to_dict(Ist):
   
    return {item: item for item in Ist}


my_list = ['apple', 'banana', 'kiwi']
result = to_dict(my_list)
print(result)  