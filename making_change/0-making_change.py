#!/usr/bin/python3
"""
Module pour résoudre le problème du rendu de monnaie (Coin Change).
"""


def makeChange(coins, total):
    """
    Calcule le nombre minimum de pièces pour atteindre un total donné.
    """
    if total <= 0:
        return 0

    dp = [total + 1] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    if dp[total] > total:
        return -1

    return dp[total]
    