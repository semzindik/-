def is_bust(cards):
    total = sum(cards)
    return total > 21  


cards1 = [10, 5, 7]  
cards2 = [10, 5, 4]  
cards3 = [11, 10, 1]  

print(is_bust(cards1)) 
print(is_bust(cards2)) 
print(is_bust(cards3))  