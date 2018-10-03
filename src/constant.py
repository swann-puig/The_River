'''
Created on 16 sept. 2018

@author: Swann
'''

import os

#------------------------------ PATH ------------------------------
PATH_DECKS = os.path.join("files", "decks")
PATH_CARDS = os.path.join("files", "cards")
PATH_BACKGROUND = None
PATH_IMAGE_BOARD = os.path.join('files', 'boards', 'dev_board.png')
PATH_BOARD_INFO = os.path.join('files', 'boards', 'dev_board')
PATH_IMAGE_ICON = os.path.join("images", "icon.bmp")
PATH_IMAGE_DECK_NORMAL = os.path.join('images', 'deck_normal.png')
PATH_IMAGE_DECK_ACTION = os.path.join('images', 'deck_action.png')
PATH_IMAGE_DETAILS_C = os.path.join('images', 'creature_card.png')
PATH_IMAGE_DETAILS_M = os.path.join('images', 'magic_card.png')
PATH_IMAGE_DETAILS_T = os.path.join('images', 'trap_card.png')
PATH_IMAGE_DETAILS_A = os.path.join('images', 'action_card.png')
PATH_IMAGE_HAND = os.path.join("images", "hand.png")
PATH_CARDS_INVENTORY = os.path.join("files", "all_cards_inventory.txt")

#------------------------------ SIZE ------------------------------
PROFILE_HEIGHT = 200
HAND_ZONE_HEIGHT = 200
DETAILS_NAME_WIDTH = 260
DETAILS_POWER_WIDTH = 130
DETAILS_DESCRIPTION_WIDTH = 225
DETAILS_OTHER_WIDTH = 160

#------------------------------ DISPLAY ------------------------------
FPS = 40

#------------------------------ SETTINGS ------------------------------
MAX_CARD_IN_HAND = 8

#------------------------------ NAMES ------------------------------
CREATURE = "creature"
MAGIC = "magic"
TRAP = "trap"
ACTION = "action"
SINGLE = 0
NETWORK = 1
