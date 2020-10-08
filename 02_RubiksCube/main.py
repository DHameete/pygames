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


def set_vertices(max_distance, min_distance = -20, camera_x = 0, camera_y = 0):

    camera_x = -1 * int(camera_x)
    camera_y = -1 * int(camera_y)

    x_value_change = random.randrange(camera_x-75, camera_x+75)
    y_value_change = random.randrange(camera_y-75, camera_y+75)
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

    glTranslatef(0, 0, -40)

    x_move = 0
    y_move = 0

    cur_x = 0
    cur_y = 0

    game_speed = 2
    direction_speed = 2

    cube_dict = {}

    for x in range(75):
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
                    x_move = direction_speed
                if event.key == K_RIGHT:
                    x_move = -direction_speed
                if event.key == K_UP:
                    y_move = -direction_speed
                if event.key == K_DOWN:
                    y_move = direction_speed

            if event.type == KEYUP:
                if event.key == K_LEFT or event.key == K_RIGHT:
                    x_move = 0
                if event.key == K_UP or event.key == K_DOWN:
                    y_move = 0

        mdlview_matrx = glGetDoublev(GL_MODELVIEW_MATRIX)

        camera_z = mdlview_matrx[3][2]

        cur_x += x_move
        cur_y += y_move

        # if camera_z <= 0:
        #     object_passed = True

        # glRotatef(1, 3, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        glTranslatef(x_move, y_move, game_speed)
       # Enable depth test
        glEnable(GL_DEPTH_TEST)
        # Accept fragment if it closer to the camera than the former one
        glDepthFunc(GL_LESS)
        
        # ground()

        for each_cube in cube_dict:
            Cube(cube_dict[each_cube])


        for each_cube in cube_dict:
            if camera_z <= cube_dict[each_cube][0][2]:
                new_max = int(-1*(camera_z-(max_distance * 2)))

                cube_dict[each_cube] = set_vertices(new_max, int(camera_z-max_distance), cur_x, cur_y)

        # Cube_small()
        pygame.display.flip()
        # pygame.time.wait(10)


if __name__ == "__main__":
    main()
    glLoadIdentity() 
    pygame.quit()
    quit()