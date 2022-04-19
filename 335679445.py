import math
import pygame

pygame.init()

screenWidth = 500
screenHeight = 500
frameLimit = 60


win = pygame.display.set_mode((screenWidth, screenHeight))
clock = pygame.time.Clock()
#pygame setup

def checkWithin(dynamicPos, independentPos, width, height, draw, win):
    if (draw):
        pygame.draw.rect(win, (255, 0, 0), (independentPos[0], independentPos[1], width, height), 5)
    if ((dynamicPos[0] > independentPos[0]) and (dynamicPos[0] < independentPos[0] + width) and (dynamicPos[1] > independentPos[1]) and (dynamicPos[1] < independentPos[1] + height)):
        return(True)
    else:
        return(False)
    #simple function for checking if something is contained within another


#a simple cursor class to hit the bloon in this demo
class cursor():
    def __init__(self):
        self.click = False

    def getPos(self):
        return pygame.mouse.get_pos()

    def setClick(self, click):
        self.click = click
    
    def getClick(self):
        return(self.click)
    
    def getHoldClick(self):
        return (pygame.mouse.get_pressed()[0])


#Im Just creating a simple player class that satisfies the needs of the bloon class.
class player():
    def __init__(self):
        self.xp = 0
        self.money = 0
    
    def addXp(self, amount):
        self.xp += amount
    
    def addMoney(self, amount):
        self.money += amount


class bloon():
    def __init__(self, win, Level, Path, speed, player):
        self.level = Level
        #bloon level
        self.lastLevel = Level
        #setting a last level to notice a change in level
        self.win = win
        #getting the pygame window
        self.x, self.y = Path[0]
        #setting starting position
        self.path = Path
        #a path list, a list of position tuples of (x, y)
        self.health = 0
        #since bloon health is set by the method below, set to 0
        self.setHealth()
        self.setColor()
        self.heading = 1
        #set starting heading; heading being where the bloon is going in the path attribute.
        self.speed = speed
        #speed
        self.xstep = 0
        self.ystep = 0
        #x and y step set to 0 to start
        self.player = player
        #getting the player class to add xp and money
        self.updatePosition(self.path[self.heading], self.speed)
        #calling the update position method to start the bloon
    
    def setHealth(self):
        if self.level == 3:
            self.health = 10
        if self.level == 2:
            self.health = 5
        if self.level == 1:
            self.health = 1
        #sets the bloons health based off the level

    def setColor(self):
        if (self.level == 1):
            self.color = (255, 0, 0)
        elif (self.level == 2):
            self.color = (0, 0, 255)
        elif (self.level == 3):
            self.color = (0, 255, 0)
        #sets the bloons color based off the level

    def setLevel(self, health):
        if health <= 10:
            self.level = 3
            if health <=5:
                self.level = 2
                if health <= 2:
                    self.level = 1
                    if health <= 0:
                        self.level = 0
        #sets the level based off health, to be continually called as to change bloon level if it gets hit
        
        if self.lastLevel != self.level:
            self.player.addXp(self.lastLevel)
            self.player.addMoney(self.lastLevel)
            self.lastLevel = self.level
            #checking if level changes, and giving the player XP and money for that.

    def hit(self, amount):
        self.health -= amount
        return(self.health)
        #hitting the bloon

    def getPos(self):
        return ((self.x, self.y))
        #getting bloon pos

    def getDistanceFromHeading(self):
        if self.heading < len(self.path):
            self.distanceFromHeading = abs(math.hypot(self.path[self.heading][0] - self.x, self.path[self.heading][1] - self.y))
            return(self.heading, self.distanceFromHeading)
        else:
            return(-1, -1)
        #getting distance from the bloons heading, for the bloon Manager to compare to get the farthest bloon.

    def updatePosition(self, target, speed):
        self.speed = speed
        self.deltaX = target[0] - self.x
        self.deltaY = target[1] - self.y

        if (abs(self.deltaX) > abs(self.deltaY)):
            if self.deltaX != 0:
                self.ystep = (self.deltaY / abs(self.deltaX))
                if (self.x > target[0]):
                    self.xstep = -1
                else:
                    self.xstep = 1
        else:
            if (self.deltaY != 0):
                self.xstep = (self.deltaX / abs(self.deltaY))
                if self.y > target[1]:
                    self.ystep = -1
                else:
                    self.ystep = 1
        #really all this does is calculate the rise/run of the bloon relative to its next position.
        #xstep being run, ystep being rise.


    def move(self):
        if self.heading < len(self.path):
            self.x += 1 * self.xstep * self.speed
            self.y += 1 * self.ystep * self.speed
            if checkWithin((self.x + 3.25, self.y + 3.25), (self.path[self.heading][0], self.path[self.heading][1]), 10, 10, False, self.win):
                #this checks if the bloon hits its heading on the path;
                #if it does it sets its heading to the next heading in the path
                self.heading += 1
                if self.heading < len(self.path):
                    self.updatePosition(self.path[self.heading], self.speed)
                    # if the heading is in the path then update where the bloon is going

            # moving the player

    def draw(self):
        pygame.draw.circle(self.win, self.color, (self.x, self.y), 7.5)
        #draw the bloon as a circle
    
    
    def calls(self):
        if self.level > 0:
            self.setColor()
            self.setLevel(self.health)
            self.move()
            self.draw()
        #all the calls for the bloon, just so that you can call one thing, rather than four.

path = [(10, 0), (100, 100), (20, 30), (60, 60), (80, 80), (500, 400), (300, 300), (250, 250)]
#creating the path the bloon will follow.
player1 = player()
bloon1 = bloon(win, 3, path, 2, player1)
mouse = cursor()
#creating instances of each object needed. Usually a bloon manager would create the bloons, but as this is an isolated demo we are doing it manually.

def main():
    hasClicked = False
    running = True
    #setting everything to default values to start the loop.
    while running:
        mouse.setClick(False)
        #setting the click to false at the start of the frame for concitentsy. (consitancy?)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running=False
            #checking if the quit button is clicked
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if hasClicked == False:
                    mouse.setClick(True)
                    hasClicked = True
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                if hasClicked == True:
                    hasClicked = False
            #getting all the events for mouse clicks.

        win.fill((0,0,0))
        #filling the win with black before drawing, otherwise the frame doesnt get redrawn.
        if checkWithin(mouse.getPos(), (bloon1.getPos()[0] - 3.75, bloon1.getPos()[1] - 3.75), 7.5, 7.5, False, win):
            if (mouse.getClick()):
                bloon1.hit(2)
                #checking to see if you click the bloon. Normally a turret would do this, but again as this is isolated were doing it manually here.

        bloon1.calls()
        #calling all the needed functions. usually the bloon manager would be doing this.

        pygame.display.flip()
        #updating the display.
        clock.tick(60)
        #updating the internal pygame clock.

    pygame.quit()
    #quit at the end of the loop
        




main()
#calling main
