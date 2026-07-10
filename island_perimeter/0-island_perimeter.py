#!/usr/bin/python3
"""
Module pour calculer le périmètre d'une île dans une grille.
"""


def island_perimeter(grid):
    """
    Retourne le périmètre de l'île décrite dans la variable grid.

    Args:
        grid (list of list of integers): 0 représente l'eau, 1 la terre.

    Returns:
        int: Le périmètre total de l'île.
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Chaque bloc de terre apporte 4 côtés
                perimeter += 4

                # Connexion en haut : on annule 2 côtés
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2

                # Connexion à gauche : on annule 2 côtés
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2

    return perimeter
