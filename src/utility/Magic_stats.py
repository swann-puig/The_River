'''
Created on 16 sept. 2018

@author: Swann
'''

class Magic_stats():
    '''
    Standard of stats about a creature card.
    '''
    def __init__(self, power, castle_life, move, attack_range, weight):
        '''
        Constructor
        '''
        self.power = power
        self.castle_life = castle_life
        self.movement = move
        self.range = attack_range
        self.weight = weight
        