import pygame
from pygame.locals import *
import sys
import random

from OpenGL.GL import *
from OpenGL.GLU import *

# FramePerSec = pygame.time.Clock()



vertices = (
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
    (0.25, 0.5, 1), # B
    (1,0.5,0.25), # O
    (0.25,0.5,0.25), # G
    (1, 0.25, 0.2), # R
    (1,1,1), # W
    (1,0.75,0), # Y
)

def set_vertices(delta_x, delta_y, delta_z):

    new_vertices = []

    for vert in vertices:
        new_vert = []

        new_x = vert[0] + delta_x
        new_y = vert[1] + delta_y
        new_z = vert[2] + delta_z

        new_vert.append(new_x)
        new_vert.append(new_y)
        new_vert.append(new_z)

        new_vertices.append(new_vert)

    return new_vertices


def Cube(vertices):
  
    glLineWidth(5)
    glBegin(GL_LINES)
    glColor3fv((0,0,0))
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

    c_index = 0
    glBegin(GL_QUADS)
    for surface in surfaces:
        for vertex in surface:
            glColor3fv(colors[c_index])
            glVertex3fv(vertices[vertex])
        c_index += 1
    glEnd()



def main():
    pygame.init()
    display = (800,600)
    displaysurface = pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    pygame.display.set_caption("Rubik's Cube")

    max_distance = 100

    gluPerspective(45, (display[0]/display[1]), 0.1, max_distance)

    glTranslatef(0, 0, -20)

    cube_dict = {}

    for x in range(3):
        for y in range(3):
            for z in range(3):
                cube_dict[9*x+3*y+z] = set_vertices(2*(x-1), 2*(y-1), 2*(z-1))


    x_rot = 0
    y_rot = 0
    rotation_speed = 3


    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    pass
                if event.key == K_LEFT:
                    x_rot = -rotation_speed
                if event.key == K_RIGHT:
                    x_rot = rotation_speed
                if event.key == K_UP:
                    y_rot = -rotation_speed
                if event.key == K_DOWN:
                    y_rot = rotation_speed

            if event.type == KEYUP:
                if event.key == K_LEFT or event.key == K_RIGHT:
                    x_rot = 0
                if event.key == K_UP or event.key == K_DOWN:
                    y_rot = 0

        glRotatef(x_rot, 0.0, 1.0, 0.0)
        glRotatef(y_rot, 1.0, 0.0, 0.0)


        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        # Enable depth test
        glEnable(GL_DEPTH_TEST)
        # Accept fragment if it closer to the camera than the former one
        glDepthFunc(GL_LESS)

        for each_cube in cube_dict:
            Cube(cube_dict[each_cube])


        glLineWidth(1)
        glBegin(GL_LINES)
        glColor3fv((1,0,0))
        glVertex3fv((0, 0, 0))
        glVertex3fv((8, 0, 0))
        glColor3fv((0,1,0))
        glVertex3fv((0, 0, 0))
        glVertex3fv((0, 8, 0))
        glEnd()

  
        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    main()
    pygame.quit()
    quit()
