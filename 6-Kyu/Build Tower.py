def tower_builder(n_floors):
    tower = []
    for i in range(1, n_floors + 1):
        stars = '*' * (2 * i - 1)
        spaces = ' ' * (n_floors - i)
        tower.append(spaces + stars + spaces)
    return tower
