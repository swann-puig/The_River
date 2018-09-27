'''
Created on 17 sept. 2018

@author: Swann
'''
from src.modeles.Card import Card
from src.constant import MAGIC, TRAP

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
            if (card.infos.type == MAGIC): power += card.get_power_bonus(self)
            
        return power
        
    def get_movement(self):
        m = self.stats.movement
        for card in self.equipped_card:
            if (card.infos.type == MAGIC): m += card.get_movement_bonus()
            
        return m
        
    def get_range(self):
        r = self.stats.range
        for card in self.equipped_card:
            if (card.infos.type == MAGIC): r += card.get_range_bonus()
            
        return r
        
    def get_capacity(self):
        c = self.stats.capacity
        for card in self.equipped_card:
            c -= card.get_weight()
            
        return c
    
    def can_equip(self, card):
        return (self.get_capacity() >= card.get_weight())
    
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
        
        