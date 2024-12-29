def can_distribute_coins(coins):
    total_coins = sum(coins) 
    return total_coins % 3 == 0  


coins_list1 = [1, 2, 3, 4, 5] 
coins_list2 = [1, 2, 3]       
coins_list3 = [1, 2, 4]       

print(can_distribute_coins(coins_list1)) 
print(can_distribute_coins(coins_list2)) 
print(can_distribute_coins(coins_list3))  