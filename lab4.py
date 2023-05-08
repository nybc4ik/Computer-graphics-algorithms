from OpenGL.GL import *
import glfw

n=500
pix = [255] * n * n * 3
edges = []
closed = 0


def main():
    if not glfw.init():
        return
    window = glfw.create_window(n, n, "Lab4", None, None)
    if not window:
        glfw.terminate()
        return
    glfw.make_context_current(window)
    glfw.set_key_callback(window, key_callback)
    glfw.set_cursor_pos_callback(window, mouse)
    while not glfw.window_should_close(window):
        display(window)
    glfw.destroy_window(window)
    glfw.terminate()

#рисуем линии
def drawLine(x1, y1, x2, y2):
    global pix
    if y1 == y2:
        for i in range(min(x1, x2), max(x1, x2)):
            pix[(y1*n+i)*3] = 0
            pix[(y1 * n + i) * 3+1] = 0
            pix[(y1 * n + i) * 3+2] = 0
        return
    if x1 == x2:
        for i in range(min(y1, y2), max(y1, y2)):
            pix[(i*n + x1)*3] = 0
            pix[(i * n + x1) * 3+1] = 0
            pix[(i * n + x1) * 3+2] = 0
        return
    dy = abs(y1 - y2)
    dx = abs(x1 - x2)
    if dx > dy:
        e = 0
        m = dy
        if x1>x2:
            x2,x1=x1,x2
            y1,y2=y2,y1
        x = x1
        y = y1
        for i in range(x1, x2):
            if e!=0:
                c=int(255*dx/e)
                c=255-c
                if c==255:
                    c=254
            else:
                c=0
            pix[(y*n + x)*3] = c
            pix[(y * n + x) * 3+1] = c
            pix[(y * n + x) * 3+2] = c
            e += m
            x += 1
            if e >= dx:
                if y1 < y2:
                    y += 1
                else:
                    y -= 1
                e -= dx
    else:
        e = 0
        m = dx
        if y1>y2:
            x2,x1=x1,x2
            y1,y2=y2,y1
        y = y1
        x = x1
        for i in range(y1, y2):
            if e!=0:
                c=int(255*dy/e)
                c=255-c
            else:
                c=0
            pix[(y*n + x)*3] = c
            pix[(y * n + x) * 3+1] = c
            pix[(y* n + x) * 3+2] = c
            e += m
            y += 1
            if e >= dy:
                if x1 < x2:
                    x += 1
                else:
                    x -= 1
                e -= dy

#заполнение
def fill():
    global n
    m=1 #маркер
    # 1 - закрас в первый раз 2 закрас во второй раз
    # после первого добавляется один, и начинается закрас территорий
    # после второго удаляется один
    for y in range (n):
        for x in range (n):
            if  pix[(y*n + x)*3] != 255: #(проверка назакрас)
                if m==1: #(проверка маркера)
                    m += 1
                else:
                    m -= 1
            else:
                if m==2: #проверка маркера
                   pix[(y*n + x)*3] = 0 #закрас
                   pix[(y * n + x) * 3+1] = 0
                   pix[(y* n + x) * 3+2] = 0
        m=1


def display(window):
    global pix
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()

    glClearColor(1.0, 1.0, 1.0, 1.0)
    glPushMatrix()
    glDrawPixels(n, n, GL_RGB, GL_UNSIGNED_BYTE, pix)
    glPopMatrix()
    glfw.swap_buffers(window)
    glfw.poll_events()



def key_callback(window, key, scancode, action, mods):
    global closed
    global edges
    global pix
    if action == glfw.PRESS:
        if key == glfw.KEY_SPACE:
            if closed == 0:
                closed=1
                drawLine(edges[0], (n - edges[1]), edges[len(edges) - 2], (n - edges[len(edges) - 1]))
                fill()
            elif closed == 1:
                closed=2
            elif closed == 2:
                closed=1
        if key == glfw.KEY_UP:
            pix=[255]*n*n*3
            edges=[]
            closed=0


def mouse(window, x, y):
    global edges
    global closed
    if glfw.PRESS:
        edges.append(int(x))
        edges.append(int(y))
        if (len(edges)//2>=2) and (closed==0):
            print(x,y)
            drawLine(edges[len(edges)-2], (n - edges[len(edges)-1]), edges[len(edges)-4], (n - edges[len(edges)-3]))

main()
