def sum_array(arr):
    if type(arr) != list:
        return 0
    if len(arr) < 3:
        return 0
    arr = sorted(arr)
    min = arr[0]
    max = arr[-1]
    return sum(arr) - min - max