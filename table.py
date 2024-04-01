
# types of outside pockets 
outside_types = {
    'red_black':['red', 'black'],
    'even_odd':['even', 'odd'], 
    'hi_lo':['hi', 'lo'],
    'dozen':['first', 'second', 'third'],

    # 2:1 row bets correspond row-wise to a result 
    # so in the table grid this integer represents the y coordinate of the inside pocket row
    'two_one':[2,4,6]
}

# parent class of inside and outside pockets
class Pocket:
    # Takes args corresponding to it's "core" position on the grid
    def __init__(self, grid_x, grid_y):
        self.pocket_grid_x = grid_x
        self.pocket_grid_y = grid_y

        # creating a tuple that represents an (x,y) coordinate
        self.grid_coordinate = (self.pocket_grid_x, self.pocket_grid_y)

# since an inside pocket is 1-1 with a spin-result, this child class straightforward
# TODO: testing to make sure grid position is valid to number
class InsidePocket(Pocket):
    def __init__(self, grid_x, grid_y, p_number): 
        super().__init__(grid_x, grid_y)
        
        # TODO: type handling for double-zero 
        self.p_number = p_number

    def is_winning(self, spin_result):

        if spin_result == self.p_number:
            return True
        
        else:
            return False


"""
Outside Pockets work differently because:
1. They can represent multiple inside pockets
2. Whether or not they win is determined differently 
according to what type of outside pocket it is 
"""

red_colors = [
    1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36
]


# define methods for calculating outside bet wins
# these will be passed as values in the dictionary of 
# outside bet attributes

def red_or_black_win(spin_result, outside_pocket_color):
    pass
            
def even_odd_win(spin_result, outside_pocket_even):
    pass

def hi_lo_win(spin_result, outside_pocket_hi_lo):
    pass

def dozen_win(spin_result, outside_pocket_dozen):
    pass

def two_one_win(spin_result, outside_pocket_row):
    pass

# types of outside pockets 
outside_pocket_meta = {
    'red_black':['red', 'black'],
    'even_odd':['even', 'odd'], 
    'hi_lo':['hi', 'lo'],
    'dozen':['first', 'second', 'third'],

    # 2:1 row bets correspond row-wise to a result 
    # so in the table grid this integer represents the y coordinate of the inside pocket row
    'two_one':[2,4,6]
}


class OutsidePocket(Pocket):
    def __init__(self, grid_x, grid_y, outside_type, name):
        super().__init__(grid_x, grid_y)

        # TODO: validate that type is a valid type and name is valid for the type
        self.outside_type = outside_type 
        self.name = name 
  
