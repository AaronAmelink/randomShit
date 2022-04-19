from curses import BUTTON_SHIFT
from operator import truediv
import pygame
import numpy as np
pygame.init()
screenSize = (500, 500)
display = pygame.display.set_mode(screenSize)
exit = False
global mousePos
global leftClick


class button:
    def __init__(self, position, width, height, color):
        self.position = position
        self.width = width
        self.height = height
        self.color = color

    def draw(self):
        pygame.draw.rect(display, self.color, pygame.Rect(self.position[0], self.position[1], self.width, self.height))
    
    def clicker(self):
        if leftClick:
            if  (mousePos[0] > self.position[0] and mousePos[0] < self.position[0] + self.width) and (mousePos[1] > self.position[1] and mousePos[1] < self.position[1] + self.height):
                #self.color = list(np.random.choice(range(256), size=3))
                return True
            else:
                return False

class buttonManager:
    def __init__(self):
        self.buttonList = []
        self.returnList = []

    def createButton(self, button):
        self.buttonList.append(button)
        self.returnList.append(False)

    def buttons(self):
        counter = 0
        for b in self.buttonList:
            b.draw()
            self.returnList[counter] = b.clicker()
            counter += 1

    def checkButtonPositions(self):
        for x in self.buttonList:
            print(x.position, self.buttonList.index(x))

    def destroyButton(self, index):
        self.buttonList.pop(index)



class sceneManager:
    def __init__(self, display):
        self.currentScene = 1
        self.sceneCheck = 1
        self.display = display
        self.hasLoaded = False
        # everytime you switch scenes, set hasLoaded to false

    def loadCurrentScene(self):
        if self.currentScene == 1:
            self.scene1()
        elif self.currentScene == 2:
            self.scene2()

    def loopCurrentScene(self):
        if self.currentScene == 1:
            self.scene1Loop()
        elif self.currentScene == 2:
            self.scene2Loop()

    def scene2(self):
        pass

    def scene2Loop(self):
        pass

    def scene1(self):
        pass
        #load here
        #set variables, create instances of classes, etc
        
    def scene1Loop(self):
        pass
        #loop here
        #do loop shit

    def loop(self):
        if self.hasLoaded == False:
            self.loadCurrentScene()
            self.hasLoaded = True
        self.loopCurrentScene()




def loop():
    pass
    
    


while not exit:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            leftClick = True
        else:
            leftClick = False
        if event.type == pygame.QUIT:
            exit = True
    mousePos = pygame.mouse.get_pos()



    loop()

    pygame.display.update()