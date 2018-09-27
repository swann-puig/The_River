'''
Created on 27 sept. 2018

@author: swann
'''
from src.modeles.Card import Card

class Magic(Card):
    '''
    classdocs
    '''

    def __init__(self, controller, owner, card_infos, creature_stats):
        '''
        Constructor
        '''
        Card.__init__(self, controller, card_infos, owner, False)
        
        self.stats = creature_stats
        
    def get_power_bonus(self, creature):
        return self.stats.power
    
    def get_castle_life_bonus(self, castle):
        return self.stats.castle_life
    
    def get_movement_bonus(self):
        return self.stats.movement
    
    def get_range_bonus(self):
        return self.stats.range
    
    def get_weight(self):
        return self.stats.weight
        