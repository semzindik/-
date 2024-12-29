import math

def water_mass(radius, height):
    volume = math.pi * (radius ** 2) * height
    mass = volume * 1000
    return round(mass, 2)

r = 0.5  
h = 1.0  
result = water_mass(r, h)
print(result)