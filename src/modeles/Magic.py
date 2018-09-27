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
        