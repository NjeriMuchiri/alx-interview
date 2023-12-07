#!/usr/bin/python3

def canUnlockAll(boxes):
    if not any(boxes):
        return False
    n = len(boxes)
    opened = [False] * n
    opened[0] = True
    boxList = [0]

    while boxList:
        current_box = boxList.pop()
        for key in boxes[current_box]:
            if 0 <= key and not opened[key]:
                opened[key] = True
                boxList.append(key)
    return all(opened)
