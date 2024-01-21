def rental_car_cost(d):
    day = 40
    total = day * d
    if d >=7:
        total -= 50
    elif d >=3:
        total -= 20
    return total