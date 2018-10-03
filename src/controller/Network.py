'''
Created on 2 oct. 2018

@author: swann
'''
from src.controller.Controller import Controller
from src.constant import NETWORK

class Network(Controller):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        Controller.__init__(self, NETWORK)
        
        
        