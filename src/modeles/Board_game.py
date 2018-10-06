'''
Created on 18 sept. 2018

@author: Swann
'''
from src.modeles.Graphic_object import Graphic_object
from src.constant import PATH_IMAGE_BOARD, PATH_BOARD_INFO, CREATURE, MAGIC, TRAP
from src.utility.loader import board_loader
import pygame

class Board_game(Graphic_object):
    '''
    classdocs
    '''
    def __init__(self, controller, x=0, y=0):
        '''
        Constructor
        '''
        Graphic_object.__init__(self, controller, PATH_IMAGE_BOARD, x, y)
        
        self.case_size, self.non_boxe, self.area1, self.area2 = board_loader(PATH_BOARD_INFO)
        
        self.nb_column = round(self.rect.width / self.case_size)
        self.nb_raw = round(self.rect.height / self.case_size)
        self.board = []
        self.box_taken = []
        self.column = []
        self.raw = []
        
        self.update_size()
        
        for i in range(0, self.nb_column):
            for j in range(0, self.nb_raw):
                self.board.append((j, i))
        
        self.group = pygame.sprite.LayeredUpdates()
        self.move_zone = []#pygame.sprite.Group()
        
    def change_image(self, new_image):
        old_height = self.rect.height
        percent = new_image.get_height() / old_height
        self.case_size *= percent
        super().change_image(new_image)
        
    def get_case_size(self):
        return self.case_size
    
    def set_position(self, x, y):
        super().set_position(x, y)
        self.update_raw_and_col()
            
    def update_size(self):
        super().update_size()
        self.update_raw_and_col()

    def update_raw_and_col(self):
        self.raw =    [round(self.rect.y + i * self.case_size) for i in range(0 , self.nb_raw+1)]
        self.column = [round(self.rect.x + i * self.case_size) for i in range(0 , self.nb_column+1)]
        
    def display_move_zone(self, card):
        w = h = card.get_movement()
        pos_card = self.get_index(card.past_rect.x, card.past_rect.y)
        for col in range(pos_card[1]-w, pos_card[1]+w+1):
            for raw in range(pos_card[0]-h, pos_card[0]+h+1):
                if (self.can_move_card(card, (raw, col), pixel=False)):
                    self.move_zone.append(pygame.Rect(self.column[col], self.raw[raw] , self.case_size, self.case_size))
        
    def remove_move_zone(self):
        self.move_zone.clear()
        
    def mouse_motion(self, event):
        pass
            
    def mouse_pressed(self, event):
        pass
            
    def mouse_released(self, event):
        pass
    
    def get_index(self, x, y):
        for i in range(0, self.nb_raw):
            for j in range(0, self.nb_column):
                if (self.raw[i] <= y and y < self.raw[i+1]):
                    if (self.column[j] <= x and x < self.column[j+1]):
                        return (i,j)
    
    def get_creature_for_equip(self, equip_card, index_output=False):
        list = []
        for creature in self.group:
            if creature.owner == equip_card.owner and creature.can_equip(equip_card):
                if (index_output):
                    list.append(self.get_index(creature.rect.x, creature.rect.y))
                else:
                    list.append(creature)
                
        return list
    
    def can_pose_card(self, card, pos):
        index = self.get_index(pos[0], pos[1])
        if (index == None):
            return False
        if (card.infos.type == CREATURE):
                return ((index in (self.area1 if card.owner == self.c.player else self.area2))
                        and (not index in self.box_taken)
                        and (not index in self.non_boxe)
                        )

        if (card.infos.type == MAGIC):
            return (index in self.get_creature_for_equip(card, index_output=True))
    
    def pose_card(self, card, pos):
        if self.can_pose_card(card, pos):
            if (card.infos.type == CREATURE):
                index = self.get_index(pos[0], pos[1])
                card.set_position(self.column[index[1]], self.raw[index[0]])
                self.add_card(card)
                self.box_taken.append(index)
                return True
            
            if (card.infos.type == MAGIC or card.infos.type == TRAP):
                index = self.get_index(pos[0], pos[1])
                list_creature = self.get_creature_for_equip(card)
                list_index = self.get_creature_for_equip(card, index_output=True)
                list_creature[list_index.index(index)].equip(card)
                return True
        return False
        
    def can_move_card(self, card, pos, pixel=True):
        old_index = self.get_index(card.past_rect.x, card.past_rect.y)
        if (pixel):
            index = self.get_index(pos[0], pos[1])
        else:
            index = pos
        if (index == None):
            return False
        return ((not index in self.box_taken)
                and (not index in self.non_boxe) 
                and (abs(index[0] - old_index[0]) + abs(index[1] - old_index[1]) <= card.get_movement())
                and index in self.board)
    
    def move_card(self, card, pos):
        if self.can_move_card(card, pos):
            old_index = self.get_index(card.past_rect.x, card.past_rect.y)
            index = self.get_index(pos[0], pos[1])
            card.set_position(self.column[index[1]], self.raw[index[0]])
            if old_index in self.box_taken: self.box_taken.remove(old_index)
            self.box_taken.append(index)
            return True
        return False
    
    def add_card(self, card):
        self.group.add(card)
        self.group.move_to_front(card)
        card.set_interactive(True)
        return True
        
    def remove(self, card):
        self.group.remove(card)
        
    def update(self):
        super().update()
        self.c.draw_rects(self.move_zone, pygame.Color(0xf2f20000), alpha=64)
        self.c.display_group(self.group)
    
        