from OpenGL.GL import *
import glfw
import math

delta = 0.0
angle = 0.0
angle1 = 0.0
posx = 0.0
posy = 0.0
posz = 0.0
size = 0.0
r=0.173205080757
run=0
seen=0

edges = (
    (0,1),
    (0,3),
    (0,4),
    (2,1),
    (2,3),
    (2,7),
    (6,3),
    (6,4),
    (6,7),
    (5,1),
    (5,4),
    (5,7)
)

grani =(
    [0,1,2,3],
    [4,5,7,6],
    [0,1,5,4],
    [2,3,6,7],
    [1,2,7,5],
    [0,3,6,4]
)

vertices= (
    (0.1, -0.1, -0.1),
    (0.1, 0.1, -0.1),
    (-0.1, 0.1, -0.1),
    (-0.1, -0.1, -0.1),
    (0.1, -0.1, 0.1),
    (0.1, 0.1, 0.1),
    (-0.1, -0.1, 0.1),
    (-0.1, 0.1, 0.1)
)
vertices1= (
    (0.6, 0.6-r, 0.6-r),
    (0.6+r, 0.6, 0.6),
    (0.6, 0.6+r, 0.6+r),
    (0.6-r, 0.6, 0.6),
    (0.6, 0.6-r, 0.6+r),
    (0.6+r, 0.6, 0.6+2*r),
    (0.6-r, 0.6, 0.6+2*r),
    (0.6, 0.6+r, 0.6+3*r)
)
def main():
    if not glfw.init():
        return
    window = glfw.create_window(640, 640, "Lab2", None, None)
    if not window:
        glfw.terminate()
        return
    glfw.make_context_current(window)
    glfw.set_key_callback(window, key_callback)
    glfw.set_scroll_callback(window, scroll_callback)
    while not glfw.window_should_close(window):
        display(window)
    glfw.destroy_window(window)
    glfw.terminate()

def CubeSeen(vertices, grani):
    glBegin(GL_QUADS)
    for gr in grani:
        for vertex in gr:
            glColor3f(1.0,0.5,1.0)
            glVertex3fv(vertices[vertex])
    glEnd()

def CubeSeen1(vertices, grani):
    glBegin(GL_QUADS)
    for gr in grani:
        for vertex in gr:
            glColor3f(0.0,1.0,1.0)
            glVertex3fv(vertices[vertex])
    glEnd()


def Cube(vertices, edges):
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glColor3f(1.0,0.5,1.0)
            glVertex3fv(vertices[vertex])
    glEnd()

def Cube1(vertices, edges):
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glColor3f(0.0,1.0,1.0)
            glVertex3fv(vertices[vertex])
    glEnd()

def display(window):
    global run
    global seen
    global angle
    global angle1
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
    
    glClearColor(1.0, 1.0, 1.0, 1.0)
    glPushMatrix()
    #glRotatef(angle, 1, 1, 1)
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glEnable(GL_DEPTH_TEST)
    if seen==0:
        Cube1(vertices1, edges)
    else:
        CubeSeen1(vertices1, grani)

    glMatrixMode(GL_MODELVIEW)
    c=math.cos(angle)
    s=math.sin(angle)
    oz=[c, s, 0, 0, -s, c, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1]
    glMultMatrixd(oz)
    c=math.cos(angle1)
    s=math.sin(angle1)
    ox=[1, 0,0,0,0,c,s,0,0,-s,c,0,0,0,0,1]
    glMultMatrixd(ox)
    #oy=[c,0,-s,0,0,1,0,0,s,0,c,0,0,0,0,1]
    #glMultMatrixd(oy)

    
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glPushMatrix()
    ct=0.81654081188
    st=0.57728771208
    cf=0.70710678118
    sf=0.70710678118
    m=[cf, sf*st, sf*ct, 0, 0, ct, -st, 0, sf, -cf*st, -cf*ct, 0, 0, 0, 0, 1]
    glMultMatrixd(m)

    if seen==0:
        Cube(vertices, edges)
    else:
        CubeSeen(vertices, grani)
    glPopMatrix()
    glMatrixMode(GL_MODELVIEW)
    run=1
    
    #Cube(vertices, edges)
    glPopMatrix()
    angle += delta
    glfw.swap_buffers(window)
    glfw.poll_events()

def key_callback(window, key, scancode, action, mods):
    global delta
    global seen
    global deltax
    global angle
    global angle1
    global posy
    if action == glfw.PRESS:
        if key == glfw.KEY_RIGHT:
            angle += 0.1
        if key == 263: # glfw.KEY_LEFT
            angle -= 0.1
        if key == glfw.KEY_SPACE: 
            if seen==0:
                seen=1
            else:
                seen=0
        if key == glfw.KEY_UP: 
            angle1 += 0.1
        if key == glfw.KEY_DOWN: 
            angle1 -= 0.1

def scroll_callback(window, xoffset, yoffset):
    global size
    if (xoffset > 0):
        size -= yoffset/10
    else:
        size += yoffset/10

main()

