'''
Created on 17 sept. 2018

@author: swann
'''
from src.modeles.Graphic_object import Graphic_object
from src.modeles.Creature import Creature
from src.modeles.Magic import Magic
from src.utility.loader import deck_loader

class Deck(Graphic_object):
    '''
    classdocs
    '''

    def __init__(self, controller, image_path, owner, filename="default"):
        '''
        Constructor
        '''
        Graphic_object.__init__(self, controller, image_path)
        
        self.name = "unnamed"
        self.cards = []
        self.owner = owner
        self.load(filename)
        
        
    def load(self, filename):
        self.cards = []
        load = deck_loader(filename)
        self.name = load[0]
        list_card_data = load[1]
        for data in list_card_data:
            if (data.infos.type == "creature"):
                self.cards.append(Creature(self.c, self.owner, data.infos, data.stats))
        
            elif (data.infos.type == "magic"):
                self.cards.append(Magic(self.c, self.owner, data.infos, data.stats))

            elif (data.infos.type == "trap"):
                self.cards.append(Magic(self.c, self.owner, data.infos, data.stats))
                
            elif (data.infos.type == "action"):
                self.cards.append(Magic(self.c, self.owner, data.infos, data.stats))
        
    def is_empty(self):
        return len(self.cards) == 0
        
    def shuffle(self):
        pass
    
    def draw(self, number_of_card=1):
        if self.is_empty():
            return []
        
        if (number_of_card > len(self.cards)):
            number_of_card = len(self.cards)
            
        temp = []
        for _ in range(0,number_of_card):
            temp.append(self.cards[-1])
            del self.cards[-1]
            
        return temp
    
    def add(self, card, shuffle=True):
        self.cards.append(card);
        if (shuffle):
            self.shuffle()
            
    def add_top(self, card):
        self.add(card, False)
    
    def search(self, card):
        pass
    
    def remove(self, card):
        if (self.cards.count(card)):
            return self.cards.pop(self.cards.index(card))
        
    def filter_by_type(self, Type):
        pass
    def filter_by_name(self, name):
        pass
    def filter_by_family(self, family):
        pass
    
    def destroy(self):
        pass
    
    def visible(self, state):
        super().visible(state)
        for card in self.cards:
            card.visible(state)
    
    def set_interactive(self, state):
        super().set_interactive(state)
        for card in self.cards:
            card.set_interactive(state)
    
    def mouse_pressed(self, event):
        if (self.rect.collidepoint(event.pos)):
            self.c.cards_drawn(self, self.draw())
    
    

