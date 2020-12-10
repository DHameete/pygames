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

COLORS = [BLUE, ORANGE, YELLOW]


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
    button = pygame.Rect(100,height-50,100,25)
    text = font.render('Hello!', True, (0,0,0))
    text_rect = text.get_rect(center=button.center)

    # loop
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                return False

            if event.type == KEYDOWN:
                points = init_chaos_mid()
                displaysurface.fill((51, 51, 51))
                now = time.time()

            if event.type == MOUSEBUTTONDOWN:
                mouse_pos = event.pos

                if button.collidepoint(mouse_pos):
                    n = 3
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
            # while a == (prev+1)%n or a == (prev-1)%n:
            #     a = random.choice(range(len(points)))
            # while a == (prev+1)%n or a == (prev-1)%n:
            #     a = random.choice(range(len(points)))
            elif n == 5:
                while (a == (prev+1)%n or a == (prev-1)%n) and (prev == prevprev):
                    a = random.choice(range(len(points)))
        

            pos = pos.lerp(points[a],0.5)
            # clr = COLORS[a % 3]

            pygame.draw.circle(displaysurface, clr, pos, 1)

            prevprev = prev
            prev = a

        pygame.draw.rect(displaysurface, (205, 205, 0), button)
        displaysurface.blit(text, text_rect)

        # Update display
        pygame.display.update()

if __name__ == "__main__":
    main()
    pygame.quit()
    sys.exit()
