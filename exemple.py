import random
import math
import pygame
import time

from pygame.locals import *

pygame.init()
fenetre = pygame.display.set_mode((1600, 950))
myfont = pygame.font.SysFont("monospace", 20 , 1)

screen_largeur = 1600
screen_hauteur = 950
laserOn = 0
chance = 0
quitterBoucle = 0
toucher = 100

pygame.mixer.pre_init()
pygame.mixer.set_num_channels(3)
pygame.mixer.init()


class Asteroid(pygame.sprite.Sprite):
    
    def __init__(self,up,type1,grandeur):
        
        # Call the parent class (Sprite) constructor 
        super().__init__()
        
        #self.image = pygame.image.load("Asteroide type 0 etat 0.png").convert_alpha()
        
        self.images = []
        liste = []
        liste.append(pygame.image.load("Asteroide type 0 etat 0.png").convert_alpha())
        liste.append(pygame.image.load("Asteroide type 0 etat 1.png").convert_alpha())
        self.images.append(liste)
        liste = []
        liste.append(pygame.image.load("Asteroide type 1 etat 0.png").convert_alpha())
        liste.append(pygame.image.load("Asteroide type 1 etat 1.png").convert_alpha())
        self.images.append(liste)
        liste = []
        liste.append(pygame.image.load("Asteroide type 2 etat 0.png").convert_alpha())
        liste.append(pygame.image.load("Asteroide type 2 etat 1.png").convert_alpha())
        self.images.append(liste)
        
        self.imagesExplosion = []
        im = pygame.image.load("explosion.png").convert_alpha()
        for j in range(0,4):
            for i in range(0,4):
                im1 = im.subsurface((j*im.get_width()/4 , i*im.get_height()/4, im.get_width()/4 , im.get_height()/4))
                self.imagesExplosion.append(im1)
        
        self.indiceExplosion = 0
        self.Explosion = 0
        self.timer = time.time()
        self.timerExplosion = time.time()
        self.imateriel = 0
        self.frequenceExplosion = 0.05
        
        self.type = type1
        self.grandeur = grandeur
        self.vieMax = [[20,40,80],[25,50,100],[30,60,120]]
        self.vie = self.vieMax[self.type][self.grandeur]
        self.degats = [[4,9,18],[5,10,20],[6,12,24]]
        self.score = [[2,4,8],[3,5,10],[3,6,12]]
        
        
        
        ima = self.images[self.type][round((self.vieMax[self.type][self.grandeur] - self.vie) / self.vieMax[self.type][self.grandeur])]
        self.image = pygame.transform.scale(ima, (round(ima.get_width() / math.pow(1.4142, 2-self.grandeur)), round(ima.get_height()/math.pow(1.4142, 2-self.grandeur))))
        
        # Fetch the rectangle object that has the dimensions of the image
        # image.
        # Update the position of this object by setting the values
        # of rect.x and rect.y
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(screen_largeur)
        self.rect.y = -random.randrange(screen_hauteur)
        
        self.dx = random.randrange(-100, 100)/100
        self.dy = random.randrange(200, 400)/100
        self.x = self.rect.x
        self.y = self.rect.y
        self.xCentre = self.image.get_width() / 2
        self.yCentre = self.image.get_height() / 2
        self.angle = 0
        
        self.up = up
        
        
    def update(self):
        
        self.x += self.dx
        self.y += self.dy
        self.rect.x = round(self.x)
        self.rect.y = round(self.y)
        
        if self.rect.y >= screen_hauteur :
            self.vie = self.vieMax[self.type][self.grandeur]
            ima = self.images[self.type][round((self.vieMax[self.type][self.grandeur] - self.vie) / self.vieMax[self.type][self.grandeur])]
            self.image = pygame.transform.scale(ima, (round(ima.get_width() / math.pow(1.4142, 2-self.grandeur)), round(ima.get_height()/math.pow(1.4142, 2-self.grandeur))))
            
            self.rect = self.image.get_rect()
            self.rect.x = random.randrange(screen_largeur-100)
            self.rect.y = random.randint(-screen_hauteur,-100)
            self.dx = random.randrange(-200, 200)/100
            self.dy = random.randrange(200, 400)/100
            self.x = self.rect.x
            self.y = self.rect.y
        
            
        # Call the parent class (Sprite) constructor
        super().update()
        
        
        
        if self.Explosion == 1 :
            self.animationExplosion()
        else :
            ima = self.images[self.type][round((self.vieMax[self.type][self.grandeur] - self.vie) / self.vieMax[self.type][self.grandeur])]
            self.image = pygame.transform.scale(ima, (round(ima.get_width() / math.pow(1.4142, 2-self.grandeur)), round(ima.get_height()/math.pow(1.4142, 2-self.grandeur))))
            
            self.imageRotation = self.image
            self.angle += 2
            self.image = pygame.transform.rotate(self.imageRotation, self.angle)
            
        fenetre.blit(self.image, (round(self.rect.x + self.xCentre - self.image.get_width()/2),round(self.rect.y + self.yCentre - self.image.get_height()/2)))
        
            
    def explose(self):
        
        p = random.randint(1,7)
        if p == 1 :
            bonus1 = Bonus(self.up)
            self.up.bonus.add(bonus1)
        
        self.up.joueur.score += self.score[self.type][self.grandeur]
        self.debutAnimationExplosion()
        
        
    def recoitDegats(self,degats):
        if self.imateriel == 0 :
            self.vie -= degats
            if self.vie <= 0 :
                self.explose()
        
    def debutAnimationExplosion(self):
        self.imateriel = 1
        self.timerExplosion = time.time()
        self.indiceExplosion = 0
        self.Explosion = 1
    
    def animationExplosion(self):
        self.timer = time.time()
        self.indiceExplosion = round((self.timer - self.timerExplosion) / self.frequenceExplosion )
        if self.indiceExplosion <= 15 and self.indiceExplosion >= 0:
            ima = self.imagesExplosion[self.indiceExplosion]
            self.image = pygame.transform.scale(ima, (round(ima.get_width() / math.pow(1.4142, 2-self.grandeur)), round(ima.get_height()/math.pow(1.4142, 2-self.grandeur))))
        else :
            self.finAnimationExplosion()
        
    def finAnimationExplosion(self):
        self.imateriel = 0
        self.rect.x = random.randrange(screen_largeur-100)
        self.rect.y = random.randint(-screen_hauteur,-100)
        self.vie = self.vieMax[self.type][self.grandeur]
        self.Explosion = 0
        self.indiceExplosion = 0
        self.dx = random.randrange(-200, 200)/100
        self.dy = random.randrange(200, 400)/100
        self.x = self.rect.x
        self.y = self.rect.y
        

class Ennemis(pygame.sprite.Sprite):
    
    def __init__(self,up,type1,grandeur):
        
        # Call the parent class (Sprite) constructor
        super().__init__()
        
        self.images = []
        liste = []
        liste.append(pygame.image.load("ennemi type 1 test2.png").convert_alpha())
        #liste.append(pygame.image.load("ennemi type 1.png").convert_alpha())
        self.images.append(liste)
        liste = []
        liste.append(pygame.image.load("ennemi type 2 test.png").convert_alpha())
        #liste.append(pygame.image.load("ennemi type 1.png").convert_alpha())
        self.images.append(liste)
        liste = []
        liste.append(pygame.image.load("ennemi type 3.png").convert_alpha())
        #liste.append(pygame.image.load("ennemi type 1.png").convert_alpha())
        self.images.append(liste)
        
        self.imagesExplosion = []
        im = pygame.image.load("explosion.png").convert_alpha()
        for j in range(0,4):
            for i in range(0,4):
                im1 = im.subsurface((j*im.get_width()/4 , i*im.get_height()/4, im.get_width()/4 , im.get_height()/4))
                self.imagesExplosion.append(im1)
        
        self.indiceExplosion = 0
        self.Explosion = 0
        self.timer = time.time()
        self.timerExplosion = time.time()
        self.imateriel = 0
        self.frequenceExplosion = 0.05
        self.laserNiveau = 0
        
        self.type = type1
        self.grandeur = grandeur
        self.vieMax = [[40,80,160],[50,100,200],[60,120,240]]
        self.vie = self.vieMax[self.type][self.grandeur]
        self.degats = [[5,10,20],[6,12,24],[7,15,28]]
        self.score = [[7,20,60],[9,27,80],[11,33,100]]
        
        ima = self.images[self.type][0]
        self.image = pygame.transform.scale(ima, (round(ima.get_width() / math.pow(1.4142, 2-self.grandeur)), round(ima.get_height()/math.pow(1.4142, 2-self.grandeur))))
        
        self.laserPositionX = [round(self.image.get_width() / 2), 0 ,round(self.image.get_width() / 2) , self.image.get_width()]
        self.laserPositionY = [self.image.get_height(), (self.image.get_height() / 2) , 0 , (self.image.get_height() / 2)]
        
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(screen_largeur)
        self.rect.y = -random.randrange(screen_hauteur)
        self.dx = 4
        self.dy = 3
        self.x = self.rect.x
        self.y = self.rect.y
        self.timerTirer = time.time()
        self.respawnTime = 0
        
        self.directionX = random.randint(-1,1)
        self.directionY = random.randint(-1,1)
        self.deplacement = random.randint(1,20)
        self.conteurDeplacement = 0
        self.xCentre = self.image.get_width() / 2
        self.yCentre = self.image.get_height() / 2
        self.angle = 0
        if self.type == 0:
            self.imageRotation = self.image
        
        self.up = up
        
    def update(self):
        
        self.intelligence()
        
        if self.rect.y >= screen_hauteur :
            self.vie = self.vieMax[self.type][self.grandeur]
            ima = self.images[self.type][0]
            self.image = pygame.transform.scale(ima, (round(ima.get_width() / math.pow(1.4142, 2-self.grandeur)), round(ima.get_height()/math.pow(1.4142, 2-self.grandeur))))
            
            self.rect = self.image.get_rect()
            self.rect.x = random.randrange(screen_largeur-100)
            self.rect.y = random.randint(-screen_hauteur,-100)
            self.dx = 0
            self.dy = 0
            self.x = self.rect.x
            self.y = self.rect.y
        
            
        # Call the parent class (Sprite) constructor
        super().update()
        
        if self.Explosion == 1 :
            self.animationExplosion()
            
        fenetre.blit(self.image, (round(self.rect.x + self.xCentre - self.image.get_width()/2),round(self.rect.y + self.yCentre - self.image.get_height()/2)))
            
        
            
    def explose(self):
        
        p = random.randint(1,5)
        if p == 1 :
            bonus1 = Bonus(self.up)
            self.up.bonus.add(bonus1)
        
        self.up.joueur.score += self.score[self.type][self.grandeur]
        self.debutAnimationExplosion()
        
        
    def recoitDegats(self,degats):
        if self.imateriel == 0 :
            self.vie -= degats
            if self.vie <= 0 :
                self.explose()
        
    def debutAnimationExplosion(self):
        self.imateriel = 1
        self.timerExplosion = time.time()
        self.indiceExplosion = 0
        self.Explosion = 1
        self.respawnTime = time.time() + 10
    
    def animationExplosion(self):
        self.timer = time.time()
        self.indiceExplosion = round((self.timer - self.timerExplosion) / self.frequenceExplosion )
        if self.indiceExplosion <= 15 and self.indiceExplosion >= 0:
            ima = self.imagesExplosion[self.indiceExplosion]
            self.image = pygame.transform.scale(ima, (round(ima.get_width() / math.pow(1.4142, 2-self.grandeur)), round(ima.get_height()/math.pow(1.4142, 2-self.grandeur))))
        else :
            self.finAnimationExplosion()
        
    def finAnimationExplosion(self):
        self.imateriel = 0
        ima = self.images[self.type][0]
        self.image = pygame.transform.scale(ima, (round(ima.get_width() / math.pow(1.4142, 2-self.grandeur)), round(ima.get_height()/math.pow(1.4142, 2-self.grandeur))))
        self.rect.x = random.randrange(screen_largeur-100)
        self.rect.y = random.randint(-screen_hauteur,-100)
        self.vie = self.vieMax[self.type][self.grandeur]
        self.Explosion = 0
        self.indiceExplosion = 0
        self.x = self.rect.x
        self.y = self.rect.y
        
        
    def intelligence(self):
         
        self.dy = 0
        
        if self.respawnTime < time.time():
        
            if self.type == 0:
                self.dx = 0
                if self.x >= 0 and (self.x + (round(self.up.vaisseau.image.get_width() / math.pow(1.4142, 2-self.grandeur)))) <= 1600:
                    if self.conteurDeplacement < self.deplacement:
                        
                        self.dx = 3 * self.directionX
                        self.dy = 3 * self.directionY
                        self.conteurDeplacement += 1
                    else:
                        bouger = random.randint(1,3)
                        if bouger == 1:
                            self.directionX = random.randint(-1,1)
                            self.directionY = random.randint(-1,1)
                        else:
                            self.directionX = 0
                            self.directionY = 0
                        self.deplacement = random.randint(20,100)
                        self.dx = 3 * self.directionX
                        self.dy = 3 * self.directionY
                        self.conteurDeplacement = 0
                
                else:
                    self.dx = -5 * self.directionX
                  
                self.angle += 0.8
                self.image = pygame.transform.rotate(self.imageRotation, self.angle)
            
                
            if self.type == 1:
                if self.dx == 0:
                    self.dx = 1
                if self.x <= 0:
                    self.dx = 1
                if self.x + self.image.get_width() >= 1600:
                    self.dx = -1
                
            
            if self.type == 2:
                self.dx = 0
                test = random.randint(0,100)
                if round((self.x + (self.x + (round(self.up.vaisseau.image.get_width() / math.pow(1.4142, 2-self.grandeur))))) / 2) < self.up.vaisseau.rect.x + test :
                    self.dx = 3
                if round((self.x + (self.x + (round(self.up.vaisseau.image.get_width() / math.pow(1.4142, 2-self.grandeur))))) / 2) > self.up.vaisseau.rect.x + test :
                    self.dx = -3
                if self.y >= 100 and self.y <= 600 and self.y + 100 < self.up.vaisseau.rect.y:
                    self.dy = random.randint(0,4)
                    if self.dy == 0:
                        self.dy = 2
                    else:
                        self.dy = 0
                
                
            if self.y < 100 :
                self.dy = 3
            
            if self.y > 600 or self.y + 100 > self.up.vaisseau.rect.y:
                self.dy = -3
            
            
            self.x += self.dx
            self.y += self.dy
            self.rect.x = round(self.x)
            self.rect.y = round(self.y)
            
            if self.y > 0 and self.Explosion == 0:
                self.tirer()

        
    def tirer(self):
    
        if (time.time() - self.timerTirer) >= 2 and self.type == 0:
                
            self.timerTirer = time.time()
            for i in range(0,4):
                laserEnnemi = LaserEnnemi(self.up, self.type, self.grandeur, self.angle + 90*i)
                laserEnnemi.rect.x = round(self.rect.x + self.xCentre /2)
                laserEnnemi.rect.y = round(self.rect.y + self.yCentre /2)
                self.up.lasersEnnemis.add(laserEnnemi)
                
        if (time.time() - self.timerTirer) >= 6 and self.type == 1:
                
            self.timerTirer = time.time()
            for i in range(0,1):
                projectileSensible = ProjectileSensible(self.up, self.type, self.grandeur, self.angle)
                projectileSensible.rect.x = self.rect.x# + self.laserPositionX[i]
                projectileSensible.rect.y = self.rect.y + self.laserPositionY[i]
                self.up.projectilesSensibles.add(projectileSensible)
                
        if (time.time() - self.timerTirer) >= 2 and self.type == 2:
                
            self.timerTirer = time.time()
            for i in range(0,1):
                laserEnnemi = LaserEnnemi(self.up, self.type, self.grandeur, self.angle)
                laserEnnemi.rect.x = self.rect.x + self.laserPositionX[i]
                laserEnnemi.rect.y = self.rect.y + self.laserPositionY[i]
                self.up.lasersEnnemis.add(laserEnnemi)
        
        
     
     
     
class Vaisseau(pygame.sprite.Sprite):
    # Repr�sente tous les vaisseaux
    
    def __init__(self, up):
        
        # Call the parent class (Sprite) constructor
        super().__init__()
        
        
        self.images = []
        self.images.append(pygame.image.load("vaisseau1.png").convert_alpha())
        self.images.append(pygame.image.load("vaisseau2.png").convert_alpha())
        self.images.append(pygame.image.load("vaisseau3.png").convert_alpha())
        
        self.niveau = 0
        self.image = self.images[self.niveau]
        
        # Fetch the rectangle object that has the dimensions of the image
        # image.
        # Update the position of this object by setting the values
        # of rect.x and rect.y
        self.rect = self.image.get_rect()
        
        self.vie = 50
        self.vieMax = [75,150,250]
        self.laserNiveau = 0
        self.laserPositionX = [[53, 53, 53, 53], [15, 15, 90, 90], [10, 15, 90, 95]]
        self.laserPositionY = -80
        self.clignot = 0
        self.timerTirer = time.time()
        self.timerClignoter = time.time()
        self.rect.x = math.floor(screen_largeur / 2)
        self.rect.y = screen_hauteur -150
        self.visible = 1
        
        self.up = up

        
    
    def update(self):
        # Call the parent class (Sprite) constructor
        
        if self.clignot == 1 :
            timer = time.time() - self.timerClignoter
            timer2 = math.fmod(timer, 0.3)
            
            if timer2 >= 0 and timer2 <= 0.05 :
                self.visible = 1
            else :
                self.visible = 0
            
            if timer > 1 :
                self.clignot = 0
                self.visible = 1
        
        if self.visible == 1 :
            super().update()
            fenetre.blit(self.images[self.niveau], (self.rect.x,self.rect.y))
                    
        
    def tirer(self):
        
        if (time.time() - self.timerTirer) >= 0.25 :
                
            self.timerTirer = time.time()
            for i in range(0,4):
                laser = Laser(self.up)
                laser.rect.x = self.up.vaisseau.rect.x + self.laserPositionX[self.niveau][i]
                laser.rect.y = self.up.vaisseau.rect.y + self.laserPositionY
                laser.niveau = self.laserNiveau
                laser.visible = 1
                self.up.lasers.add(laser)
        
        
        
    def recoitDegats(self, degats):
        if self.clignot == 0:
            self.clignot = 1
            self.visible = 0
            self.timerClignoter = time.time()
            self.vie -= degats
            if self.vie <= 0 :
                self.vie = self.vieMax[self.niveau]
                self.up.joueur.vie -= 1
                self.up.creationNiveau()
                
                
        
    def changeNiveau(self,niveau):
        self.niveau = niveau
        self.vie = self.vieMax[self.niveau]
    
    
    
class Laser(pygame.sprite.Sprite):
    #...
    
    def __init__(self, up):
        # Call the parent class (Sprite) constructor
        super().__init__()
        
        self.images = []
        self.images.append(pygame.image.load("lazer niv1.jpg").convert_alpha())
        self.images.append(pygame.image.load("lazer niv2.jpg").convert_alpha())
        self.images.append(pygame.image.load("lazer niv3.jpg").convert_alpha())
        self.images.append(pygame.image.load("lazer niv4.jpg").convert_alpha())
        
        self.niveau = 0
        self.image = self.images[self.niveau]
         
        self.rect = self.image.get_rect()
        self.rect.x = 1
        self.rect.y = 1
        self.degats = [3, 5, 7, 9]
        
        self.up = up

        
    def update(self):
        # Call the parent class (Sprite) constructor
        super().update()
        
        self.rect.y -= 30
        if self.rect.y <= -30 :
            self.kill()
        else :
            fenetre.blit(self.images[self.niveau], (self.rect.x,self.rect.y))
            
    
    def toucher(self,asteroid):
        asteroid.recoitDegats(self.degats[self.niveau])
        

class LaserEnnemi(pygame.sprite.Sprite):

    def __init__(self, up, type1, grandeur, angle):
        # Call the parent class (Sprite) constructor
        super().__init__()
        
        self.images = []
        self.images.append(pygame.image.load("projectile bleu.png").convert_alpha())
        self.images.append(pygame.image.load("lazer niv1.jpg").convert_alpha())
        self.images.append(pygame.image.load("lazer niv4.jpg").convert_alpha())
        
        self.type = type1
        self.grandeur = grandeur
        self.angle = angle
        self.image = self.images[self.type]
        if self.type != 2:
            self.image = pygame.transform.scale(self.image, (round(self.image.get_width() / math.pow(1.4142, 2-self.grandeur)), round(self.image.get_height()/math.pow(1.4142, 2-self.grandeur))))
        
        self.image = pygame.transform.rotate(self.image, self.angle)
        self.rect = self.image.get_rect()
        self.rect.x = 1
        self.rect.y = 1
        self.degatsEnnemis = [[5,10,20],[1,2,3],[6,11,22]]
        #self.degats = self.degatsEnnemis[self.type][self.grandeur]
        self.frequenceExplosion = 0.05
        
        self.up = up

        
    def update(self):
        # Call the parent class (Sprite) constructor
        super().update()
        
        if self.type == 0:
            self.rect.x += round(5 * math.cos(self.angle*math.pi / 180))
            self.rect.y += round(5 * math.sin(self.angle*math.pi / 180))
            if self.rect.y >= 980 or self.rect.x >= 1630 or self.rect.y <= -30 or self.rect.x <= -30:
                self.kill()
            else :
                fenetre.blit(self.image, (self.rect.x,self.rect.y))
            
        if self.type == 2:
            self.rect.y += 30
            if self.rect.y >= 980 :
                self.kill()
            else :
                fenetre.blit(self.image, (self.rect.x,self.rect.y))

class ProjectileSensible(pygame.sprite.Sprite):
    
    def __init__(self,up, type1, grandeur, angle):
        
        super().__init__()
        
        self.images = []
        liste = []
        self.images.append(liste)
        liste = []
        liste.append(pygame.image.load("projectile.png").convert_alpha())
        liste.append(pygame.image.load("projectile enrgie explosion.png").convert_alpha())
        self.images.append(liste)
        
        self.type = type1
        self.grandeur = grandeur
        self.angle = angle
        self.image = self.images[self.type][0]
        self.image = pygame.transform.scale(self.image, (round(self.image.get_width() / math.pow(1.4142, 2-self.grandeur)), round(self.image.get_height()/math.pow(1.4142, 2-self.grandeur))))
        
        self.image = pygame.transform.rotate(self.image, self.angle)
        self.rect = self.image.get_rect()
        self.rect.x = 1
        self.rect.y = 1
        self.timerExplosion = 0
        self.Explosion = 0
        
        self.degatsEnnemis = [[] , [15, 25, 40] , []]
        
        self.up = up
        
    def update(self):
            
        if self.Explosion == 0:
            if self.type == 1:
                self.rect.y += 1
                if self.rect.y >= 980 :
                    self.kill()
                else :
                    fenetre.blit(self.image, (self.rect.x,self.rect.y))
        else:
            self.animationExplosion()
        
    def explose(self):
        
        self.debutAnimationExplosion()
        
    def debutAnimationExplosion(self):
        self.timerExplosion = time.time() + 0.8
        self.Explosion = 1
        self.animationExplosion()
    
    def animationExplosion(self):
        if self.timerExplosion > time.time():
            self.image = self.images[self.type][1]
            self.image = pygame.transform.scale(self.image, (round(self.image.get_width() / math.pow(1.4142, 2-self.grandeur)), round(self.image.get_height()/math.pow(1.4142, 2-self.grandeur))))
            fenetre.blit(self.image, (self.rect.x,self.rect.y))
        else:
            self.finAnimationExplosion()
    def finAnimationExplosion(self):
        self.kill()
        
class Joueur():
    
    def __init__(self,up):
        
        self.vie = 3
        self.score = 0
        self.niveau = 1
        self.proportion = 1
        self.imageBarContour = pygame.image.load("barVieContour.png").convert_alpha()
        self.imageBarInterieur = pygame.image.load("barVieInterieur.png").convert_alpha()
        self.imageVie = pygame.image.load("vie.png").convert_alpha()
        
        self.up = up
                
    def afficher(self):
        score_display = myfont.render("score: " + str(self.score), 1, (255,255,255))
        fenetre.blit(score_display, (1440, 20))

        # Collage vie
        boucle = 0
        while boucle < self.vie:
            fenetre.blit(self.imageVie, (25*boucle,0))
            boucle += 1
    
        niveauDisplay = myfont.render("Niveau: " + str(self.niveau), 1, (255,255,255))
        fenetre.blit(niveauDisplay, (1150, 20))
        
        self.proportion = self.up.vaisseau.vie / self.up.vaisseau.vieMax[self.up.vaisseau.niveau]
        imageBar1 = self.imageBarInterieur.subsurface((0, 0, self.imageBarInterieur.get_width() * self.proportion, self.imageBarInterieur.get_height()))
        fenetre.blit(self.imageBarContour, (700,20))
        fenetre.blit(imageBar1, (700,20))
        
    def afficherScore(self):
        score_display = myfont.render(str(self.score), 1, (255,255,255))
        fenetre.blit(score_display, (1450, 20))
        


        

class Bonus(pygame.sprite.Sprite):
    #...
    
    def __init__(self, up):
        # Call the parent class (Sprite) constructor
        super().__init__()
        
        self.images = []
        self.images.append(pygame.image.load("bonus laser.png").convert_alpha())
        self.images.append(pygame.image.load("bonus vaisseau.png").convert_alpha())
        self.images.append(pygame.image.load("vie.png").convert_alpha())
        self.images.append(pygame.image.load("bonus bar vie petit.png").convert_alpha())
        self.images.append(pygame.image.load("bonus bar vie.png").convert_alpha())
        
        self.probabilite = [0.20 , 0.20 , 0.05 , 0.50 , 0.05]
        self.probabiliteCumule = [1 , 0.80 , 0.60 , 0.55 , 0.05]
        p = random.randint(1,1000)/1000
        for i in range(0,5) :
            if p <= self.probabiliteCumule[i] :
                self.type = i
        
        self.image = self.images[self.type]
        
        self.imageRotation = pygame.image.load("bonus laser.png").convert_alpha()
        
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0,1540)
        self.rect.y = random.randint(0,740) +60
        self.angle = 0
        self.tourner = 1
        self.xCentre = self.image.get_width() / 2
        self.yCentre = self.image.get_height() / 2
        
        self.up = up
        
        
    def update(self):
        # Call the parent class (Sprite) constructor
        super().update()
        
        self.rect.y += 1
        
        if self.type == 0 :
            self.angle += 9
            self.image = pygame.transform.rotate(self.imageRotation, self.angle)
        
        
        if self.rect.y >= screen_hauteur :
            self.kill()
        else :
            fenetre.blit(self.image, (round(self.rect.x + self.xCentre - self.image.get_width()/2),round(self.rect.y + self.yCentre - self.image.get_height()/2)))
            
    def activer(self):
        
        if self.type == 0 :
            if self.up.vaisseau.laserNiveau < 3 :
                self.up.vaisseau.laserNiveau += 1
            
            self.up.joueur.score += 20
                
        elif self.type == 1 :
            if self.up.vaisseau.niveau < 2 :
                self.up.vaisseau.changeNiveau(self.up.vaisseau.niveau + 1)
            
            self.up.joueur.score += 20
                
        elif self.type == 2 :
            self.up.joueur.vie += 1
            self.up.joueur.score += 50
            
        elif self.type == 3 :
            self.up.vaisseau.vie += 50
            self.up.vaisseau.vie = min(self.up.vaisseau.vie , self.up.vaisseau.vieMax[self.up.vaisseau.niveau])
            self.up.joueur.score += 10
            
        else :
            self.up.vaisseau.vie = self.up.vaisseau.vieMax[self.up.vaisseau.niveau]
            self.up.joueur.score += 40
        
        self.kill()
        
        
        
class Niveau():
    
    def __init__(self, up):
        
        # niveauAsteroids[niveau][type][grandeur] -> nombre d'ast�roide d'un type et d'une grandeur
        self.niveauAsteroids = [[[2,2,1],[2,1,0],[1,1,0]] , [[1,1,1],[1,2,1],[2,2,0]] , [[0,1,1],[2,2,2],[2,2,1]] , [[2,2,2],[2,2,2],[2,2,2]] , [[0,1,1],[0,3,2],[4,2,2]] , [[0,1,2],[1,2,3],[2,3,3]] , [[1,2,3],[1,2,3],[4,5,6]]]
        self.niveau = 0
        self.asteroids = pygame.sprite.Group()
        for i in range(0,3):
            for j in range(0,3):
                for _ in range(0,self.niveauAsteroids[self.niveau][i][j]):
                    asteroid = Asteroid(self,i,j)
                    self.asteroids.add(asteroid)
        
        
        self.niveauEnnemis = [[[1,0,0],[0,0,0],[0,0,0]] , [[0,1,0],[1,0,0],[1,0,0]] , [[3,2,1],[0,0,0],[0,0,0]] , [[1,1,0],[2,1,0],[2,1,0]] , [[1,0,1],[1,3,1],[2,0,0]] , [[0,0,1],[0,0,2],[3,1,1]] , [[0,0,2],[0,2,2],[2,2,2]]] 
        self.ennemis = pygame.sprite.Group()
        self.lasersEnnemis = pygame.sprite.Group()
        self.projectilesSensibles = pygame.sprite.Group()
        for i in range(0,3):
            for j in range(0,3):
                for _ in range(0,self.niveauEnnemis[self.niveau][i][j]):
                    ennemi = Ennemis(self,i,j)
                    self.ennemis.add(ennemi)
        
        
        self.vaisseau = Vaisseau(self)
        
        self.lasers = pygame.sprite.Group()
        for i in range(0,4):
            laser = Laser(self)
            self.lasers.add(laser)
        
        self.joueur = Joueur(self)
        
        self.scoreNiveau = [200, 500, 1000, 2000, 4000, 8000, 99999]
        self.scoreNiveau2 = [0, 200, 500, 1000, 2000, 4000, 8000, 99999]
        self.bonus = pygame.sprite.Group()
        
        self.fond = []
        for i in range(1,8):
            self.fond.append(pygame.image.load("fond niv" + str(i) + ".jpg").convert())
        
        self.quitter = 0
        self.up = up
        
    def update(self):
        
        self.evenement()
        
        fenetre.blit(self.fond[self.niveau], (0,0))
        self.vaisseau.update()
        self.asteroids.update()
        self.ennemis.update()
        self.lasers.update()
        self.lasersEnnemis.update()
        self.projectilesSensibles.update()
        self.bonus.update()
        self.joueur.afficher()
        pygame.display.flip()
        
        self.collision()
        
        if self.joueur.score >= self.scoreNiveau[self.niveau]:
            self.changeNiveau()
            
        pygame.display.flip()
        
            
    def changeNiveau(self):
        
        self.niveau += 1
        self.joueur.niveau += 1
        
        self.vaisseau.rect.x = math.floor(screen_largeur / 2)
        self.vaisseau.rect.y = screen_hauteur -150
        
        self.lasers = pygame.sprite.Group()
        self.lasersEnnemis = pygame.sprite.Group()
        self.projectilesSensibles = pygame.sprite.Group()
        
        self.asteroids = pygame.sprite.Group()
        for i in range(0,3):
            for j in range(0,3):
                for _ in range(0,self.niveauAsteroids[self.niveau][i][j]):
                    asteroid = Asteroid(self,i,j)
                    self.asteroids.add(asteroid)
                    
        self.ennemis = pygame.sprite.Group()
        for i in range(0,3):
            for j in range(0,3):
                for _ in range(0,self.niveauEnnemis[self.niveau][i][j]):
                    ennemi = Ennemis(self,i,j)
                    self.ennemis.add(ennemi)
            
        
    def creationNiveau(self): 
        
        self.vaisseau.rect.x = math.floor(screen_largeur / 2)
        self.vaisseau.rect.y = screen_hauteur -150
        
        if self.vaisseau.laserNiveau > 0 :
            self.vaisseau.laserNiveau -= 1
        if self.vaisseau.niveau > 0 :
            self.vaisseau.changeNiveau(self.vaisseau.niveau - 1)
            
        self.vaisseau.vie = self.vaisseau.vieMax[self.vaisseau.niveau]
        self.joueur.score = max(self.joueur.score-100 , self.scoreNiveau2[self.niveau])
        
        self.bonus = pygame.sprite.Group()
        self.lasers = pygame.sprite.Group()
        self.lasersEnnemis = pygame.sprite.Group()
        self.projectilesSensibles = pygame.sprite.Group()
        
        self.asteroids = pygame.sprite.Group()
        for i in range(0,3):
            for j in range(0,3):
                for _ in range(0,self.niveauAsteroids[self.niveau][i][j]):
                    asteroid = Asteroid(self,i,j)
                    self.asteroids.add(asteroid)
                    
        self.ennemis = pygame.sprite.Group()
        for i in range(0,3):
            for j in range(0,3):
                for _ in range(0,self.niveauEnnemis[self.niveau][i][j]):
                    ennemi = Ennemis(self,i,j)
                    self.ennemis.add(ennemi)
        
                    
    def initialisation(self): 
        
        self.niveau = 0
        self.vaisseau.laserNiveau = 0
        self.vaisseau.changeNiveau(0)
        self.joueur.score = 0
        self.joueur.vie = 3
        
        self.creationNiveau()
        
        
    def lancer(self):
        
        #pygame.key.set_repeat(10,10)
        
        self.initialisation()
        
        while self.quitter == 0 :
            
            self.update()
            
            
        
        
    def evenement(self):
        
        #detect up,down,left,right keypresses
        if pygame.key.get_pressed()[pygame.K_UP] != 0 :
            if self.vaisseau.rect.y >= 9:
                self.vaisseau.rect.y -= 9
                    
        if pygame.key.get_pressed()[pygame.K_DOWN] != 0 :
            if self.vaisseau.rect.y <= 841:
                self.vaisseau.rect.y += 9
                    
        if pygame.key.get_pressed()[pygame.K_LEFT] != 0 : #Gauche
            if self.vaisseau.rect.x >= 9:
                self.vaisseau.rect.x -= 9
                
        if pygame.key.get_pressed()[pygame.K_RIGHT] != 0 : #Droite
            if self.vaisseau.rect.x <= 1481:
                self.vaisseau.rect.x += 9
                
        if pygame.key.get_pressed()[pygame.K_ESCAPE] != 0 : 
            self.quitter = 1
        
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
        
        if pygame.mouse.get_pressed()[0] == 1 :
            self.vaisseau.tirer()
            
        if self.joueur.vie == 0 :
            self.quitter = 1
            
                
    def collision(self):
        
            collisionList = pygame.sprite.spritecollide(self.vaisseau, self.asteroids, False)
            for asteroid in collisionList :
                if asteroid.imateriel == 0 :
                    self.vaisseau.recoitDegats(asteroid.degats[asteroid.type][asteroid.grandeur])
                        
            collisionList = pygame.sprite.spritecollide(self.vaisseau, self.lasersEnnemis, False)
            for laserEnnemi in collisionList :
                self.vaisseau.recoitDegats(laserEnnemi.degatsEnnemis[laserEnnemi.type][laserEnnemi.grandeur])
                        
            collisionList = pygame.sprite.spritecollide(self.vaisseau, self.bonus, False)
            for bonus in collisionList :
                bonus.activer()
            
            collisionList = pygame.sprite.spritecollide(self.vaisseau, self.projectilesSensibles, False)
            for projectileSensible in collisionList :
                if projectileSensible.Explosion == 0:
                    projectileSensible.explose()
                self.vaisseau.recoitDegats(projectileSensible.degatsEnnemis[projectileSensible.type][projectileSensible.grandeur])
            
            collisionList = pygame.sprite.groupcollide(self.lasers, self.asteroids, 0, 0)
            for laser in collisionList.keys() :
                for asteroid in collisionList[laser] :
                    if asteroid.imateriel == 0 :
                        asteroid.recoitDegats(laser.degats[laser.niveau])
                        laser.kill()
                        
            collisionList = pygame.sprite.groupcollide(self.lasers, self.ennemis, 0, 0)
            for laser in collisionList.keys() :
                for ennemi in collisionList[laser] :
                    if ennemi.imateriel == 0 :
                        ennemi.recoitDegats(laser.degats[laser.niveau])
                        laser.kill()
            
            collisionList = pygame.sprite.groupcollide(self.projectilesSensibles, self.asteroids, 0, 0)
            for projectileSensible in collisionList.keys() :
                for asteroid in collisionList[projectileSensible]:
                    if asteroid.imateriel == 0 :
                        if projectileSensible.Explosion == 0:
                            projectileSensible.explose()
                        asteroid.recoitDegats(projectileSensible.degatsEnnemis[projectileSensible.type][projectileSensible.grandeur])
            
            collisionList = pygame.sprite.groupcollide(self.lasers, self.projectilesSensibles, 0, 0)
            for laser in collisionList.keys() :
                for projectileSensible in collisionList[laser] :
                    projectileSensible.explose()
                    

class MenuDemarrer():
    
    def __init__(self):
        
        self.fond = pygame.image.load("fond accueil.jpg").convert()
        self.boutonStart = pygame.image.load("bouton start.jpg").convert()
        
        self.startX = 720
        self.startY = 110
        
        self.niveau = Niveau(self)
        
        self.cadre = pygame.image.load("cadre.png").convert_alpha()
        self.fontTitre = pygame.font.SysFont("times", 18 , 1)
        self.fontNormal = pygame.font.SysFont("times", 18 , 0)
    
        self.fichierScoresR = open("Meilleurs scores.txt", "r")
        #self.fichierScoresW = open("Meilleurs scores.txt", "w")
        
        self.chaineScores = self.fichierScoresR.read()
        

        
        
    def evenement(self):
        
        for event in pygame.event.get():    #Attente des �v�nements
    
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1 and event.pos[1] < self.startY+150 and event.pos[1] > self.startY and event.pos[0] < self.startX+300 and event.pos[0] > self.startX:   #Si clic gauche et souris sur bouton start
                    self.niveau.lancer()
                    
            if event.type == QUIT:
                self.fichierScoresR.close()
                exit()
                
        if pygame.key.get_pressed()[pygame.K_ESCAPE] != 0 : 
            self.fichierScoresR.close()
            exit()

                
    def update(self):
        
        fenetre.blit(self.fond, (0,0))
        fenetre.blit(self.boutonStart, (720,110))
        self.afficheFenetreScore()
        
        
        
        
        self.niveau.joueur.afficherScore()
        pygame.display.flip()
        
        self.evenement()
        
    def lancer(self):
        
        """pygame.mixer.music.load("Albator.mp3")
        
        #pygame.mixer.music.load('Ouverture Sas.mp3')
        pygame.mixer.music.queue('Skip Beat opening.mp3')
        pygame.mixer.music.play()
        pygame.mixer.music.queue('Ouverture Sas.mp3')
        
        pygame.mixer.music.queue("Zero no Tsukaima-Opening .mp3")
        pygame.mixer.music.queue("No game No Life Opening.mp3")
        pygame.mixer.music.queue("High School DxD Ending.mp3")
        pygame.mixer.music.queue("Hikaru no Go op.mp3")
        pygame.mixer.music.queue("Skip_Beat_-Namida.mp3")
        #pygame.mixer.music.play()"""

        while 1 :
            
            self.update()

           
    def afficheFenetreScore(self):
        
        fenetre.blit(self.cadre, (50,150))
        score_display = self.fontTitre.render("Meilleurs scores: ", 1, (255,255,255))
        fenetre.blit(score_display, (65, 155))
        
        
        listeScore = self.chaineScores.split()
        
            
        for i in range(0,len(listeScore)) :
            ligneListe = listeScore[i].split(':')
            nom = self.fontNormal.render(ligneListe[0], 1, (255,255,255))
            fenetre.blit(nom, (65, 190 + 25*i))
            score = self.fontNormal.render(ligneListe[1], 1, (255,255,255))
            fenetre.blit(score, (400, 190 + 25*i))
        

        

menuDemarrer = MenuDemarrer()
menuDemarrer.lancer()
