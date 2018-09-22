'''
Created on 16 sept. 2018

@author: Swann
'''

import pygame

class Graphic_object(pygame.sprite.Sprite):
    '''
    classdocs
    '''


    def __init__(self, controller, image_path, x=0, y=0):
        '''
        Constructor
        '''
        pygame.sprite.Sprite.__init__(self)
        self.c = controller
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect()
        self.past_rect = self.image.get_rect()
        self.rect.x, self.past_rect.x = x, x
        self.rect.y, self.past_rect.y = y, y
        self.is_visible = True
        self.interactive = False
        
        self.drag = False
        self.offset_x, self.offset_y = 0,0
        
    def set_position(self, x, y):
        self.rect.x, self.past_rect.x = x, x
        self.rect.y, self.past_rect.y = y, y
        
    def change_image(self, new_image):
        self.image = new_image
        self.update_size()
        
    def update_size(self):
        self.rect.width = self.image.get_width()
        self.rect.height = self.image.get_height()
        self.rect.center = (self.rect.width/2, self.rect.height/2)
    
        
    def visible(self, boolean):
        self.is_visible = boolean
        
    def set_interactive(self, activate):
        if (not self.interactive and activate):
            self.c.view.add_listen_mouse_event(self)
            self.interactive = activate
        elif (self.interactive and not activate):
            self.c.view.remove_listen_mouse_event(self)
            self.interactive = activate
        
    def mouse_pressed(self, event):
        if (self.rect.collidepoint(event.pos)):
            self.drag = True
            mouse_x, mouse_y = event.pos
            self.offset_x = self.rect.x - mouse_x
            self.offset_y = self.rect.y - mouse_y
            
    def mouse_released(self, event):
        self.drag = False
            
    def mouse_motion(self, event):
        if (self.drag):
            mouse_x, mouse_y = event.pos
            self.rect.x = mouse_x + self.offset_x
            self.rect.y = mouse_y + self.offset_y
            
    def move_to_old_position(self):
        self.rect.x = self.past_rect.x
        self.rect.y = self.past_rect.y
    
    def destroy(self):
        pass
    
    def update(self):
        if self.is_visible:
            self.c.display(self.image, (self.rect.x, self.rect.y))
        