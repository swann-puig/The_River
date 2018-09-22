'''
Created on 17 sept. 2018

@author: Swann
'''
from src.modeles.Card import Card

class Creature(Card):
    '''
    classdocs
    '''

    def __init__(self, controller, owner, card_infos, creature_stats):
        '''
        Constructor
        '''
        Card.__init__(self, controller, card_infos, owner, False)
        
        self.stats = creature_stats
        self.equipped_card = []
        
    def mouse_pressed(self, event):
        super().mouse_pressed(event)
        
    def mouse_released(self, event):
        super().mouse_released(event)
            
        
    def mouse_motion(self, event):
        super().mouse_motion(event)