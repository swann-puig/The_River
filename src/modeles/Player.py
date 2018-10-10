'''
Created on 17 sept. 2018

@author: swann
'''
from src.modeles.Deck import Deck
from src.modeles.Hand import Hand
from src.view.Profile import Profile
from src.constant import PATH_IMAGE_DECK_NORMAL, PATH_IMAGE_DECK_ACTION

class Player():
    '''
    classdocs
    '''


    def __init__(self, controller, name, color, display_hand_card_Y):
        '''
        Constructor
        '''
        self.c = controller
        self.name = name
        self.profile = Profile(self, self.c.view.SCREEN_WIDTH)
        self.deck_normal = Deck(controller, PATH_IMAGE_DECK_NORMAL, self, "default")
        self.deck_action = Deck(controller, PATH_IMAGE_DECK_ACTION, self, "default")
        self.hand = Hand(controller, self.c.view.SCREEN_WIDTH, 0, display_hand_card_Y)
        self.castle = None
        self.life = 100
        self.action_point = 2
        self.color = color
    
    def init_position(self):
        self.deck_normal.set_position(self.profile.rect.x - self.deck_normal.rect.width - 20, 0)
        self.deck_action.set_position(self.profile.rect.x + self.profile.rect.width + 20, 0)
        
    def get_life(self):
        return self.life
    
    def get_action_point(self):
        return self.action_point
        
    def draw_normal_card(self, number=1):
        self.deck_normal.draw(number)
        
    def draw_deck_action(self, number=1):
        self.deck_action.draw(number)
        
    def use_magic_card(self, magic_card, target):
        pass
        
    def pose_creature(self, creature_card):
        pass
    
    def pose_trap(self, trap_card):
        pass
    
    def use_action_card(self, action_card):
        pass
    
    def take_damage(self, amount):
        self.life -= amount
        
    def add_life(self, amount):
        self.life += amount
        
    def set_visible(self, state):
        self.deck_normal.set_interactive(state)
        self.deck_action.set_interactive(state)
        self.hand.set_interactive(state)
        
        self.deck_normal.visible(state)
        self.deck_action.visible(state)
        self.hand.visible(state)
        
    def update(self):
        self.deck_normal.update()
        self.deck_action.update()
        self.hand.update()
        self.profile.update(self.c.view)
    
    
    
    
    
    
    
    
    
        