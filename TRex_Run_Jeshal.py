#########
# Created by Jeshal Mohapatra
# Age 10
# School: GEMS Modern Academy, Dubai, UAE
#########

import random
WIDTH = 688

HEIGHT = 645
FLOOR = 440

trex = Actor('idle',(125,FLOOR))
cactus = Actor('cactus1',(544,FLOOR))
cactusture = ['cactus1','cactus2','cactus3','cactus4','cactus5']

postures = ['run1','run2']

trex.above_ground = 0
frames_per_image = 1

x = 0
score = 0
trex_status = ""
speed = 2

FALL = 0.5
JUMP = -15

def draw():
    screen.clear()
    screen.fill((255,255,255))
    screen.blit('floor-1',(45,456))
    screen.draw.text(str(score),(550,5),fontsize=50,fontname='pixelmix_bold', color="black")

    trex.draw()
    cactus.draw()

def update():
    global x,frames_per_image, score

    cactus.left -= speed
    #print(cactus.left)
    score += 1
    print(score)

    if cactus.right < 59:
        cactus.left = 544
        cactus.image = random.choice(cactusture)

    trex.image = postures[x // frames_per_image]
    x +=1

    if x // frames_per_image >=len (postures):
        x = 0

    trex.above_ground += FALL
    trex.y += trex.above_ground

    if(trex.y > FLOOR):
        trex.y = FLOOR
    else:
        trex.image = 'jump'

    if trex.colliderect(cactus):
        trex_status = "Hit"
        print (trex_status)
        trex.image = 'death'
        score = 0
        print(score)

def on_key_down():
    if keyboard.SPACE:
        trex.above_ground = JUMP# Write your code here :-)
