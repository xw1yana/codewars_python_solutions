def persistence(num):
    def multiply_digits(n):
        result = 1
        for digit in str(n):
            result *= int(digit)
        return result
    count = 0
    while num >= 10:
        num = multiply_digits(num)
        count += 1
    return count
