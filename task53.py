def count_lucky_numbers(n):
    if n % 2 != 0:
        return 0 

    half_length = n // 2
    max_digit_sum = 9 * half_length 


    dp = [0] * (max_digit_sum + 1)
    dp[0] = 1  

    for _ in range(half_length):
        new_dp = [0] * (max_digit_sum + 1)
        for digit in range(10):  
            for sum_value in range(max_digit_sum - digit + 1):
                new_dp[sum_value + digit] += dp[sum_value]
        dp = new_dp


    return sum(count * count for count in dp)


print(count_lucky_numbers(2))
print(count_lucky_numbers(4)) 
print(count_lucky_numbers(6))