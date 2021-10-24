import numpy as np

class PolyHendronDie():

    def __init__(self,dice_expr):

        self.dice_expr = dice_expr.lower()
        rolls,sides = self.dice_expr.split('d')
        self.rolls = int(rolls)
        self.sides = int(sides)
        self._dice_random_sum = 0
        self._dice_max_sum = 0
        self._dice_min_sum = 0
        self.dice_random_sum()
        self.dice_max_sum()
        self.dice_min_sum()
        
    def get_dice_random_sum(self):
        return self._dice_random_sum
        
    def get_dice_max_sum(self):
        return self._dice_max_sum
    
    def get_dice_min_sum(self):
        return self._dice_min_sum
        
    def roll_die(self):
        return np.random.choice(range(1,self.sides+1))
        
    def max_die(self):
        return self.sides
        
    def min_die(self):
        return 1
        
    def dice_random_sum(self):
        for _ in range(self.rolls):
            self._dice_random_sum+=self.roll_die()
            
    def dice_max_sum(self):
        for _ in range(self.rolls):
            self._dice_max_sum+=self.max_die()
        
    def dice_min_sum(self):
        for _ in range(self.rolls):
            self._dice_min_sum+=self.min_die()
    