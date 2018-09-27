'''
Created on 17 sept. 2018

@author: Swann
'''
from src.modeles.Card import Card
#from pygame.locals import LEFT

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
        power = self.stats.power
        for card in self.equipped_card:
            power += card.get_power_bonus(self)
            
        return power
        
    def get_movement(self):
        return self.stats.movement
        
    def get_range(self):
        return self.stats.range
        
    def get_capacity(self):
        return self.stats.capacity
    
    def can_equip(self, card):
        return (self.get_capacity() >= card.stats.weight)
    
    def equip(self, card):
        if self.can_equip(card):
            self.equipped_card.append(card)
            return True
        return False
        
    def mouse_pressed(self, event):
        if (self.rect.collidepoint(event.pos) and self.posed):
            if (event.button == 1): # LEFT clic
                self.c.deselect_from_board()
                self.c.select_from_board(self)
                super().mouse_pressed(event)
            elif (event.button == 3): # RIGHT clic
                self.c.display_details(self, event.pos)
                
        else:
            super().mouse_pressed(event)
        
    def mouse_released(self, event):
        if (self.posed):
            self.c.move_card_posed(self, (self.rect.x - self.offset_x, self.rect.y - self.offset_y))

        super().mouse_released(event)
        
    def mouse_motion(self, event):
        super().mouse_motion(event)
        
        