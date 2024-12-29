def dislike_6(a):
    if isinstance(a, (int, float)):
        return "Только не б!"
    return True

result1 = dislike_6("hello")
result2 = dislike_6(6)
print(result1, result2)