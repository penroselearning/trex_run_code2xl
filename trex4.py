# #########
## Step 4
## Set the Jump Height Position for the TREX
## Create a New Function for on_key_down
## Set the Position of the TREX when the SPACE key is pressed
## Set the FALL_SPEED (Gravitional Pull)
## Apply the fall logic in the Update Function
## Change the difficulty of the game by altering the Cactus Speed, FALL_SPEED or JUMP_HEIGHT
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

speed = 3
# Sets the starting speed for the cactus to move to the left

score = 0
# Set the starting score of the game

JUMP_HEIGHT = (FLOOR - 100)
FALL_SPEED = 4

def draw():
    screen.clear()
    screen.fill((255,255,255))
    screen.blit('floor-1',(5,456))
    
    screen.draw.text(str(score),(430,5),fontsize=50,fontname='pixelmix_bold', color="black")
    # Display the Score on the Game Screen
    # use str() to display the score. 
    # integers will not display on the game screen unless converted to string
    
    trex.draw()
    cactus.draw()

def update():
    global speed,score
    
    # Move the cactus to its left
    cactus.left -= speed
    
    # since the update function runs 60 times per second
    # we will increase the score by 1 for every 1 second
    score += 1/60
    
    # display the score with just 2 decimal places
    score = round(score,2)
    
    # If the cactus disappears from the left of the screen
    # bring back a random cactus in original position
    if cactus.left < -10:
        cactus.pos = (544,FLOOR)
        cactus.image = random.choice(cactuses)
        
        # increases the speed each time a new cactus gets displayed
        speed += 0.1
    
    # if the trex collides with the cactus, the score is reset to 0
    if trex.colliderect(cactus):
        score = 0
    
    # if trex jumps, it will have trex.y value less than FLOOR
    # it should then fall at the speed of FALL_SPEED variable
    if trex.y < FLOOR:
        trex.y += FALL_SPEED
    # the trex should not fall below FLOOR Level
    # when the trex reaches the floor level
    # maintain it at the same floor level
    elif trex.y == FLOOR:
        trex.y = FLOOR

def on_key_down():
    if keyboard.SPACE:
        trex.y = JUMP_HEIGHT;
        
