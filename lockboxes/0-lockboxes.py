#!/usr/bin/python3
""" Lockboxes module """


def canUnlockAll(boxes):
    newList = []
    n = len(boxes)

    if not isinstance(boxes, list):
        return False

    for i in boxes:
        if len(i) == 0 and i is not boxes[n - 1]:
            return False
        for j in i:
            newList.append(j)
    for index, key in enumerate(boxes):
        if index in newList or index < n - 1:
            return True
        else:
            return False
