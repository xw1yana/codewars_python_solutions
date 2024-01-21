def stray(arr):
    result = 0
    for item in arr:
        result ^= item
    return result