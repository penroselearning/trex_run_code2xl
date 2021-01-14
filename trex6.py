# #########
## Step 6
## You will lose points if above the TREX is continously above the floor for a certain number of seconds
## Create a penalty variable and set it to zero
## Increment the penalty by 1/60th of a second each time the TREX is above the ground
## When the penalty reaches 10 seconds, the score should decrement
## Play a sound continously when the player is being penalised
## Change font color of score when the player is being penalised
## Display the best score at the bottom of the screen
########

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

best_score = 0

JUMP_HEIGHT = (FLOOR - 100)
FALL_SPEED = 4

# Running Postures of TRex
trex_pose = ['run1','run2']
x = 0

# Number of Frames each image should be displayed
frames_per_image = 30

penalty = 0

def draw():
    screen.clear()
    screen.fill((255,255,255))
    screen.blit('floor-1',(5,456))
    
    if penalty >=10:
        screen.draw.text(str(score),(430,5),fontsize=50,fontname='pixelmix_bold', color="red")
    else:
        screen.draw.text(str(score),(430,5),fontsize=50,fontname='pixelmix_bold', color="black")
    # Display the Score on the Game Screen
    # use str() to display the score.
    # integers will not display on the game screen unless converted to string

    if best_score > 0:
        best_score_text = f'Your Best score is {str(best_score)}'
        
        screen.draw.text(best_score_text,(40,500),
        fontsize=30,fontname='pixelmix_bold', color="black")
    

    trex.draw()
    cactus.draw()

def update():
    global speed,score,x,penalty,best_score

    # Move the cactus to its left
    cactus.left -= speed

    # since the update function runs 60 times per second
    # we will increase the score by 1 for every 1 second
    if penalty >= 10:
        sounds.point.play()
        score -= 1/60
    else:
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
        # update the best score
        if score > best_score:
            best_score = score
            
        score = 0
        
        sounds.point.play()

    # if trex jumps, it will have trex.y value less than FLOOR
    # it should then fall at the speed of FALL_SPEED variable
    if trex.y < FLOOR:
        penalty += 1/60
        trex.y += FALL_SPEED
    # the trex should not fall below FLOOR Level
    # when the trex reaches the floor level
    # maintain it at the same floor level
    elif trex.y == FLOOR:
        penalty = 0
        trex.y = FLOOR

        trex.image = trex_pose[x//frames_per_image]
        x += 1

        if x//frames_per_image >= len (trex_pose):
            x = 0


def on_key_down():
    if keyboard.SPACE:
        trex.y = JUMP_HEIGHT;


