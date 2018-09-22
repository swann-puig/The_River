'''
Created on 17 sept. 2018

@author: Swann
'''

from src.utility.Card_infos import Card_infos
from src.utility.Creature_stats import Creature_stats
from src.constant import PATH_DECKS, PATH_CARDS
import os

class Info():
    '''
    classdocs
    '''
    def __init__(self, infos, stats):
        self.infos = infos
        self.stats = stats
        
def normalize(string):
    string.replace("\n", "")
    string.replace("\r", "")
    return str

def card_loader(card_name):
    file = open(os.path.join(PATH_CARDS, card_name, "infos"), "r")
    name = file.readline().split(": ")[1][:-1]
    family = file.readline().split(": ")[1][:-1]
    description = file.readline().split(": ")[1][:-1]
    Type = file.readline().split(": ")[1]
    image_path = os.path.join(PATH_CARDS, card_name,"image.png")
    file.close()
    
    i = Card_infos(name, family, description, Type, image_path)
    s = None
    if (Type == "creature"):
        file = open(os.path.join(PATH_CARDS, card_name, "stats"), "r")
        power = int(file.readline().split(": ")[1])
        move = int(file.readline().split(": ")[1])
        Range = int(file.readline().split(": ")[1])
        capacity = int(file.readline().split(": ")[1])
        file.close()
        
        s = Creature_stats(power, move, Range, capacity)
        
    else:
        s = Creature_stats(1000, 2, 2, 1)

    return Info(i, s)

'''
@deck_input, an object Deck type
@return (name, list_card_info) a list of card infos written in the deck filename.
'''
def deck_loader(filename="default"):
    file = open(os.path.join(PATH_DECKS, filename), "r")
    name = file.readline().split(": ")[1][:-1]
    list_name = file.readline().split(": ")[1].split(", ")
    file.close()
    list_card_info = []
    for card_name in list_name:
        list_card_info.append(card_loader(card_name))
    
    return (name, list_card_info)

def board_loader(filename):
    file = open(filename, "r")
    boxe_size = int(file.readline().split(": ")[1])
    non_box = file.readline().split(": ")[1][:-1]
    area1 = file.readline().split(": ")[1][:-1]
    area2 = file.readline().split(": ")[1]
    file.close()
    out = []
    for coords in [non_box, area1, area2]:
    
        if (coords == "[]"):
            out.append([])
        else:
            boxes = []
            i = 2 # first number emplacement 
            stop = False
            while (not stop):
                if coords[i+1] == ',':
                    raw = int(coords[i])
                    i += 2
                else:
                    raw = int(coords[i:i+2])
                    i += 3
                
                if coords[i+1] == ')':
                    column = int(coords[i])
                    if coords[i+2] == ']': stop = True
                    i += 5
                else:
                    column = int(coords[i:i+2])
                    if coords[i+3] == ']': stop = True
                    i += 6
                boxes.append((raw, column))
            out.append(boxes)
    
    non_box, area1, area2 = out[0], out[1], out[2]
    return boxe_size, non_box, area1, area2
    