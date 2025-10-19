# functional programming uses pure functions and higher-order functions
def area(rect):
    return rect[0] * rect[1]

rectangles = [(5, 3), (2, 8), (6, 4)]
areas = list(map(area, rectangles))

print("Areas:", areas)