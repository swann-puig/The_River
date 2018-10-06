'''
Created on 16 sept. 2018

@author: Swann
'''

from src.view.View import View
from src.view.Profile import Profile
from src.view.Card_details import Card_details
from src.modeles.Player import Player
from src.modeles.Board_game import Board_game
from src.constant import SINGLE, NETWORK

class Controller():
    '''
    classdocs
    '''

    def __init__(self, mode):
        '''
        Constructor
        '''
        self.mode = mode
        #------------------------------ CREATE ------------------------------
        self.view = View(self);
        self.player = Player(self, "Player1 nom", 0xff0000, self.view.get_display_hand_card_Y())
        self.board = Board_game(self)
        self.profile = Profile(self.player, self.view.SCREEN_WIDTH)
        if (mode == SINGLE):
            self.player2 = Player(self, "Player2 nom", 0xff0000, self.view.get_display_hand_card_Y())
        else:
            self.player2 = Player(self, "Player2 nom", 0xff0000, self.view.get_display_hand_card_Y())
        
        self.details = None
        self.selected_from_hand = (None, 0) # (card, layer)
        
        #------------------------------ RESIZE ------------------------------
        self.view.init_resize_element(self.board, self.player.deck_normal, self.player.deck_normal.cards[0], Card_details(self.player.deck_normal.cards[0], self.view.SCREEN_WIDTH, 0, 0))
        self.view.resize_game_board(self.board)
        self.view.resize_deck(self.player.deck_normal)
        self.view.resize_deck(self.player.deck_action)
        
        #------------------------------ SET POSITION ------------------------------
        self.board.set_position(self.view.SCREEN_CENTER[0]-self.board.rect.width/2, self.view.SCREEN_CENTER[1]-self.board.rect.height/2)
        self.player.deck_normal.set_position(self.profile.rect.x - self.player.deck_normal.rect.width - 20, 0)
        self.player.deck_action.set_position(self.profile.rect.x + self.profile.rect.width + 20, 0)
        
        if (mode == SINGLE):
            self.view.resize_deck(self.player2.deck_normal)
            self.view.resize_deck(self.player2.deck_action)
            self.player2.deck_normal.set_position(self.profile.rect.x - self.player.deck_normal.rect.width - 20, 0)
            self.player2.deck_action.set_position(self.profile.rect.x + self.profile.rect.width + 20, 0)
        
        
        #------------------------------ START ------------------------------
        self.round = None
        self.end_turn(self.player2)
        self.player.start()
        self.update()
    
        
    def update(self):
        while self.view.update():
            self.board.update()
            self.profile.update(self.view)
            self.player.update()
            self.player2.update()
            if (self.details != None): self.details.update(self.view)
            self.view.display_all()
            
    
    def display(self, image, coord):
        self.view.display(image, coord)
        
    def display_group(self, group):
        self.view.display_group(group)
        
    def draw_rects(self, rects, color, alpha=255):
        self.view.draw_rects(rects, color, alpha)
        
    def display_details(self, card, pos, remove=False):
        if (remove):
            self.details = None
        elif (self.is_display_priority(card, pos) or card.is_posed()):
            if (self.details == None):
                self.details = Card_details(card, self.view.SCREEN_WIDTH, pos[0], 0, self.view.percent_resize_details)
            elif (self.details.card != card):
                self.details = Card_details(card, self.view.SCREEN_WIDTH, pos[0], 0, self.view.percent_resize_details)
        
    def display_check_details(self, event):
        for sprite in self.player.hand.group:
            if (sprite.rect.collidepoint(event.pos)):
                return True
        self.details = None
        
    def is_display_priority(self, card, pos):
        cards_overlapping = self.player.hand.group.get_sprites_at(pos)
        if (cards_overlapping != []):
            return cards_overlapping[-1] == card
        return False
    
    def resize_card_hand(self, card):
        self.view.resize_card_hand(card)
    
    def resize_card_board(self, card):
        self.view.resize_card_board(card)
    
    def cards_drawn(self, deck, cards):
        for card in cards:
            if not self.player.hand.add_card(card):
                deck.add_top(card)
            # message trop de carte en main
    
    def get_main_player(self):
        return self.player
    
    def place_card_on_board(self, card, pos):
        if self.board.pose_card(card, pos):
            card.owner.hand.remove(card)
            card.set_posed(True)
            return True
        return False
    
    def card_released_in_wrong_place(self, card):
        if (card.location == self.board):
            card.set_location(None)
            self.view.resize_card_hand(card)
        card.move_to_old_position()
        self.deselect_from_hand()

    def move_card_posed(self, card, pos):
        if self.board.move_card(card, pos):
            self.deselect_from_board()
            self.select_from_board(card)
        else:
            card.move_to_old_position()
            
        
    def is_in_board(self, pos):
        return self.board.rect.collidepoint(pos)
    
    def select_from_hand(self, card):
        if (self.selected_from_hand[0] != None):
            if (not self.selected_from_hand[0].is_posed()):
                self.player.hand.group.change_layer(self.selected_from_hand[0], self.selected_from_hand[1])
        self.selected_from_hand = (card, self.player.hand.group.get_layer_of_sprite(card))
        self.player.hand.group.move_to_front(card)
        
    def deselect_from_hand(self):
        if (self.selected_from_hand[0] != None):
            if (not self.selected_from_hand[0].is_posed()):
                self.player.hand.group.change_layer(self.selected_from_hand[0], self.selected_from_hand[1])
        self.selected_from_hand = (None, 0)
        
    def select_from_board(self, card):
        self.display_move_zone(card)
        
    def deselect_from_board(self):
        self.remove_move_zone()
        
    def display_move_zone(self, card):
        self.board.display_move_zone(card)
        
    def remove_move_zone(self):
        self.board.remove_move_zone()
        
    def end_turn(self, player):
        if (self.round == self.player):
            self.round = self.player2
        else:
            self.round = self.player
        
        print("end", player.name)
        print("start", self.round.name)
        player.set_visible(False)
        self.round.set_visible(True)
        
        