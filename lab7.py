import pygame
from pygame.locals import *
import time
from OpenGL.GL import *
from OpenGL.GLU import *

start_time = time.time()

x, y = 0, 0
vx, vy = 0.01, 0.06

surfaces = (
    (0, 1, 2, 3),
    (3, 2, 7, 6),
    (6, 7, 5, 4),
    (4, 5, 1, 0),
    (1, 5, 7, 2),
    (4, 0, 3, 6),
)

normals = [
    (0, 0, -1),
    (-1, 0, 0),
    (0, 0, 1),
    (1, 0, 0),
    (0, 1, 0),
    (0, -1, 0)
]

colors = (
    (1, 1, 1),
    (0, 1, 0),
    (0, 0, 1),
    (0, 1, 0),
    (0, 0, 1),
    (1, 0, 1),
    (0, 1, 0),
    (1, 0, 1),
    (0, 1, 0),
    (0, 0, 1),
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


def cube():
    global x, y
    glBegin(GL_QUADS)
    verticies = (
        (x + 1, y - 1, -1),
        (x + 1, y + 1, -1),
        (x - 1, y + 1, -1),
        (x - 1, y - 1, -1),
        (x + 1, y - 1, 1),
        (x + 1, y + 1, 1),
        (x - 1, y - 1, 1),
        (x - 1, y + 1, 1),
    )
    for i_surface, surface in enumerate(surfaces):
        n = 0
        glNormal3fv(normals[i_surface])
        for vertex in surface:
            n += 1
            glColor3fv(colors[n])
            glVertex3fv(verticies[vertex])
    glEnd()

    glColor3fv(colors[0])
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(verticies[vertex])
    glEnd()


def main():
    checkpoint = 0

    lol = 1
    for kek in range(0, 10 ** 7):
        lol += kek
    print("proverka ", lol)

    global surfaces
    global x, y, vx, vy
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    clock = pygame.time.Clock()

    glMatrixMode(GL_PROJECTION)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)

    glMatrixMode(GL_MODELVIEW)
    glTranslatef(0, 0, -5)

    # источники света

    glLight(GL_LIGHT0, GL_POSITION, (5, 5, 5, 1))  # позиции света справа, сверху, со стороны наблюдателя
    glLightfv(GL_LIGHT0, GL_AMBIENT, (0, 0, 0, 1))
    glLightfv(GL_LIGHT0, GL_DIFFUSE, (1, 1, 1, 1))

    glEnable(GL_DEPTH_TEST)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)
        glEnable(GL_COLOR_MATERIAL)
        glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)

        glRotatef(1, 3, 1, 1)
        cube()
        x += vx
        y += vy
        if x >= 1 or x <= -1:
            vx = -vx
        if y >= 1 or y <= -1:
            vy = -vy
        glDisable(GL_LIGHT0)
        glDisable(GL_LIGHTING)
        glDisable(GL_COLOR_MATERIAL)

        pygame.display.flip()
        clock.tick(60)

        if checkpoint == 0:  # чекпоинт чтобы время писалось всего один раз а не кучу :)
            print("--- %s seconds ---" % (time.time() - start_time))
            checkpoint += 1


main()
