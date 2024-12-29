def radius_of_sphere(volume):
    from math import pi, pow
    return pow((3 * volume) / (4 * pi), 1/3)

result = radius_of_sphere(100)
print(result)