import pygame
import math
import random
pygame.init()
screenX = 1920
screenY = 1080
screen = pygame.display.set_mode((screenX, screenY))
doExit = False
lines = 0
cameraX = 0
cameraY = 0
scale = 1
Clock = pygame.time.Clock()

# https://docs.google.com/presentation/d/1_9vaR8Gl3kL8IgQ9PZxdM65N26y-_QPE6OMWVh0LTdU/edit#slide=id.g2675e1715c5_0_20

def midPoint(num1, num2):
    return(num1 + (num2 - num1)/2)

def onScreen(x, y):
    if (x > 0 and x < screenX) and (y > 0 and y < screenY):
        return True
    else:
        return False

def sierpinski(x1, y1, x2, y2, x3, y3, counter, isEven, screen, scale):
    counter += 1
    if counter <= countScaleVal:
        if isEven and counter == countScaleVal: #only draws the triangles on the 8th frame to prevent overdraw.
            # r = random.randint(0, 255)#(counter * 100) % 255
            # g = random.randint(0, 255)
            # b = random.randint(0, 255)
            # color = (r, g, b)
            baseColor = 255
            color = (baseColor, baseColor, baseColor)
            
            # pygame.draw.polygon(screen, color, ((x1, y1), (x2, y2), (x3, y3)))
            if onScreen(x1, y1) or onScreen(x2, y2):
                pygame.draw.line(screen, color, (x1, y1), (x2, y2))
                global lines
                lines += 1
            if onScreen(x2, y2) or onScreen(x3, y3):
                pygame.draw.line(screen, color, (x2, y2), (x3, y3))
                lines += 1
            if onScreen(x3, y3) or onScreen(x1, y1):
                pygame.draw.line(screen, color, (x3, y3), (x1, y1))
                lines += 1

        midx1x2 = midPoint(x1, x2)
        midy1y2 = midPoint(y1, y2)
        midx3x1 = midPoint(x3, x1)
        midy3y1 = midPoint(y3, y1)
        midx3x2 = midPoint(x3, x2)
        midy3y2 = midPoint(y3, y2)
        if onScreen(x1, y1) or onScreen(midx1x2, midy1y2) or onScreen(midx3x1, midy3y1) and counter > 2:
            sierpinski(x1, y1, midx1x2, midy1y2, midx3x1, midy3y1, counter, isEven, screen, scale)
        if onScreen(midx1x2, midy1y2) or onScreen(x2, y2) or onScreen(midx3x2, midy3y2):
            sierpinski(midx1x2, midy1y2, x2, y2, midx3x2, midy3y2, counter, isEven, screen, scale)
        if onScreen(midx3x1, midy3y1) or onScreen(midx3x2, midy3y2) or onScreen(x3, y3):
            sierpinski(midx3x1, midy3y1, midx3x2, midy3y2, x3, y3, counter, isEven, screen, scale)
        # pygame.display.flip()
        isEven *= -1
        return 0



# sierpinski(screenX/2, 0, 0, screenY, screenX, screenY, 0, True, screen, scale)

countScaleVal = 8 #math.floor(8 * ((scale - 1) / 8 + 1))
while not doExit:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            doExit = True

    # cameraX += 1
    # scale += .01

    

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LSHIFT]:
        moveSpeed = -5 * (1/(scale + scale/100)) * 5
    else:
        moveSpeed = -5 * (1/(scale + scale/100))
    if keys[pygame.K_LCTRL]:
        scaleSpeed = (scale/100) * 2
    else:
        scaleSpeed = scale/100
    if keys[pygame.K_w]:
        cameraY -= moveSpeed
        print("lines = " + str(lines))
    if keys[pygame.K_a]:
        cameraX -= moveSpeed
        print("lines = " + str(lines))
    if keys[pygame.K_s]:
        cameraY += moveSpeed
        print("lines = " + str(lines))
    if keys[pygame.K_d]:
        cameraX += moveSpeed
        print("lines = " + str(lines))
    if keys[pygame.K_r]:
        cameraX = 0
        cameraY = 0
        scale = 1
        countScaleVal = 8
    if keys[pygame.K_UP]:
        scale += scaleSpeed
        # cameraX += moveSpeed
        # cameraY += moveSpeed
        if posx3 / (2 ** countScaleVal) > 7.5 and posx3 / (2 ** (countScaleVal + 1)) > 4.5:
            countScaleVal += 1
        print("lines = " + str(lines), scale, countScaleVal, posx3 / (2 ** countScaleVal))
    if keys[pygame.K_DOWN]:
        scale -= scaleSpeed
        # cameraX += moveSpeed
        # cameraY += moveSpeed
        if posx3 / (2 ** countScaleVal) < 4.5:
            countScaleVal -= 1
        print("lines = " + str(lines), scale, countScaleVal, posx3 / (2 ** countScaleVal))

    lines = 0

    screen.fill((0, 0, 0))
    posx1 = (screenX/2 + cameraX) * scale
    posy1 = (0 + cameraY) * scale
    posx2 = (0 + cameraX) * scale# - ((screenY) * scale) - screenY
    posy2 = (screenY + cameraY) * scale
    posx3 = (screenX + cameraX) * scale
    posy3 = (screenY + cameraY) * scale


    sierpinski(posx1, posy1, posx2, posy2, posx3, posy3, 0, True, screen, scale)

    pygame.display.flip()
pygame.quit()