def mul_to_int(a, b):
    result = a * b
    if result.is_integer():
        return int(result)
    return result

result1 = mul_to_int(2, 3)
result2 = mul_to_int(2.5, 4)
print(result1, result2)