'''
Created on 16 sept. 2018

@author: Swann
'''
from src.modeles.Graphic_card import Graphic_card

class Card(Graphic_card):
    '''
    classdocs
    '''

    def __init__(self, controller, card_infos, owner, isTraversable):
        '''
        Constructor
        '''
        Graphic_card.__init__(self, controller, owner, card_infos.image_path)
        
        #------------------------------ INIT STATS------------------------------
        self.infos = card_infos
        self.isTraversable = isTraversable
        

        
        
        
        