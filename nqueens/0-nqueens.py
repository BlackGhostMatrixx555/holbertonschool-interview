#!/usr/bin/python3
"""
N Queens puzzle solver module using backtracking.
"""
import sys


def print_usage_and_exit(message, status=1):
    """
    Prints an error message to stdout and exits with a given status.
    """
    print(message)
    sys.exit(status)


def init_arguments():
    """
    Validates the command line arguments and returns N.
    """
    if len(sys.argv) != 2:
        print_usage_and_exit("Usage: nqueens N")

    try:
        n = int(sys.argv[1])
    except ValueError:
        print_usage_and_exit("N must be a number")

    if n < 4:
        print_usage_and_exit("N must be at least 4")

    return n


def is_safe(row, col, board):
    """
    Checks if a queen can be safely placed at board[row] = col.
    """
    for i in range(row):
        if board[i] == col or abs(board[i] - col) == abs(i - row):
            return False
    return True


def solve_nqueens(row, n, board):
    """
    Recursively solves the N Queens puzzle using backtracking.
    """
    if row == n:
        solution = [[i, board[i]] for i in range(n)]
        print(solution)
        return

    for col in range(n):
        if is_safe(row, col, board):
            board[row] = col
            solve_nqueens(row + 1, n, board)


if __name__ == "__main__":
    n_queens = init_arguments()
    queen_board = [0] * n_queens
    solve_nqueens(0, n_queens, queen_board)
