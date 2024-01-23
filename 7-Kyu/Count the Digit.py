def nb_dig(n, d):
    count = 0
    for k in range(n + 1):
        count += str(k**2).count(str(d))
    return count
