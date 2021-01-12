# #########
## Step 2
## Set the Speed for the Cactus to move across the screen
## Create the Update Function to enable animation in the game
## Change the position of the Cactus using the speed value
## When the cactus disappears from the screen bring another random cactus to original position
## Since it is random, the same cactus could be repeated
## Each time a new cactus displays, its speed of movement increases
#########

import random
WIDTH = 600

HEIGHT = 600
FLOOR = 440

cactuses = ['cactus1','cactus2','cactus3','cactus4','cactus5']
random_cactus = random.choice(cactuses)

trex = Actor('idle')
trex.pos = (125,FLOOR)
# Set the Position of the T-Rex

cactus = Actor(random_cactus)
cactus.pos = (544,FLOOR)
# Set the Position of the Cactus

speed = 1
# Sets the starting speed for the cactus to move to the left

def draw():
    screen.clear()
    screen.fill((255,255,255))
    screen.blit('floor-1',(5,456))
    
    trex.draw()
    cactus.draw()

def update():
    global speed
    # Move the cactus to its left
    cactus.left -= speed
    
    # If the cactus disappears from the left of the screen
    # bring back a random cactus in original position
    if cactus.left < -10:
        cactus.pos = (544,FLOOR)
        cactus.image = random.choice(cactuses)
        
        # increases the speed each time a new cactus gets displayed
        speed += 0.1
