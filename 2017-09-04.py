def get_circle_coordinates(circle):
    x = circle[0]
    y = circle[1]
    r = circle[2]

    return (x+r,y+r),(x+r,y-r),(x-r,y+r),(x-r,y-r)

coordinates = []

for i in range(4):
    line = input()
    circle = list(map(float, line.split(',')))
    coordinates += get_circle_coordinates(circle)
    
max_x = round(max(coordinates, key=lambda x:x[0])[0], 3)
max_y = round(max(coordinates, key=lambda x:x[1])[1], 3)
min_x = round(min(coordinates, key=lambda x:x[0])[0], 3)
min_y = round(min(coordinates, key=lambda x:x[1])[1], 3)

print("({0:.3f}, {1:.3f}), ({0:.3f}, {2:.3f}), ({3:.3f}, {1:.3f}), ({3:.3f}, {2:.3f})".format(min_x, min_y, max_y, max_x))