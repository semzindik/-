def change(Ist):

    if len(Ist) < 2:
        raise ValueError("Список должен содержать минимум 2 элемента.")
    

    Ist[0], Ist[-1] = Ist[-1], Ist[0]
    
    return Ist

my_list = [1, 2, 3, 4]
changed_list = change(my_list)
print(changed_list)