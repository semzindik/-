def rock_paper_scissors(player1, player2):
    choices = ["камень", "ножницы", "бумага"]
    
    if player1 not in choices or player2 not in choices:
        return "Некорректный ввод. Пожалуйста, выберите 'камень', 'ножницы' или 'бумага'."
    
    if player1 == player2:
        return "Ничья!"
    
    if (player1 == "камень" and player2 == "ножницы") or \
       (player1 == "ножницы" and player2 == "бумага") or \
       (player1 == "бумага" and player2 == "камень"):
        return "Игрок 1 выиграл!"
    else:
        return "Игрок 2 выиграл!"

result = rock_paper_scissors("камень", "ножницы")
print(result)