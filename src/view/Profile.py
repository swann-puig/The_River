'''
Created on 17 sept. 2018

@author: Swann
'''

import pygame
from src.constant import PROFILE_HEIGHT, PATH_IMAGE_PROFILE
from src.modeles.Graphic_object import Graphic_object

class Profile(Graphic_object):
    '''
    classdocs
    '''
    def __init__(self, player, SCREEN_WIDTH, background_path=PATH_IMAGE_PROFILE):
        '''
        Constructor
        '''
        Graphic_object.__init__(self, player.c, background_path)
        
        self.player = player
        self.textColor = pygame.Color("0xffffff") #RRGGBB
        #------------------------------ TITLE ------------------------------
        self.fontTitle = pygame.font.SysFont("times", 36 , 1)
        self.title = self.fontTitle.render("Profile:", 1, self.textColor)
        
        #------------------------------ TEXT ------------------------------
        self.fontText = pygame.font.SysFont("times", 24)
        self.textName = self.fontText.render(player.name, 1, self.textColor)
        self.textLife = self.fontText.render("Life: ", 1, self.textColor)
        self.textAction = self.fontText.render("Action Point: ", 1, self.textColor)
        
        self.buttonEndTurn = self.fontText.render("END TURN", 1, pygame.Color("0xff0000"))
        
        #------------------------------ CONFIG ------------------------------
        self.inter_line = self.textAction.get_height() + 6
        self.padx, self.pady = 5, 5
        
        size = self.textAction.get_width() + 100
        self.rect = pygame.Rect(SCREEN_WIDTH/2 - size/2, 0, size, PROFILE_HEIGHT)
        
        if False:
            self.rect = pygame.image.load(background_path).convert_alpha()
            self.rect.x = SCREEN_WIDTH/2 - self.rect.width/2
            self.rect.y = 0
            
        #------------------------------ value temp ------------------------------
        self.value_life = 0
        self.value_action = 0
        self.life = None
        self.action = None
        
        self.visible(False)
        self.set_interactive(True)
        
    def get_width(self):
        return self.rect.width
        
    def check_change(self):
        if (self.value_life != self.player.get_life() or self.value_action != self.player.get_action_point()):
            self.life = self.fontText.render(str(self.player.get_life()), 1, self.textColor)
            self.action = self.fontText.render(str(self.player.get_action_point()), 1, self.textColor)
        
    def mouse_pressed(self, event):
        pass
            
    def mouse_released(self, event):
        if (self.rect.x + self.padx < event.pos[0] and event.pos[0] < self.rect.x + self.padx + self.buttonEndTurn.get_width()
             and self.rect.y + self.inter_line*4 + self.pady < event.pos[1] and event.pos[1] < self.rect.y + self.inter_line*4 + self.pady + self.buttonEndTurn.get_height()):
            self.player.c.end_turn()
            
    def mouse_motion(self, event):
        pass
        
    def update(self, view):
        self.check_change()
        pygame.draw.rect(view.window, pygame.Color("black"), self.rect) # a remplacer par l'image de fond
        pygame.draw.rect(view.window, self.textColor, self.rect, 2)
        view.window.blit(self.title,      (self.rect.x + self.rect.width/2 - self.title.get_width()/2,  self.rect.y + self.pady))
        
        view.window.blit(self.textName,   (self.rect.x + self.padx,  self.rect.y + self.inter_line + self.pady))
        
        view.window.blit(self.textLife,   (self.rect.x + self.padx,  self.rect.y + self.inter_line*2 + self.pady))
        view.window.blit(self.life,       (self.rect.x + self.padx + self.textLife.get_width() + 10,    self.rect.y + self.inter_line*2 + self.pady))
        
        view.window.blit(self.textAction, (self.rect.x + self.padx,  self.rect.y + self.inter_line*3 + self.pady))
        view.window.blit(self.action,     (self.rect.x + self.padx + self.textAction.get_width() + 10,  self.rect.y + self.inter_line*3 + self.pady))
        
        view.window.blit(self.buttonEndTurn, (self.rect.x + self.padx,  self.rect.y + self.inter_line*4 + self.pady))
        
    
    