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
    (1,0,0),
    (0,1,0),
    (0,0,1),
    (1,1,0),
    (1,0,1),
)

ground_vertices = (
    (-10, -1.1, 20),
    (10, -1.1, 20),
    (-10, -1.1, -300),
    (10, -1.1, -300),
)

def ground():
    glBegin(GL_QUADS)
    for vertex in ground_vertices:
        glColor3fv((0, 0.5, 0.5))
        glVertex3fv(vertex)

    glEnd()


def set_vertices(max_distance, min_distance = -20):
    x_value_change = random.randrange(-10,10)
    y_value_change = random.randrange(-10,10)
    z_value_change = random.randrange(-1*max_distance, min_distance)

    new_vertices = []

    for vert in vertices:
        new_vert = []

        new_x = vert[0] + x_value_change
        new_y = vert[1] + y_value_change
        new_z = vert[2] + z_value_change

        new_vert.append(new_x)
        new_vert.append(new_y)
        new_vert.append(new_z)

        new_vertices.append(new_vert)

    return new_vertices


def Cube(vertices):
    glBegin(GL_QUADS)
    for surface in surfaces:
        x = 1
        for vertex in surface:
            glColor3fv(colors[x])
            glVertex3fv(vertices[vertex])
            x += 1
    glEnd()


    glBegin(GL_LINES)
    glColor3fv(colors[0])
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()


def Cube_small():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            v = tuple(x/2 for x in vertices[vertex])
            glVertex3fv(v)
    glEnd()


def main():
    pygame.init()
    display = (800,600)
    displaysurface = pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    pygame.display.set_caption("Rubik's Cube")

    max_distance = 100

    gluPerspective(45, (display[0]/display[1]), 0.1, max_distance)

    glTranslatef(random.randrange(-5,5),random.randrange(-5,5), -40)
    # glRotatef(25, 2, 1, 0)

    # object_passed = False

    x_move = 0
    y_move = 0

    cube_dict = {}

    for x in range(20):
        cube_dict[x] = set_vertices(max_distance)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    glRotatef(10, 1, 1, 1)
                if event.key == K_LEFT:
                    x_move = 0.3
                if event.key == K_RIGHT:
                    x_move = -0.3
                if event.key == K_UP:
                    y_move = -0.3
                if event.key == K_DOWN:
                    y_move = 0.3

            if event.type == KEYUP:
                if event.key == K_LEFT or event.key == K_RIGHT:
                    x_move = 0
                if event.key == K_UP or event.key == K_DOWN:
                    y_move = 0

        mdlview_matrx = glGetDoublev(GL_MODELVIEW_MATRIX)

        camera_z = mdlview_matrx[3][2]

        # if camera_z <= 0:
        #     object_passed = True

        # glRotatef(1, 3, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        glTranslatef(x_move, y_move, 0.5)
       # Enable depth test
        glEnable(GL_DEPTH_TEST)
        # Accept fragment if it closer to the camera than the former one
        glDepthFunc(GL_LESS)
        
        # ground()

        for each_cube in cube_dict:
            Cube(cube_dict[each_cube])


        for each_cube in cube_dict:
            if camera_z <= cube_dict[each_cube][0][2]:
                new_max = int(-1*(camera_z-max_distance))

                cube_dict[each_cube] = set_vertices(new_max, int(camera_z))

        # Cube_small()
        pygame.display.flip()
        pygame.time.wait(10)


if __name__ == "__main__":
    main()
    glLoadIdentity() 
    pygame.quit()
    quit()