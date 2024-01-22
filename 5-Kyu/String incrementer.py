def increment_string(s):
    i = len(s)
    while i > 0 and s[i-1].isdigit():
        i -= 1

    non_numeric = s[:i]
    numeric = s[i:]

    if not numeric:
        return s + '1'

    length = len(numeric)
    new_number = str(int(numeric) + 1).zfill(length)

    return non_numeric + new_number
