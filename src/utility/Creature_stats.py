'''
Created on 16 sept. 2018

@author: Swann
'''

class Creature_stats():
    '''
    Standard of stats about a creature card.
    '''
    def __init__(self, power, move, attack_range, capacity):
        '''
        Constructor
        '''
        self.max_power = power
        self.power = power
        self.movement = move
        self.range = attack_range
        self.capacity = capacity