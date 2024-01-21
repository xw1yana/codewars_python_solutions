def findNextSquare(sq):
    root = sq**0.5
    if root.is_integer():
        return int((root + 1)**2)
    else:
        return -1
