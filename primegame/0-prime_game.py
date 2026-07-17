#!/usr/bin/python3
"""
Prime Game
"""


def isWinner(x, nums):
    """
    Determines the winner of a set of prime game rounds.
    
    Args:
        x (int): Number of rounds.
        nums (list): Array of n for each round.
        
    Returns:
        str: Name of the player that won the most rounds.
             If the winner cannot be determined, returns None.
    """
    if not nums or x < 1:
        return None

    # Find the maximum n to bound our Sieve of Eratosthenes
    max_n = max(nums)
    if max_n < 1:
        return None

    # Step 1: Sieve of Eratosthenes to find all primes up to max_n
    is_prime = [True] * (max_n + 1)
    is_prime[0] = is_prime[1] = False
    
    for i in range(2, int(max_n**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, max_n + 1, i):
                is_prime[j] = False

    # Step 2: Precompute the cumulative count of primes up to each index
    prime_counts = [0] * (max_n + 1)
    for i in range(1, max_n + 1):
        prime_counts[i] = prime_counts[i - 1] + (1 if is_prime[i] else 0)

    # Step 3: Determine the winner for each round
    maria_wins = 0
    ben_wins = 0

    for n in nums[:x]:
        # If the number of primes up to n is odd, Maria wins. Even, Ben wins.
        if prime_counts[n] % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    # Step 4: Return the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
