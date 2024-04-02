import itertools 

def create_grid():
    
    # set ranges for x and y axes of the table grid
    x_rng = range(1,28)
    y_rng = range(1,12)

    coords = []

    for x in x_rng:
        for x_val, y in itertools.product([x],y_rng):
            coords.append((x_val,y))

    return coords

def create_inside_pockets():
   
    # create dict and manually instantiate zero/double-zero
    inside_pocket_dict = {
        (1,3):-1,
        (1,5):0,
    }
    # represents the x values that intersect with core pocket coordinates
    core_pocket_columns = range(3, 26, 2)

    # represent the y values that intersect with core pocket coordinates, and the starting number for that row
    core_pocket_rows = [
        (2, 3),
        (4, 2), 
        (6, 1),
    ]
    
    for row in core_pocket_rows:
        
        pocket_num = row[1]

        for x_val, y in itertools.product([row[0]],core_pocket_columns):

            #print((x_val,y), pocket_num)

            inside_pocket_dict[(x_val,y)] = pocket_num

            pocket_num += 3 
    
    return inside_pocket_dict

