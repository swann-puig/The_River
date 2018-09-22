'''
Created on 16 sept. 2018

@author: Swann
'''

import pygame
from pygame.locals import QUIT, MOUSEBUTTONDOWN, MOUSEBUTTONUP, MOUSEMOTION
from src.constant import FPS, PATH_BACKGROUND, PROFILE_HEIGHT, HAND_ZONE_HEIGHT
from screeninfo import get_monitors

class View(object):
    '''
    classdocs
    '''

    def __init__(self, controller):
        '''
        Constructor
        '''
        #------------------------------ INIT ------------------------------
        self.c = controller
        cut = str(get_monitors()[0]).split("(")[1].split("x")
        self.SCREEN_WIDTH  = int(cut[0])
        self.SCREEN_HEIGHT = int(cut[1].split("+")[0]) - 40
        #self.SCREEN_WIDTH = 800
        #self.SCREEN_HEIGHT = 600
        self.SCREEN_CENTER = (self.SCREEN_WIDTH/2, self.SCREEN_HEIGHT/2)
        print(str(self.SCREEN_WIDTH) + "x" + str(self.SCREEN_HEIGHT))
        pygame.init()
        self.window = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))#, pygame.FULLSCREEN)
        self.clock = pygame.time.Clock()

        self.object_listen = []

        #------------------------------ LOAD IMAGE ------------------------------
        #self.background = pygame.image.load(PATH_BACKGROUND).convert_alpha()
        
        #------------------------------ RESIZE ------------------------------
        self.percent_resize_board = 0 # will change when init resize function is call
        self.percent_resize_deck  = 0 # will change when init resize function is call
        self.percent_resize_hand  = 0 # will change when init resize function is call
        self.percent_resize_details  = 0 # will change when init resize function is call
        self.percent_resize_board_card = 0 # will change when init resize function is call
        self.details_size = 0
        
        
    def display_background(self):
        pass
    
    def display_details_card(self):
        pass
    
    def display_move_grid(self):
        pass
    
    def display(self, image, coord):
        self.window.blit(image, coord)
        
    def display_group(self, group):
        group.draw(self.window)
        
    def get_display_hand_card_Y(self):
        return self.SCREEN_HEIGHT - HAND_ZONE_HEIGHT
        
    def init_resize_element(self, board, deck, lambda_card, lambda_details):
        self.percent_resize_deck = (PROFILE_HEIGHT) / deck.image.get_height()
        self.percent_resize_hand = (HAND_ZONE_HEIGHT) / lambda_card.image_origine.get_height()
        self.percent_resize_board = (self.SCREEN_HEIGHT - PROFILE_HEIGHT - HAND_ZONE_HEIGHT) / board.rect.height
        self.percent_resize_details  = (self.SCREEN_HEIGHT - HAND_ZONE_HEIGHT) / lambda_details.image.get_height()
        self.percent_resize_board_card = (board.case_size * self.percent_resize_board) / lambda_card.image_origine.get_height()
        self.details_size = (lambda_details.image.get_width() * self.percent_resize_details, lambda_details.image.get_height() * self.percent_resize_details)
    
    def resize_game_board(self, board):
        new_image = pygame.transform.scale(board.image, (round(board.rect.width*self.percent_resize_board), round(board.rect.height*self.percent_resize_board)))
        board.change_image(new_image)
    
    def resize_deck(self, deck):
        new_image = pygame.transform.scale(deck.image, (round(deck.image.get_width()*self.percent_resize_deck), round(deck.image.get_height()*self.percent_resize_deck)))
        deck.change_image(new_image)
    
    def resize_card_hand(self, card):
        new_image = pygame.transform.scale(card.image_origine, (round(card.image_origine.get_width()*self.percent_resize_hand), round(card.image_origine.get_height()*self.percent_resize_hand)))
        card.change_image(new_image)
        
    def resize_card_board(self, card):
        new_image = pygame.transform.scale(card.image_origine, (round(card.image_origine.get_width()*self.percent_resize_board_card), round(card.image_origine.get_height()*self.percent_resize_board_card)))
        card.change_image(new_image)
        
    def add_card_to_hand(self):
        pass
    
    
    def quit(self):
        pygame.quit()
        
    def add_listen_mouse_event(self, object):
        self.object_listen.append(object)
        
    def remove_listen_mouse_event(self, object):
        self.object_listen.remove(object)
    
    def read_event(self):
        if not self.read_keyboard():
            return False
        
        for event in pygame.event.get():
            if event.type == QUIT:
                self.quit()
                return False
            elif event.type == MOUSEBUTTONDOWN:
                for o in self.object_listen:
                    o.mouse_pressed(event)
            elif event.type == MOUSEMOTION:
                for o in self.object_listen:
                    o.mouse_motion(event)
                self.c.display_check_details(event)
            elif event.type == MOUSEBUTTONUP:
                for o in self.object_listen:
                    o.mouse_released(event)
            
        return True
            
    def read_keyboard(self):
        list_key = pygame.key.get_pressed()
        if (list_key[pygame.K_ESCAPE]):
            self.quit()
            return False
        
        return True
        
    def update(self):
        pygame.draw.rect(self.window, pygame.Color("black"), self.window.get_rect()) # a remplacer par l'image de fond
        return self.read_event()
    
    def display_all(self):
        pygame.display.flip()
        self.clock.tick(FPS)
    
    