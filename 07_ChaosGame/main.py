import pygame
from pygame.locals import *
import sys, time, math
import random


width = 800
height = 600

WHITE = (255, 255, 255)
BLUE = (0, 255, 255)
ORANGE = (255, 128, 0)
YELLOW = (255, 255, 0)
GREEN = (128, 255, 0)
PURPLE = (255, 0, 255)

COLORS = [BLUE, ORANGE, YELLOW, GREEN, PURPLE]


def init_chaos():
    points = []

    for _ in range(2):
        x = random.randint(0, width)
        y = random.randint(0, height)
        points.append(pygame.Vector2(x,y))

    diff_vec = points[1] - points[0]
    diff_vec.rotate_ip(60)
    points.append(points[0] + diff_vec)
    
    if points[2].x < 0 or points[2].x > width or points[2].y < 0 or points[2].y > height:
        diff_vec.rotate_ip(-120)
        points[2] = points[0] + diff_vec

    return points


def init_chaos_mid(n):
    points = []

    r = random.randint(height/6, height/2)
    x_mid = random.randint(r, width - r)
    y_mid = random.randint(r, height - r)
    phi = random.randint(0,360)

    for _ in range(n):
        x = r * math.cos(phi * math.pi / 180) + x_mid
        y = r * math.sin(phi * math.pi / 180) + y_mid
        points.append(pygame.Vector2(x,y))

        phi += (360 / n)

    return points

def main():

    # setup
    pygame.init()
    display = (width, height)
    displaysurface = pygame.display.set_mode(display)
    pygame.display.set_caption("Chaos game")

    # Draw background
    displaysurface.fill((51, 51, 51))

    # Initialize shape 
    n = 5
    points = init_chaos_mid(n)

    # Initialize starting position
    x_pos = random.randint(0, width)
    y_pos = random.randint(0, height)
    pos = pygame.Vector2(x_pos, y_pos)
    
    clr = BLUE
    now = time.time()

    prevprev = 0
    prev = 0
    a = prev

    # Font
    font = pygame.font.SysFont('Arial', 25)
     
    # button 1
    button1 = pygame.Rect(100,height-50,100,25)
    text1 = font.render('Triangle!', True, (0,0,0))
    text_rect1 = text1.get_rect(center=button1.center)

    # button 2
    button2 = pygame.Rect(250,height-50,100,25)
    text2 = font.render('Square!', True, (0,0,0))
    text_rect2 = text2.get_rect(center=button2.center)

    # button 3
    button3 = pygame.Rect(400,height-50,100,25)
    text3 = font.render('Star!', True, (0,0,0))
    text_rect3 = text3.get_rect(center=button3.center)

    # loop
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                return False

            # if event.type == KEYDOWN:
            #     points = init_chaos_mid()
            #     displaysurface.fill((51, 51, 51))
            #     now = time.time()

            if event.type == MOUSEBUTTONDOWN:
                mouse_pos = event.pos

                if button1.collidepoint(mouse_pos):
                    n = 3
                    points = init_chaos_mid(n)
                    displaysurface.fill((51, 51, 51))
                    now = time.time() 

                if button2.collidepoint(mouse_pos):
                    n = 4
                    points = init_chaos_mid(n)
                    displaysurface.fill((51, 51, 51))
                    now = time.time() 

                if button3.collidepoint(mouse_pos):
                    n = 5
                    points = init_chaos_mid(n)
                    displaysurface.fill((51, 51, 51))
                    now = time.time() 

        # Keep track of time
        if time.time() - now > 3:
            points = init_chaos_mid(n)
            displaysurface.fill((51, 51, 51))
            now = time.time() 

        # Draw points
        for point in points:
            pygame.draw.circle(displaysurface, WHITE, point, 3)

        # Draw new set of points
        for _ in range(100):

            a = random.choice(range(len(points)))
            if n == 3:
                a = random.choice(range(len(points)))
            elif n == 4:
                while a == prev:
                    a = random.choice(range(len(points)))
            elif n == 5:
                while (a == (prev+1)%n or a == (prev-1)%n) and (prev == prevprev):
                    a = random.choice(range(len(points)))
        

            pos = pos.lerp(points[a],0.5)
            clr = COLORS[a]

            pygame.draw.circle(displaysurface, clr, pos, 1)

            prevprev = prev
            prev = a

        pygame.draw.rect(displaysurface, (205, 205, 0), button1)
        displaysurface.blit(text1, text_rect1)

        pygame.draw.rect(displaysurface, (205, 205, 0), button2)
        displaysurface.blit(text2, text_rect2)

        pygame.draw.rect(displaysurface, (205, 205, 0), button3)
        displaysurface.blit(text3, text_rect3)

        # Update display
        pygame.display.update()

if __name__ == "__main__":
    main()
    pygame.quit()
    sys.exit()
