from OpenGL.GL import *
import glfw
import math

angle = 0.0
ang=0.0
seen=0

def main():
    if not glfw.init():
        return
    window = glfw.create_window(640, 640, "Lab3", None, None)
    if not window:
        glfw.terminate()
        return
    glfw.make_context_current(window)
    glfw.set_key_callback(window, key_callback)
    while not glfw.window_should_close(window):
        display(window)
    glfw.destroy_window(window)
    glfw.terminate()

def Prizm(n, ang):
    g=360/n
    angle=math.radians(g)
    vertex=[0]*(2*n*3)
    # вершины 
    for i in range(n):
        vertex[i*3]=math.cos(angle*i)*0.5
        vertex[i*3+1]=math.sin(angle*i)*0.5
        vertex[i*3+2]=-0.5
    for i in range(n):
        vertex[(i+n)*3]=math.cos(angle*i+ang)*0.25
        vertex[(i+n)*3+1]=math.sin(angle*i+ang)*0.25
        vertex[(i+n)*3+2]=0.5
    #грани
    for i in range(n):
        glBegin(GL_LINES)
        tup=(vertex[i*3], vertex[i*3+1], vertex[i*3+2])
        glVertex3fv(tup)
        tup=(vertex[(i+n)*3], vertex[(i+n)*3+1], vertex[(i+n)*3+2])
        glVertex3fv(tup)
        glEnd()
    for i in range(n-1):
        glBegin(GL_LINES)
        tup=(vertex[i*3], vertex[i*3+1], vertex[i*3+2])
        glVertex3fv(tup)
        tup=(vertex[(i+1)*3], vertex[(i+1)*3+1], vertex[(i+1)*3+2])
        glVertex3fv(tup)
        glEnd()
    for i in range(n-1):
        glBegin(GL_LINES)
        tup=(vertex[(i+n+1)*3], vertex[(i+n+1)*3+1], vertex[(i+n+1)*3+2])
        glVertex3fv(tup)
        tup=(vertex[(i+n)*3], vertex[(i+n)*3+1], vertex[(i+n)*3+2])
        glVertex3fv(tup)
        glEnd()
    glBegin(GL_LINES)
    tup=(vertex[(n-1)*3], vertex[(n-1)*3+1], vertex[(n-1)*3+2])
    glVertex3fv(tup)
    tup=(vertex[0], vertex[1], vertex[2])
    glVertex3fv(tup)
    tup=(vertex[(2*n-1)*3], vertex[(2*n-1)*3+1], vertex[(2*n-1)*3+2])
    glVertex3fv(tup)
    tup=(vertex[(n)*3], vertex[(n)*3+1], vertex[(n)*3+2])
    glVertex3fv(tup)
    glEnd()
    

def display(window):
    global seen
    global angle
    global angle1
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
    
    glClearColor(1.0, 1.0, 1.0, 1.0)
    glPushMatrix()
    glRotatef(angle, 1, 1, 1)

    glColor3f(1.0,0.5,1.0)
    
    Prizm(4, ang)
    
    #Cube(vertices, edges)
    glPopMatrix()
    glfw.swap_buffers(window)
    glfw.poll_events()

def key_callback(window, key, scancode, action, mods):
    global seen
    global angle
    global ang
    if action == glfw.PRESS:
        if key == glfw.KEY_RIGHT:
            angle += 10
        if key == 263: # glfw.KEY_LEFT
            angle -= 1
        if key == glfw.KEY_SPACE: 
            if seen==0:
                seen=1
            else:
                seen=0
        if key == glfw.KEY_UP: 
            ang += 1
        if key == glfw.KEY_DOWN: 
            ang -= 1

main()

