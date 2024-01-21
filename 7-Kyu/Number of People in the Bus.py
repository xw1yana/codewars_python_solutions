def number(bus_stops):
    total_people = 0
    for a, b in bus_stops:
        total_people += a - b
    return max(0, total_people)

