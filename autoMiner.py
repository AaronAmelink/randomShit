import pyautogui
print("Width is how far to mine on the right, Height is how far to mine down, and depth is how far to mine forwards.")
print("Please start the player in the highest point of the bottom left of where you want the mine. From a top view:")
print(" * * * * * \n * * * * * \n * * * * * \n * * * * * \n P * * * * ")
width = int(input("The Width of the Mine:"))
height = int(input("The Height of the Mine:"))
depth = int(input("The Depth of the Mine:"))


lookToggle = "Right"
for h in range(0,height - 1):
    for w in range(0, width - 1):
        for d in range(0, depth - 1):
            #break block here
            #look down
            #break block
            #look up
            #walk forward
        if not (w == width-1):    
            if lookToggle == "Right":
                pass
                #look right
            else:
                pass
                #look left
            #break block
            #walk forward
            if lookToggle == "Right":
                lookToggle = "Left"
                #look right
            else:
                lookToggle = "Right"
                #look left
    #look down
    #mine two blocks
    #360
    lookToggle = "Right"
    
        
    