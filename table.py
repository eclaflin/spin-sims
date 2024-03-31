# define 'red' numbers
red = [
    1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36
]

# parent class of inside and outside pockets
class Pocket:
    # need an attribute corresponding to it's "core" position on the grid
    def __init__(self, grid_x, grid_y):
        self.pocket_grid_x = grid_x
        self.pocket_grid_y = grid_y
        self.grid_coordinate = (self.pocket_grid_x, self.pocket_grid_y)

class InsidePocket(Pocket):
    def __init__(self, grid_x, grid_y, p_number): 
        super().__init__(grid_x, grid_y)
        
        self.p_number = p_number

    def is_winning(self, spin_result):

        if spin_result == self.p_number:
            return True
        
        else:
            return False

