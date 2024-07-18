# Input coins and amount from user
coins = list(map(int, input().split()))
amount = int(input())

def coinChange(coins, amount):
    # Create a list for dynamic programming and initialize it
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0
    
    # Iterate through each coin
    for coin in coins:
        for x in range(coin, amount + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)
    
    # Return the result
    return dp[amount] if dp[amount] != amount + 1 else -1

# Compute the result
result = coinChange(coins, amount)
print(result)
