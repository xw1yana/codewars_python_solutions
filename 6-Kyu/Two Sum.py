def two_sum(numbers, target):
    num_to_index = {}
    for index, num in enumerate(numbers):
        complement = target - num
        if complement in num_to_index:
            return (num_to_index[complement], index)
        num_to_index[num] = index
    return None  # In case there is no solution

