def to_float(num):
    try:
        return float(num)
    except (ValueError, TypeError):
        return "Невозможно преобразовать"

result1 = to_float(10)
result2 = to_float("3.14")
result3 = to_float([1, 2, 3])
print(result1, result2, result3)