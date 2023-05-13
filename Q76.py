def coin_change_greedy(coins, amount):
    coins.sort(reverse=True)  # sort coins in descending order
    result = []
    for coin in coins:
        while coin <= amount:
            result.append(coin)
            amount -= coin
    if amount == 0:
        return result
    else:
        return None  # no exact change possible
