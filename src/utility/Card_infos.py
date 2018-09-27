'''
Created on 16 sept. 2018

@author: Swann
'''

class Card_infos():
    '''
    Standard of basic informations about a card.
    '''
    def __init__(self, name, family, description, type, effect, image_path):
        '''
        Constructor
        '''
        self.name = name
        self.family = family
        self.description = description
        self.type = type
        self.effect = effect
        self.image_path = image_path
        self.color = 0x000000ff
        if (self.type == "creature"):
            self.color = 0xffff0020
        elif (self.type == "Magic"):
            self.color = 0x0000ff20
        elif (self.type == "trap"):
            self.color = 0xff000020
        elif (self.type == "action"):
            self.color = 0x00ff0020
            
            