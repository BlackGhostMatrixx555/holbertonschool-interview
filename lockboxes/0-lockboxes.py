#!/usr/bin/python3
"""Module that determines if all locked boxes can be opened."""


def canUnlockAll(boxes):
    """Determine if all boxes can be opened.

    Args:
        boxes (list of lists): each box contains keys to other boxes.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    n = len(boxes)
    unlocked = set([0])
    queue = [0]
    while queue:
        box = queue.pop()
        for key in boxes[box]:
            if key < n and key not in unlocked:
                unlocked.add(key)
                queue.append(key)
    return len(unlocked) == n
