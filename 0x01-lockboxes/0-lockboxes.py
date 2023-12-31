#!/usr/bin/python3
"""Interview question Practice"""
from itertools import dropwhile


def canUnlockAll(boxes):
    """This method Checks if all boxes can be unlocked"""

    keys = {0}
    available_boxes = range(len(boxes))

    while True:
        not_found = set()

        for i in available_boxes:
            if i in keys:
                for key in dropwhile(lambda k: k in keys, boxes[i]):
                    keys.add(key)
            else:
                not_found.add(i)

        if available_boxes == not_found:
            return False

        if not not_found:
            return True

        available_boxes = not_found
