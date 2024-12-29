def distance(a, b):
    return round(((b['x'] - a['x'])**2 + (b['y'] - a['y'])**2)**0.5, 3)
a = {'x': 1, 'y': 2}
b = {'x': 4, 'y': 6}
print(distance(a, b))