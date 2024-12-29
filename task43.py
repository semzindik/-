def remove_enemies(names, enemies):
    return [name for name in names if name not in enemies]

names_list = ["Alice", "Bob", "Charlie", "David"]
enemies_list = ["Bob", "David"]

result = remove_enemies(names_list, enemies_list)
print(result)  