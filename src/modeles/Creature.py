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
        
    def get_max_power(self):
        return self.stats.max_power
        
    def get_power(self):
        return self.stats.power
        
    def get_movement(self):
        return self.stats.movement
        
    def get_range(self):
        return self.stats.range
        
    def get_capacity(self):
        return self.stats.capacity
        
    def mouse_pressed(self, event):
        super().mouse_pressed(event)
        if (self.rect.collidepoint(event.pos) and self.posed):
            print("DSK")
            self.c.display_move_zone(self)
        
    def mouse_released(self, event):
        super().mouse_released(event)
        self.c.remove_move_zone()
        
    def mouse_motion(self, event):
        super().mouse_motion(event)