import itertools 

# set ranges for x and y axes of the table grid
x_rng = range(1,28)
y_rng = range(1,27)

def create_grid(x_r, y_r):

    coords = []

    for x in x_rng:
        for x_val, y in itertools.product([x],y_rng):
            coords.append((x_val,y))

    return coords
