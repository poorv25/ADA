def coin_change(coins, amount):
    # Initialize a list to store the minimum number of coins needed to make up each amount up to the target amount
    dp = [float('inf')] * (amount+1)
    dp[0] = 0  # Base case: it takes 0 coins to make up an amount of 0

    # Iterate through all the amounts from 1 to the target amount
    for i in range(1, amount+1):
        # Iterate through all the available coins
        for coin in coins:
            # Check if the current coin can be used to make up the current amount
            if coin <= i:
                # If the current coin is used, update the minimum number of coins needed for the current amount
                dp[i] = min(dp[i], dp[i-coin]+1)

    if dp[amount] == float('inf'):
        # If no combination of coins can make up the target amount, return -1
        return -1
    else:
        # Otherwise, return the minimum number of coins needed to make up the target amount
        return dp[amount]
