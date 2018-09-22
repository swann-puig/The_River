'''
Created on 16 sept. 2018

@author: Swann
'''

class Card_infos():
    '''
    Standard of basic informations about a card.
    '''
    def __init__(self, name, family, description, type, image_path):
        '''
        Constructor
        '''
        self.name = name
        self.family = family
        self.description = description
        self.type = type
        self.image_path = image_path
        self.color = 0x000000
        if (self.type == "creature"):
            self.color = 0x555555
        elif (self.type == "magic"):
            self.color = 0x0000ff
        elif (self.type == "trap"):
            self.color = 0xff0000
        elif (self.type == "action"):
            self.color = 0x00ff00
            
            