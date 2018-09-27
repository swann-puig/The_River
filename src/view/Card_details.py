'''
Created on 21 sept. 2018

@author: Swann
'''

from src.constant import PATH_IMAGE_DETAILS_C, PATH_IMAGE_DETAILS_M, PATH_IMAGE_DETAILS_T, PATH_IMAGE_DETAILS_A, CREATURE, MAGIC, TRAP, ACTION
from src.constant import DETAILS_NAME_WIDTH, DETAILS_POWER_WIDTH, DETAILS_DESCRIPTION_WIDTH, DETAILS_OTHER_WIDTH
import pygame

class Card_details():
    '''
    classdocs
    '''


    def __init__(self, card, SCREEN_WIDTH, x, y, percent=1):
        '''
        Constructor
        '''
        self.card = card
        if (card.infos.type == CREATURE):
            self.image = pygame.image.load(PATH_IMAGE_DETAILS_C).convert_alpha()
        elif (card.infos.type == MAGIC):
            self.image = pygame.image.load(PATH_IMAGE_DETAILS_M).convert_alpha()
        elif (card.infos.type == TRAP):
            self.image = pygame.image.load(PATH_IMAGE_DETAILS_T).convert_alpha()
        else:
            self.image = pygame.image.load(PATH_IMAGE_DETAILS_A).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x - self.rect.width/2
        self.rect.y = y
        self.image_card = card.image_origine
        self.SCREEN_WIDTH = SCREEN_WIDTH
        
        self.textColor = pygame.Color("0x000000") #RRGGBB
        #------------------------------ NAME ------------------------------
        self.fontName = None
        self.name = None
        self.fontFamily = None
        self.family = None
        
        #------------------------------ TEXT ------------------------------
        self.fontText = None
        self.description = None
        
        #------------------------------ STATS ------------------------------
        self.fontStats = None
        if (card.infos.type != "action"):
            # Common
            self.fontPower = None
            self.power = None
            self.movement = None
            self.range = None
            self.capacity_weight = None
        
        else:
            self.action_point = None
            
        #------------------------------ POSITIONS FIXED MANUALLY ------------------------------
        self.pos_name = (15, 0)
        self.pos_family = None # dépend de name
        self.pos_description = (20, 405)
        
        y = 345
        if (card.infos.type != "action"):
            self.pos_power = (20, y)
            x = 160
            self.pos_movement = (self.pos_power[0] + DETAILS_POWER_WIDTH + 10, y)
            self.pos_range = (self.pos_movement[0] + DETAILS_OTHER_WIDTH/3, y)
            self.pos_capacity_weight = (self.pos_movement[0] + 2*DETAILS_OTHER_WIDTH/3, y)
        
        else:
            self.pos_action_point= (20, y)
        
        self.resize(percent)
        
    def get_good_font_size(self, font_name, desired_width, text, bold=False, italic=False):
        max_size = 60
        min_size = 8
        for size in range(0, max_size-min_size):
            font = pygame.font.SysFont(font_name, max_size-size, bold, italic)
            if (font.size(text)[0] <= desired_width):
                return font
            
        return pygame.font.SysFont(font_name, min_size, bold, italic)
        
    def resize(self, percent):
        
        #------------------------------ NAME ------------------------------
        self.fontName = self.get_good_font_size("times", DETAILS_NAME_WIDTH*percent, self.card.infos.name, bold=True)
        self.name = self.fontName.render(self.card.infos.name, True, self.textColor)
        self.fontFamily = self.get_good_font_size("times", DETAILS_NAME_WIDTH*percent, self.card.infos.family, italic=True)
        self.family = self.fontFamily.render(self.card.infos.family, True, self.textColor)
        
        #------------------------------ TEXT ------------------------------
        self.fontText = self.get_good_font_size("times", DETAILS_DESCRIPTION_WIDTH*percent, self.card.infos.description)
        self.description = self.fontText.render(self.card.infos.description, True, self.textColor)
        
        #------------------------------ STATS ------------------------------
        self.fontStats = self.get_good_font_size("times", DETAILS_OTHER_WIDTH*percent/4, "M:" + str(self.card.stats.movement), bold=True)
        if (self.card.infos.type == "creature"):
            # Common
            self.fontPower = self.get_good_font_size("times", DETAILS_POWER_WIDTH*percent, "Power:" + str(self.card.stats.power), bold=True)
            self.power = self.fontPower.render("Power:" + str(self.card.get_power()), True, self.textColor)
            self.movement = self.fontStats.render("M:" + str(self.card.get_movement()), True, self.textColor)
            self.range = self.fontStats.render("R:" + str(self.card.get_range()), True, self.textColor)
            self.capacity_weight = self.fontStats.render("C:" + str(self.card.get_capacity()), True, self.textColor)
            
                
        elif (self.card.infos.type == "magic"):
            self.fontPower = self.get_good_font_size("times", DETAILS_POWER_WIDTH*percent, "Power:" + str(self.card.stats.power), bold=True)
            self.power = self.fontPower.render("Power:" + str(self.card.get_power_bonus(None)), True, self.textColor)
            self.movement = self.fontStats.render("M:" + str(self.card.stats.movement), True, self.textColor)
            self.range = self.fontStats.render("R:" + str(self.card.stats.range), True, self.textColor)
            self.capacity_weight = self.fontStats.render("W:" + str(self.card.stats.weight), True, self.textColor)
        
        else:
            self.action_point = self.fontStats.render("Action:" + str(self.card.stats.action_point), True, self.textColor)
            
        
        self.pos_name = (self.pos_name[0] * percent, self.pos_name[1] * percent)
        self.pos_family = (self.pos_name[0], self.pos_name[1] + self.name.get_height() - 12 * percent)
        self.pos_description = (self.pos_description[0] * percent, self.pos_description[1] * percent)
        
        if (self.card.infos.type != "action"):
            self.pos_power = (self.pos_power[0] * percent, self.pos_power[1] * percent)
            self.pos_movement = (self.pos_power[0] + (DETAILS_POWER_WIDTH+10) * percent, self.pos_movement[1] * percent)
            self.pos_range = (self.pos_movement[0] + DETAILS_OTHER_WIDTH * percent/3, self.pos_range[1] * percent)
            self.pos_capacity_weight = (self.pos_movement[0] + 2*DETAILS_OTHER_WIDTH * percent/3, self.pos_capacity_weight[1] * percent)
        
        else:
            self.pos_action_point= (self.pos_action_point[0] * percent, self.pos_action_point[1] * percent)

        x = self.rect.x + self.rect.width/2
        self.image = pygame.transform.scale(self.image, (round(self.rect.width*percent), round(self.rect.height*percent)))
        self.image_card = pygame.transform.scale(self.image_card, (round(self.image_card.get_width()*percent), round(self.image_card.get_height()*percent)))
        
        self.rect = self.image.get_rect()
        self.rect.x = x - self.rect.width/2
        if (self.rect.x < 0): self.rect.x = 0
        if (self.rect.x + self.rect.width > self.SCREEN_WIDTH): self.rect.x = self.SCREEN_WIDTH - self.rect.width
        
        return self
        
    def update(self, view):
        view.window.blit(self.image_card, (self.rect.x, self.rect.y))
        view.window.blit(self.image, (self.rect.x, self.rect.y))
        view.window.blit(self.name, (self.rect.x + self.pos_name[0],  self.rect.y + self.pos_name[1]))
        view.window.blit(self.family, (self.rect.x + self.pos_family[0],  self.rect.y + self.pos_family[1]))
        view.window.blit(self.description, (self.rect.x + self.pos_description[0],  self.rect.y + self.pos_description[1]))
        if (self.card.infos.type != "action"):
            view.window.blit(self.power, (self.rect.x + self.pos_power[0],  self.rect.y + self.pos_power[1]))
            view.window.blit(self.movement, (self.rect.x + self.pos_movement[0],  self.rect.y + self.pos_movement[1]))
            view.window.blit(self.range, (self.rect.x + self.pos_range[0],  self.rect.y + self.pos_range[1]))
            view.window.blit(self.capacity_weight, (self.rect.x + self.pos_capacity_weight[0],  self.rect.y + self.pos_capacity_weight[1]))
        else:
            view.window.blit(self.action_point, (self.rect.x + self.pos_action_point[0],  self.rect.y + self.pos_action_point[1]))
            
        
        
        
        