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
    for surface in surfaces:
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

    glTranslatef(0.0, 0.0, -40)
    # glRotatef(25, 2, 1, 0)

    object_passed = False

    print(object_passed)

    while not object_passed:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    glRotatef(1, 3, 1, 1)
                if event.key == K_LEFT:
                    glTranslatef(0.5, 0, 0)
                if event.key == K_RIGHT:
                    glTranslatef(-0.5, 0, 0)
                if event.key == K_UP:
                    glTranslatef(0, -1, 0)
                if event.key == K_DOWN:
                    glTranslatef(0, 1, 0)
            # if event.type == MOUSEBUTTONDOWN:
            #     if event.button == 4:
            #         glTranslatef(0, 0, 1.0)
            #     if event.button == 5:
            #         glTranslatef(0, 0, -1.0)

        x = glGetDoublev(GL_MODELVIEW_MATRIX)

        camera_z = x[3][2]

        if camera_z <= 0:
            object_passed = True

        # glRotatef(1, 3, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        glTranslatef(0, 0, 0.5)
       # Enable depth test
        glEnable(GL_DEPTH_TEST)
        # Accept fragment if it closer to the camera than the former one
        glDepthFunc(GL_LESS)
        
        Cube()
        # Cube_small()
        pygame.display.flip()
        pygame.time.wait(10)


if __name__ == "__main__":
    for x in range(10):
        main()
        glLoadIdentity() 
    pygame.quit()
    quit()