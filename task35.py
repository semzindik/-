def total_volume(boxes):
    total = 0
    for box in boxes:
        length, width, height = box
        volume = length * width * height
        total += volume
    return total

box_dimensions = [
    (2, 3, 4),  
    (1, 1, 1),
    (5, 2, 3)  
]

result = total_volume(box_dimensions)
print(result) 