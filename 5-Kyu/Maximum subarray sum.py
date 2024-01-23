def max_sequence(arr):
    if not arr:
        return 0

    max_end = max_so_far = 0

    for num in arr:
        max_end = max(0, max_end + num)
        max_so_far = max(max_so_far, max_end)
    return max_so_far
