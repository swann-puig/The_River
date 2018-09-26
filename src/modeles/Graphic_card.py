'''
Created on 18 sept. 2018

@author: Swann
'''

import pygame
from src.modeles.Graphic_object import Graphic_object

class Graphic_card(Graphic_object):
    '''
    classdocs
    '''


    def __init__(self, controller, owner, image_path):
        '''
        Constructor
        '''
        Graphic_object.__init__(self, controller, image_path)
        self.owner = owner
        self.image_origine = self.image
        self.location = None
        self.posed = False
        
        
    def set_location(self, location):
        self.location = location
        
    def get_location(self):
        return self.location
    
    def is_posed(self):
        return self.posed
    
    def set_posed(self, Bool):
        self.posed = Bool
    
    def mouse_pressed(self, event):
        if (self.rect.collidepoint(event.pos) and not self.posed):
            if (self.c.is_display_priority(self, event.pos)):
                super().mouse_pressed(event)
                self.c.select_from_hand(self)
                self.c.display_details(self, event.pos, remove=True)
        
        else:
            super().mouse_pressed(event)
        
    def mouse_released(self, event):
        if (self.get_location() == self.c.board and not self.posed):
            self.c.place_card_on_board(self, (self.rect.x - self.offset_x, self.rect.y - self.offset_y))
        
        if (self.drag and not self.posed): # verification une 2eme fois car l'etat a peut etre change
            self.c.card_released_in_wrong_place(self)
            
        super().mouse_released(event)
        
    def mouse_motion(self, event):
        if (self.drag):
            if (self.c.is_in_board(event.pos) and self.location != self.c.board):
                self.c.resize_card_board(self)
                self.offset_x = -self.rect.center[0]
                self.offset_y = -self.rect.center[1]
                self.location = self.c.board

            elif (not self.c.is_in_board(event.pos) and self.location != None and not self.posed):
                self.location = None
                self.c.resize_card_hand(self)
                self.offset_x = -self.rect.center[0]
                self.offset_y = -self.rect.center[1]
                
        elif (self.rect.collidepoint(event.pos) and not self.posed):
            self.c.display_details(self, event.pos)
                
        super().mouse_motion(event)
        
        
        
        