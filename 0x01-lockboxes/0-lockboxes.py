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


# boxes1 = [[1], [2], [3], [4], []]
# print(canUnlockAll(boxes1))
# boxes2 = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
# print(canUnlockAll(boxes2))
# boxes3 = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
# print(canUnlockAll(boxes3))
