'''
Created on 23 sept. 2018

@author: Swann
'''

from src.utility.pygame_textinput import TextInput
import pygame
import os
from tkinter.filedialog import askopenfilename
from src.constant import PATH_CARDS

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
errorColor = pygame.Color("0xff0000") #RRGGBB

#---------------------------------- OUTPUT ----------------------------------

infoText = fontText.render("Use <enter> key to go in the next entry.", True, importImageColor)

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

name = TextInput("DSK", font_family="times", font_size=FONT_SIZE, text_color=inputColor, cursor_color=textColor)
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
select = nameText # indique qui est selectionné
x, y = 10, 50
pady = nameText.get_height()
selectPos = (0,0)
imageTextPos = (x, pady*11)
validatePos = (x, pady*13)
errorPos = (x, pady*15)
imagePos = (x+350, y)
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

error = fontText.render("", True, errorColor)

def Validation():
    global error
    if len(name.get_text()) < 2:
        error = fontText.render("invalid name", True, errorColor)
        print("invalid name")
        return False
    
    if type.get_text() == "creature":
        try:
            int(power.get_text())
        except:
            print("invalid power")
            error = fontText.render("invalid power", True, errorColor)
            return False
        try:
            int(movement.get_text())
        except:
            print("invalid movement")
            error = fontText.render("invalid movement", True, errorColor)
            return False
        try:
            int(range.get_text())
        except:
            print("invalid range")
            error = fontText.render("invalid range", True, errorColor)
            return False
        try:
            int(capacity.get_text())
        except:
            print("invalid capacity")
            error = fontText.render("invalid capacity", True, errorColor)
            return False
            
    elif type.get_text() == "magic":
        try:
            int(powerBonus.get_text())
        except:
            print("invalid power")
            error = fontText.render("invalid power", True, errorColor)
            return False
        try:
            int(castleBonus.get_text())
        except:
            print("invalid castle life")
            error = fontText.render("invalid castle life", True, errorColor)
            return False
        try:
            int(movementBonus.get_text())
        except:
            print("invalid movement")
            error = fontText.render("invalid movement", True, errorColor)
            return False
        try:
            int(rangeBonus.get_text())
        except:
            print("invalid range")
            error = fontText.render("invalid range", True, errorColor)
            return False
        try:
            int(weight.get_text())
        except:
            print("invalid weight")
            error = fontText.render("invalid weight", True, errorColor)
            return False
        
    elif type.get_text() == "trap":
        try:
            int(damageTrap.get_text())
        except:
            print("invalid damage")
            error = fontText.render("invalid damage", True, errorColor)
            return False
        try:
            int(rangeTrap.get_text())
        except:
            print("invalid range")
            error = fontText.render("invalid range", True, errorColor)
            return False
        try:
            int(weight.get_text())
        except:
            print("invalid weight")
            error = fontText.render("invalid weight", True, errorColor)
            return False
    
    else:
        print("invalid type")
        error = fontText.render("invalid type", True, errorColor)
        return False
    
    if image != None:
        if image.get_size() != (320, 320):
            print("image must be 320x320 pixel")
            error = fontText.render("image must be 320x320 pixel", True, errorColor)
            return False
    else:
        print("no image")
        error = fontText.render("no image", True, errorColor)
        return False
    
    if os.path.exists(os.path.join(PATH_CARDS, name.get_text())):
        print("card name already used")
        error = fontText.render("card name already used", True, errorColor)
        return False
    
    error = fontText.render("", True, errorColor)
    return True

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
                
        else:
            screen.blit(allTypes[i_type][1][i].get_surface(), (x + text.get_width(), y + pady*i))

    
    screen.blit(validateText, validatePos)
    screen.blit(importImage, imageTextPos)
    
    screen.blit(infoText, (200, 10))
    screen.blit(error, errorPos)
    
    pygame.display.update()
    clock.tick(30)
    
#---------------------------------- AFTER VALIDATION ----------------------------------

path = os.path.join(PATH_CARDS, name.get_text())
os.makedirs(path)

f = open(os.path.join(path, "infos"), "w")

f.write("name: " + name.get_text() + "\n")
f.write("family: " + family.get_text() + "\n")
f.write("description: " + description.get_text() + "\n")
f.write("type: " + type.get_text() + "\n")
f.write("effect: " + effect.get_text() + "\n")

f.close()

f = open(os.path.join(path, "stats"), "w")

if (type.get_text() == "creature"):
    
    f.write("power: " + power.get_text() + "\n")
    f.write("movement: " + movement.get_text() + "\n")
    f.write("range: " + range.get_text() + "\n")
    f.write("capacity: " + capacity.get_text() + "\n")

elif (type.get_text() == "magic"):
    
    f.write("power bonus: " + powerBonus.get_text() + "\n")
    f.write("castle life bonus: " + castleBonus.get_text() + "\n")
    f.write("movement bonus: " + movementBonus.get_text() + "\n")
    f.write("range bonus: " + rangeBonus.get_text() + "\n")
    f.write("weight: " + weight.get_text() + "\n")
    
elif (type.get_text() == "trap"):

    f.write("damage: " + damageTrap.get_text() + "\n")
    f.write("range: " + rangeTrap.get_text() + "\n")
    f.write("weight: " + weight.get_text() + "\n")

f.close()

pygame.image.save(image, os.path.join(path, "image.png"))

