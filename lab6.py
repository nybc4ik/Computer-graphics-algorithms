import pygame
import sys
from OpenGL.GL import *
from OpenGL.GLU import *
x=0
y=0
vx=0.001
vy=-0.002
vertices = (
    # x  y  z
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
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
    (5, 7)
)


def loadTexture():
    textureSurface = pygame.image.load('browser_NjYzkBq2nq.png')
    textureData = pygame.image.tostring(textureSurface, "RGBA", 1)
    width = textureSurface.get_width()
    height = textureSurface.get_height()

    glEnable(GL_TEXTURE_2D)
    texid = glGenTextures(1)

    glBindTexture(GL_TEXTURE_2D, texid)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, width, height,
                 0, GL_RGBA, GL_UNSIGNED_BYTE, textureData)

    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)

    return texid


def draw_cube(lines=False):
    global x
    global vx
    global vy
    global y
    if lines:
        glBegin(GL_LINES)
        for edge in edges:
            glColor3fv((1, 1, 1))
            for vertex in edge:
                glVertex3fv(vertices[vertex])
        glEnd()
    else:
        glBegin(GL_QUADS)
        glTexCoord2f(0.0, 0.0)
        glVertex3f(x-1.0, y-1.0,  1.0)
        glTexCoord2f(1.0, 0.0)
        glVertex3f(x+1.0, y-1.0,  1.0)
        glTexCoord2f(1.0, 1.0)
        glVertex3f(x+1.0,  y+1.0,  1.0)
        glTexCoord2f(0.0, 1.0)
        glVertex3f(x-1.0,  y+1.0,  1.0)
        glTexCoord2f(1.0, 0.0)
        glVertex3f(x-1.0, y-1.0, -1.0)
        glTexCoord2f(1.0, 1.0)
        glVertex3f(x-1.0,  y+1.0, -1.0)
        glTexCoord2f(0.0, 1.0)
        glVertex3f(x+1.0, y+1.0, -1.0)
        glTexCoord2f(0.0, 0.0)
        glVertex3f(x+1.0, y-1.0, -1.0)
        glTexCoord2f(0.0, 1.0)
        glVertex3f(x-1.0,  y+1.0, -1.0)
        glTexCoord2f(0.0, 0.0)
        glVertex3f(x-1.0,  y+1.0,  1.0)
        glTexCoord2f(1.0, 0.0)
        glVertex3f(x+1.0,  y+1.0,  1.0)
        glTexCoord2f(1.0, 1.0)
        glVertex3f(x+1.0,  y+1.0, -1.0)
        glTexCoord2f(1.0, 1.0)
        glVertex3f(x-1.0, y-1.0, -1.0)
        glTexCoord2f(0.0, 1.0)
        glVertex3f(x+1.0, y-1.0, -1.0)
        glTexCoord2f(0.0, 0.0)
        glVertex3f(x+1.0, y-1.0,  1.0)
        glTexCoord2f(1.0, 0.0)
        glVertex3f(x-1.0, y-1.0,  1.0)
        glTexCoord2f(1.0, 0.0)
        glVertex3f(x+1.0, y-1.0, -1.0)
        glTexCoord2f(1.0, 1.0)
        glVertex3f(x+1.0,  y+1.0, -1.0)
        glTexCoord2f(0.0, 1.0)
        glVertex3f(x+1.0,  y+1.0,  1.0)
        glTexCoord2f(0.0, 0.0)
        glVertex3f(x+1.0, y-1.0,  1.0)
        glTexCoord2f(0.0, 0.0)
        glVertex3f(x-1.0, y-1.0, -1.0)
        glTexCoord2f(1.0, 0.0)
        glVertex3f(x-1.0, y-1.0,  1.0)
        glTexCoord2f(1.0, 1.0)
        glVertex3f(x-1.0,  y+1.0,  1.0)
        glTexCoord2f(0.0, 1.0)
        glVertex3f(x-1.0,  y+1.0, -1.0)
        glEnd()
    x+=vx
    y+=vy
    if x>=1 or x<=-1:
        vx=-vx
    if y>=1 or y<=-1:
        vy=-vy
pygame.init()
display = (1920, 1080)
display = (1920, 1080)
screen = pygame.display.set_mode(
    display, pygame.DOUBLEBUF | pygame.OPENGL | pygame.OPENGLBLIT)

loadTexture()

gluPerspective(45, display[0] / display[1], 0.1, 50.0)
glTranslatef(0.0, 0.0, -5)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    draw_cube(lines=False)

    pygame.display.flip()