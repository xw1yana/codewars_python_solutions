def sum_mix(arr):
    return sum(int(x) if isinstance(x, (int, str)) else x for x in arr)