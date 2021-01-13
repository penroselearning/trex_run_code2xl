# #########
## Step 1
## Download the required resources for the game (images and sound)
## Defining the Height and Width of the Game
## Setting the vertical FLOOR Position where the Cactus and T-Rex will be displayed
## Building a List of Cactus file names
## Selecting a Cactus Randomly
## Display the T-Rex and Cactus on the screen
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


def draw():
    screen.clear()
    screen.fill((255,255,255))
    screen.blit('floor-1',(5,456))
    
    trex.draw()
    cactus.draw()
