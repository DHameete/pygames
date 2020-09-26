import pygame
from pygame.locals import *
import sys

from OpenGL.GL import *
from OpenGL.GLU import *

# FramePerSec = pygame.time.Clock()



verticies = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1),
)

edges = (
    (0, 1),
    (0, 3),
    (0, 4),
    (2, 1),
    (2, 3),
    (2, 7),
    (6, 3),
    (6, 4),
    (6, 7),
    (5, 1),
    (5, 4),
    (5, 7),
)

surfaces = (
    (0,1,2,3),
    (7,6,3,2),
    (6,7,5,4),
    (4,5,1,0),
    (1,5,7,2),
    (4,0,3,6)
)

colors = (
    (1,0,0),
    (0,1,0),
    (0,0,1),
    (1,1,0),
    (1,0,1),
)


def Cube():
    glBegin(GL_QUADS)
    for surface in surfaces[0:2]:
        x = 1
        for vertex in surface:
            glColor3fv(colors[x])
            glVertex3fv(verticies[vertex])
            x += 1
    glEnd()


    glBegin(GL_LINES)
    glColor3fv(colors[0])
    for edge in edges:
        for vertex in edge:
            glVertex3fv(verticies[vertex])
    glEnd()


def Cube_small():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            v = tuple(x/2 for x in verticies[vertex])
            glVertex3fv(v)
    glEnd()


def main():
    pygame.init()
    display = (800,600)
    displaysurface = pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    pygame.display.set_caption("Rubik's Cube")

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

    glTranslatef(0.0, 0.0, -5)
    glRotatef(0, 0, 0, 0)

    while True:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    glRotatef(1, 3, 1, 1)
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        
        # glRotatef(1, 3, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        # Enable depth test
        glEnable(GL_DEPTH_TEST)
        # Accept fragment if it closer to the camera than the former one
        glDepthFunc(GL_LESS)
        
        Cube()
        # Cube_small()
        pygame.display.flip()
        pygame.time.wait(10)


if __name__ == "__main__":
    main()