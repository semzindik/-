def create_coordinates(x_coords, y_coords):

    if len(x_coords) != len(y_coords):
        raise ValueError ("Длины массивов должны быть равны.")
    
    coordinates = [(x, y) for x, y in zip(x_coords, y_coords)]
    
    return coordinates

x_array = [1, 2, 3, 4]
y_array = [5, 6, 7, 8]
result = create_coordinates(x_array, y_array)
print(result)