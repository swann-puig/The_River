'''
Created on 23 sept. 2018

@author: Swann
'''

from src.utility.pygame_textinput import TextInput
import pygame
import subprocess
from tkinter.filedialog import askopenfilename

pygame.init()
pygame.display.set_caption("Editor")

screen = pygame.display.set_mode((900, 600))
clock = pygame.time.Clock()

FONT_SIZE = 28
FONT_TITLE = 36
fontText = pygame.font.SysFont("times", FONT_SIZE)
fontTitle = pygame.font.SysFont("times", FONT_TITLE)
textColor = pygame.Color("0x000000") #RRGGBB
inputColor = pygame.Color("0x800000") #RRGGBB
backgroundColor = pygame.Color("0xe1e1e1") #RRGGBB
validateColor = pygame.Color("0x00ff00") #RRGGBB
importImageColor = pygame.Color("0x0000ff") #RRGGBB

#---------------------------------- OUTPUT ----------------------------------

nameText = fontText.render("name: ", True, textColor)
familyText = fontText.render("family: ", True, textColor)
descriptionText = fontText.render("description: ", True, textColor)
typeText = fontText.render("type: ", True, textColor)
effectText = fontText.render("effect name: ", True, textColor)

# creature stats
powerText = fontText.render("power: ", True, textColor)
movementText = fontText.render("movement: ", True, textColor)
rangeText = fontText.render("attack range: ", True, textColor)
capacityText = fontText.render("equipment capacity: ", True, textColor)

# magic stats
powerBonusText = fontText.render("power bonus: ", True, textColor)
castleBonusText = fontText.render("castle life bonus: ", True, textColor)
movementBonusText = fontText.render("movement bonus: ", True, textColor)
rangeBonusText = fontText.render("range bonus: ", True, textColor)

# trap stats
damageTrapText = fontText.render("damage: ", True, textColor)
rangeTrapText = fontText.render("attack range: ", True, textColor)

# trap and magic
weightText = fontText.render("weight: ", True, textColor)

#---------------------------------- INPUT ----------------------------------

name = TextInput(font_family="times", font_size=FONT_SIZE, text_color=inputColor, cursor_color=textColor)
family = TextInput(font_family="times", font_size=FONT_SIZE, text_color=inputColor, cursor_color=textColor)
description = TextInput(font_family="times", font_size=FONT_SIZE, text_color=inputColor, cursor_color=textColor)
type = TextInput(font_family="times", font_size=FONT_SIZE, text_color=inputColor, cursor_color=textColor)
effect = TextInput(font_family="times", font_size=FONT_SIZE, text_color=inputColor, cursor_color=textColor)

# creature stats
power = TextInput(font_family="times", font_size=FONT_SIZE, text_color=inputColor, cursor_color=textColor)
movement = TextInput(font_family="times", font_size=FONT_SIZE, text_color=inputColor, cursor_color=textColor)
range = TextInput(font_family="times", font_size=FONT_SIZE, text_color=inputColor, cursor_color=textColor)
capacity = TextInput(font_family="times", font_size=FONT_SIZE, text_color=inputColor, cursor_color=textColor)

# magic stats
powerBonus = TextInput(font_family="times", font_size=FONT_SIZE, text_color=inputColor, cursor_color=textColor)
castleBonus = TextInput(font_family="times", font_size=FONT_SIZE, text_color=inputColor, cursor_color=textColor)
movementBonus = TextInput(font_family="times", font_size=FONT_SIZE, text_color=inputColor, cursor_color=textColor)
rangeBonus = TextInput(font_family="times", font_size=FONT_SIZE, text_color=inputColor, cursor_color=textColor)

# trap stats
damageTrap = TextInput(font_family="times", font_size=FONT_SIZE, text_color=inputColor, cursor_color=textColor)
rangeTrap = TextInput(font_family="times", font_size=FONT_SIZE, text_color=inputColor, cursor_color=textColor)

# trap and magic
weight = TextInput(font_family="times", font_size=FONT_SIZE, text_color=inputColor, cursor_color=textColor)

#---------------------------------- BUTTON & IMAGE----------------------------------
validateText = fontTitle.render("<Validate>", True, validateColor)
importImage = fontTitle.render("<Import Image>", True, importImageColor)
image = None

#---------------------------------- SELECTION ----------------------------------
select = typeText # indique qui est selectionné
x, y = 10, 10
pady = nameText.get_height()
selectPos = (0,0)
imageTextPos = (x, pady*12)
validatePos = (x, pady*14)
imagePos = (x+350, 10)
selectNext = False

commonText  = [nameText, familyText, descriptionText, typeText, effectText]
commonInput = [name, family, description, type, effect]

creatureText  = [powerText, movementText, rangeText, capacityText]
creatureInput = [power, movement, range, capacity]

magicText  = [powerBonusText, castleBonusText, movementBonusText, rangeBonusText, weightText]
magicInput = [powerBonus, castleBonus, movementBonus, rangeBonus, weight]

trapText  = [damageTrapText, rangeText, weightText]
trapInput = [damageTrap, rangeTrap, weight]

allTypes = [None, (creatureText, creatureInput), (magicText, magicInput), (trapText, trapInput)]

def Validation():
    print("DSK")


validate = False

while not validate:
    screen.fill(backgroundColor)

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            exit()
            
        elif event.type == pygame.MOUSEBUTTONDOWN:
            rect = validateText.get_rect()
            if validatePos[0] < event.pos[0] and event.pos[0] < validatePos[0] + rect.width and validatePos[1] < event.pos[1] and event.pos[1] < validatePos[1] + rect.height:
                if Validation():
                    validate = True
                
            rect = importImage.get_rect()
            if imageTextPos[0] < event.pos[0] and event.pos[0] < imageTextPos[0] + rect.width and imageTextPos[1] < event.pos[1] and event.pos[1] < imageTextPos[1] + rect.height:
                ftypes = [('PNG files', '*.png'), ('All files', '*')]
                filename = askopenfilename(filetypes=ftypes)
                print(filename)
                image = pygame.image.load(filename).convert_alpha()
                print(image)
                try:
                    pass
                except:
                    image = None
    
    if (image != None): screen.blit(image, imagePos)
    
    if selectNext:
        select = commonText[0]
        
    for i, text in enumerate(commonText):
        screen.blit(text, (x, y + pady*i))
        if select == text:
            selectNext = commonInput[i].update(events)  # return True if key <Enter> pressed
            if selectNext:
                if (i < len(commonText) - 1):
                    select = commonText[i+1]
                    selectNext = False
                    
            events = []
            pygame.event.clear()
            screen.blit(commonInput[i].get_surface(), (x + text.get_width(), y + pady*i))
            
        else:
            screen.blit(commonInput[i].get_surface(), (x + text.get_width(), y + pady*i))
            
    line = len(commonText)

    i_type = 0
    if (type.get_text() == "creature"): i_type = 1
    elif (type.get_text() == "magic"):  i_type = 2
    elif (type.get_text() == "trap"):   i_type = 3
        
    if i_type > 0:
            
        if selectNext:
            select = allTypes[i_type][0][0]
            
        for i, text in enumerate(allTypes[i_type][0]):
            screen.blit(text, (x, y + pady * (i + line)))
            if select == text:
                selectNext = allTypes[i_type][1][i].update(events)  # return True if key <Enter> pressed
                if selectNext:
                    if (i < len(allTypes[i_type][0]) - 1):
                        select = allTypes[i_type][0][i+1]
                        selectNext = False
                
                events = []
                pygame.event.clear()
                screen.blit(allTypes[i_type][1][i].get_surface(), (x + text.get_width(), y + pady * (i + line)))


    
    screen.blit(validateText, validatePos)
    screen.blit(importImage, imageTextPos)
    
    pygame.display.update()
    clock.tick(30)
    




