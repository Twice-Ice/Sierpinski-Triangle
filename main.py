import pygame
import math
import random
pygame.init()
screenX = 1920
screenY = 1080
screen = pygame.display.set_mode((screenX, screenY))
doExit = False

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
    if counter <= math.floor(8 * scale):
        if isEven and counter == math.floor(8 * scale): #only draws the triangles on the 8th frame to prevent overdraw.
            # r = random.randint(0, 255)#(counter * 100) % 255
            # g = random.randint(0, 255)
            # b = random.randint(0, 255)
            # color = (r, g, b)
            baseColor = 255
            color = (baseColor, baseColor, baseColor)
            
            # pygame.draw.polygon(screen, color, ((x1, y1), (x2, y2), (x3, y3)))
            if onScreen(x1, y1) and onScreen(x2, y2):
                pygame.draw.line(screen, color, (x1, y1), (x2, y2))
            if onScreen(x2, y2) and onScreen(x3, y3):
                pygame.draw.line(screen, color, (x2, y2), (x3, y3))
            if onScreen(x3, y3) and onScreen(x1, y1):
                pygame.draw.line(screen, color, (x3, y3), (x1, y1))
        else:
            pass #no point in drawing something that won't show up so just don't draw it.

        # if onScreen(x1, y1) and onScreen(midPoint(x1, x2), midPoint(y1, y2)) and onScreen(midPoint(x3, x1), midPoint(y3, y1)):
        sierpinski(x1, y1, midPoint(x1, x2), midPoint(y1, y2), midPoint(x3, x1), midPoint(y3, y1), counter, isEven, screen, scale)
        # if onScreen(midPoint(x1, x2), midPoint(y1, y2)) and onScreen(x2, y2) and onScreen(midPoint(x3, x2), midPoint(y3, y2)):
        sierpinski(midPoint(x1, x2), midPoint(y1, y2), x2, y2, midPoint(x3, x2), midPoint(y3, y2), counter, isEven, screen, scale)
        # if onScreen(midPoint(x1, x3), midPoint(y1, y3)) and onScreen(midPoint(x3, x2), midPoint(y3, y2)) and onScreen(x3, y3):
        sierpinski(midPoint(x1, x3), midPoint(y1, y3), midPoint(x3, x2), midPoint(y3, y2), x3, y3, counter, isEven, screen, scale)
        # pygame.display.flip()
        isEven *= -1
        return 0

cameraX = 0
cameraY = 0
scale = 1

# sierpinski(screenX/2, 0, 0, screenY, screenX, screenY, 0, True, screen, scale)

moveSpeed = -5
scaleSpeed = .05
while not doExit:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            doExit = True

    # cameraX += 1
    # scale += .01

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        cameraY -= moveSpeed
    if keys[pygame.K_a]:
        cameraX -= moveSpeed
    if keys[pygame.K_s]:
        cameraY += moveSpeed
    if keys[pygame.K_d]:
        cameraX += moveSpeed
    if keys[pygame.K_UP]:
        scale += scaleSpeed
    if keys[pygame.K_DOWN]:
        scale -= scaleSpeed
    
    screen.fill((0, 0, 0))
    sierpinski((screenX/2 + cameraX) * scale, (0 + cameraY) * scale, (0 + cameraX) * scale, (screenY + cameraY) * scale, (screenX + cameraX) * scale, (screenY + cameraY) * scale, 0, True, screen, scale)

    pygame.display.flip()
pygame.quit()