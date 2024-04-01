
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

    if spin_result < 1:
        spin_color ='green'

    elif spin_result in red_colors:
        spin_color = 'red'

    else:
        spin_color 'black'

    return True if spin_color == outside_pocket_color else return False

def even_odd_win(spin_result, outside_pocket_even):

    if spin_result < 1:
        even_odd = None

    elif spin_result % 2 == 0:
        even_odd ='even' 

    else:
        even_odd = 'odd'

    return True if even_odd == outside_pocket_even else return False

def hi_lo_win(spin_result, outside_pocket_hi_lo):
    
    if spin_result < 1:
        hi_lo = None 

    elif spin_result >= 19:
        hi_lo = 'hi'

    else:
        return 'lo'

    return True if hi_lo == outside_pocket_hi_lo else return False

def dozen_win(spin_result, outside_pocket_dozen):
    
    if spin_result < 1:
        dozen = None 

    elif spin_result <= 12:
        dozen = 'first'

    elif spin_result <= 24:
        dozen = 'second'

    else:
        dozen = 'third'

    return True if doz == outside_pocket_dozen else return False

def two_one_win(spin_result, outside_pocket_row):

    # TODO: figure out how to make this work 
    pass

# types of outside pockets 
outside_pocket_meta = {
    'red_black':{
        'options': ['red', 'black', 'green'], 
        'win_function': red_or_black_win
    }, 
    'even_odd':{
        'options': ['even', 'odd'], 
        'win_function': even_odd_win
    }, 
    'hi_lo':{
        'options': ['hi', 'lo'], 
        'win_function': hi_lo_win
    },
    'dozen':{
        'options':['first', 'second','thid'], 
        'win_function': dozen_win
    }, 
    'two_one':{
        # these coorespond to y-axis values in board grid
        'options':[2,4,6], 
        'win_function': two_won_win
    }
}


class OutsidePocket(Pocket):
    def __init__(self, grid_x, grid_y, outside_type, name):
        super().__init__(grid_x, grid_y)

        # TODO: validate that type is a valid type and name is valid for the type
        self.outside_type = outside_type 
        self.name = name

        self.win_function = outside_pocket_meta[outside_type]['win_function']
    
    def is_winning(self, spin_result):
        
        return self.win_function(spin_result, self.name)
