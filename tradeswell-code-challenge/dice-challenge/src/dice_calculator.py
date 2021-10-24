import re
import numpy as np
from src.dice import PolyHendronDie


class DiceCalculator():

    def __init__(self,expr):
        self.operations = re.findall('(\d+d\d+)|(\+)|(\-)|(\d)',expr.lower())
        self.lookup_hash = {0:'dice',1:'add',2:'subtract',3:'number'}
        self.N_ops = len(self.lookup_hash.keys())
        self.random_value = 0
        self.max_value = 0
        self.min_value = 0
        
    def get_hash_op(self,op):
        return [(i,v) for i,v in zip(range(self.N_ops),op) if v!=''][0]
        
    def add_num(self,num,sign):
        self.random_value += int(num)*sign
        self.max_value += float(num)*sign
        self.min_value += float(num)*sign   
        
    def add_dice(self,dice_expr,sign):
        polyhdie = PolyHendronDie(dice_expr)
        self.random_value += sign*polyhdie.get_dice_random_sum()
        if sign<0:
            self.max_value += sign*polyhdie.get_dice_min_sum()
            self.min_value += sign*polyhdie.get_dice_max_sum()
        else:
            self.max_value += sign*polyhdie.get_dice_max_sum()
            self.min_value += sign*polyhdie.get_dice_min_sum()

    def compute_graph(self):
        
        sign = 1
        
        for oper in self.operations:
            op_id,op_val = self.get_hash_op(oper)
            op_id = self.lookup_hash[op_id]
            if op_id=='add':
                sign=1
            if op_id=='subtract':
                sign=-1
            
            if op_id=='dice':
                print(op_val)
                self.add_dice(op_val,sign)
            if op_id=='number':
                self.add_num(op_val,sign)
            
            
            
            
            
            
                