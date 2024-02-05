import pygame
import random
pygame.init()
screenX = 1920
screenY = 1080
screen = pygame.display.set_mode((screenX, screenY))
doExit = False

# https://docs.google.com/presentation/d/1_9vaR8Gl3kL8IgQ9PZxdM65N26y-_QPE6OMWVh0LTdU/edit#slide=id.g2675e1715c5_0_20

def midPoint(num1, num2):
    return(num1 + (num2 - num1)/2)

def sierpinski(x1, y1, x2, y2, x3, y3, counter, isEven, screen):
    counter += 1
    if counter < 12:
        if isEven:
            r = random.randint(0, 255)#(counter * 100) % 255
            g = random.randint(0, 50)
            b = random.randint(0, 155)
            color = (r, g, b)
            # baseColor = 255
            # color = (baseColor, baseColor, baseColor)
            
            # pygame.draw.polygon(screen, color, ((x1, y1), (x2, y2), (x3, y3)))
            pygame.draw.line(screen, color, (x1, y1), (x2, y2))
            pygame.draw.line(screen, color, (x2, y2), (x3, y3))
            pygame.draw.line(screen, color, (x3, y3), (x1, y1))
        else:
            pass #no point in drawing something that won't show up so just don't draw it.

        sierpinski(x1, y1, midPoint(x1, x2), midPoint(y1, y2), midPoint(x3, x1), midPoint(y3, y1), counter, isEven, screen)
        sierpinski(midPoint(x1, x2), midPoint(y1, y2), x2, y2, midPoint(x3, x2), midPoint(y3, y2), counter, isEven, screen)
        sierpinski(midPoint(x1, x3), midPoint(y1, y3), midPoint(x3, x2), midPoint(y3, y2), x3, y3, counter, isEven, screen)
        pygame.display.flip()
        isEven *= -1
        return 0

sierpinski(screenX/2, 0, 0, screenY, screenX, screenY, 0, True, screen)

while not doExit:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            doExit = True    
    pygame.display.flip()
pygame.quit()