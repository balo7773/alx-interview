#!/usr/bin/python3

"""
module
"""


def canUnlockAll(boxes):
    """function """
    n = len(boxes)
    unlocked = set([0])  # Start with box 0 unlocked
    keys = set(boxes[0])  # Initialize with keys from the first box
    
    while keys:
        new_key = keys.pop()
        if new_key < n and new_key not in unlocked:
            unlocked.add(new_key)
            keys.update(boxes[new_key])
    
    return len(unlocked) == n
