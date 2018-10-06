'''
Created on 19 sept. 2018

@author: Swann
'''

from src.modeles.Graphic_object import Graphic_object
from src.constant import PATH_IMAGE_HAND, MAX_CARD_IN_HAND
import pygame

class Hand(Graphic_object):
    '''
    classdocs
    '''


    def __init__(self, controller, width, x, display_card_y):
        '''
        Constructor
        '''
        Graphic_object.__init__(self, controller, PATH_IMAGE_HAND, x, display_card_y)
        
        self.group = pygame.sprite.LayeredUpdates()
        self.gridx = width/MAX_CARD_IN_HAND
        self.y = display_card_y
        self.layer = 0
        
    def add_card(self, card):
        if (len(self.group) < MAX_CARD_IN_HAND):
            self.group.add(card, layer=self.layer)
            #self.group.move_to_front(card)
            self.layer += 1
            self.c.resize_card_hand(card)
            card.set_interactive(True)
            self.refresh_all_pos()
            return True
        return False
        
    def remove(self, card):
        self.group.remove(card)
        self.refresh_all_pos()
        
    def refresh_all_pos(self):
        for index, card in enumerate(self.group):
            card.set_position(index * self.gridx, self.y)
        
    def visible(self, state):
        super().visible(state)
        for card in self.group:
            card.visible(state)
    
    def set_interactive(self, state):
        super().set_interactive(state)
        for card in self.group:
            card.set_interactive(state)
        
    def update(self):
        super().update()
        if self.is_visible:
            self.c.display_group(self.group)
        
        
        