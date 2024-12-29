def help_bool(letter):
    if letter == 'к':
        return "Коммутативность: A AND B = B AND A и A OR B = B OR A"
    elif letter == 'а':
        return "Ассоциативность: (A AND B) AND C = A AND (B AND C) и (A OR B) OR C = A OR (B OR C)"
    elif letter == 'д':
        return "Дистрибутивность: A AND (B OR C) = (A AND B) OR (A AND C) и A OR (B AND C) = (A OR B) AND (A OR C)"
    elif letter == 'м':
        return "Правило де Моргана: NOT (A AND B) = (NOT A) OR (NOT B) и NOT (A OR B) = (NOT A) AND (NOT B)"
    else:
        return ("Пожалуйста, используйте одну из следующих букв:\n"
                "к - коммутативность\n"
                "а - ассоциативность\n"
                "д - дистрибутивность\n"
                "м - правило де Моргана")

print(help_bool('к'))
print(help_bool('а'))
print(help_bool('д'))
print(help_bool('м'))
print(help_bool('x'))  