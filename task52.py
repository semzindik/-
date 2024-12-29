def number_to_russian(n):
    if n < 0 or n > 999:
        raise ValueError("Число должно быть в диапазоне от 0 до 999")

    units = ["", "один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять"]
    teens = ["десять", "одиннадцать", "двенадцать", "тринадцать", "четырнадцать", 
             "пятнадцать", "шестнадцать", "семнадцать", "восемнадцать", "девятнадцать"]
    tens = ["", "десять", "двадцать", "тридцать", "сорок", "пятьдесят", 
            "шестьдесят", "семьдесят", "восемьдесят", "девяносто"]
    hundreds = ["", "сто", "двести", "триста", "четыреста", "пятьсот", 
                "шестьсот", "семьсот", "восемьсот", "девятьсот"]

    if n == 0:
        return "ноль"

    result = []

    
    h = n // 100
    if h > 0:
        result.append(hundreds[h])

    
    t = (n % 100) // 10
    if t == 1 and n % 10 != 0: 
        result.append(teens[n % 10])
    else:
        if t > 0:
            result.append(tens[t])

    
    u = n % 10
    if t != 1:  
        result.append(units[u])

    return ' '.join(result).strip()


print(number_to_russian(0))    
print(number_to_russian(5))    
print(number_to_russian(12))  
print(number_to_russian(25))   
print(number_to_russian(105))  
print(number_to_russian(999))  