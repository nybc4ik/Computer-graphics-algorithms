from OpenGL.GL import *
import glfw

points = [[1, 0, -1, 1], [0.4, 1, 0.4, 0.6], [0.4, 0.25, 0.25, 0.25]]

marker = 0
n = 640
pix = [255] * n * n * 3
cutingEdges = [
    (0.0, 0.0),
    (0.5, 0.0),
    (0.5, 0.5),
    (0.0, 0.5),
    ]
figureEdges = []
newEdges = []

def main():
    global points
    if not glfw.init():
        return
    window = glfw.create_window(n, n, "Lab5", None, None)
    if not window:
        glfw.terminate()
        return
    glfw.make_context_current(window)
    glfw.set_key_callback(window, key_callback)
    while not glfw.window_should_close(window):
        display(window)
    glfw.destroy_window(window)
    glfw.terminate()

def intersection(x1, y1, x2, y2, x3, y3, x4, y4):
    # Вычисление коэффициентов уравнений в общем виде
    A1 = y2 - y1
    B1 = x1 - x2
    C1 = x2 * y1 - x1 * y2

    A2 = y4 - y3
    B2 = x3 - x4
    C2 = x4 * y3 - x3 * y4

    # Решение системы уравнений
    det = A1 * B2 - A2 * B1
    if det == 0:
        print("Прямые параллельные ты ошибся приятель :)")
        return 0
    else:
        Point1 = (B1 * C2 - B2 * C1) / det
        Point2 = (A2 * C1 - A1 * C2) / det
        return(Point1, Point2)


def crash(x1, y1, x2, y2):
    global Point5
    num1 = 0
    if x1 < 0:
        num1 += 1
    if x1 > 0.5:
        num1 += 100
    if y1 > 0.5:
        num1 += 10
    if y1 < 0:
        num1 += 1000

    num2 = 0
    if x2 < 0:
        num2 += 1
    if x2 > 0.5:
        num2 += 100
    if y2 > 0.5:
        num2 += 10
    if y2 < 0:
        num2 += 1000


    if num1 == 0 and num2 == 0:  # линия вся лежит в центре её удаляем
        # оно лежит в центре удаляем его!!!
        # print("удаляем линию!")
        # print(num1, num2)

        glBegin(GL_LINES)
        glColor3d(0, 0, 0)
        glVertex3d(x1, y1, 0)
        glVertex3d(x2, y2, 0)
        glEnd()
        return 0
    if num1 == num2:  # линия вся не лежит в центре её не удаляем и не пересекает отсекатель
        # print("не удаляем линию!")
        # print(num1, num2)
        return 0
    # проверка не тривиальных случаев
    # если две точки лежат вне отсекателя
    while (num1 != 0 and num2 != 0) or (num1 != num2):
        # выбор начальной точки (которая лежит вне окна)
        if num1 != 0:  # Если первый конец не лежит в центр...- то мы должны укротить по его часть
            if num1 == 1 or num1 == 11 or num1 == 1001:  # слева так же верхний левый угол и нижний левый угол
                # где Ax и Bx координаты стороны пересекающей прямую
                Ax = 0
                Ay = 0.5
                Bx = 0
                By = 0
            elif num1 == 10 or num1 == 110:  # вверх так же верхний правый угол
                # где Ax1 и Bx2 координаты стороны пересекающей прямую
                Ax = 0
                Ay = 0.5
                Bx = 0.5
                By = 0.5
            elif num1 == 100 or num1 == 1100:  # право так же нижний правый угол
                # где Ax1 и Bx2 координаты стороны пересекающей прямую
                Ax = 0.5
                Ay = 0
                Bx = 0.5
                By = 0.5
            elif num1 == 1000:  # нижняя грань!
                # где Ax1 и Bx2 координаты стороны пересекающей прямую
                Ax = 0
                Ay = 0
                Bx = 0.5
                By = 0
            else:
                print("Ты наверное перепутал или что-то пошло не так.... в общем земля тебе пухом ....")
            Point3, Point4 = intersection(Ax, Ay, Bx, By, x1, y1, x2, y2)
            if num2 != 0:  # Если второй конец не лежит в центр... -то мы должны укротить по его часть
                if num2 == 1 or num2 == 11 or num2 == 1001:  # слева так же верхний левый угол и нижний левый угол
                    # где Ax и Bx координаты стороны пересекающей прямую
                    Ax = 0
                    Ay = 0.5
                    Bx = 0
                    By = 0
                elif num2 == 10 or num2 == 110:  # вверх так же верхний правый угол
                    # где Ax1 и Bx2 координаты стороны пересекающей прямую
                    Ax = 0
                    Ay = 0.5
                    Bx = 0.5
                    By = 0.5
                elif num2 == 100 or num2 == 1100:  # право так же нижний правый угол
                    # где Ax1 и Bx2 координаты стороны пересекающей прямую
                    Ax = 0.5
                    Ay = 0
                    Bx = 0.5
                    By = 0.5
                elif num2 == 1000:  # нижняя грань!
                    # где Ax1 и Bx2 координаты стороны пересекающей прямую
                    Ax = 0
                    Ay = 0
                    Bx = 0.5
                    By = 0
                else:
                    print("Ты наверное перепутал или что-то пошло не так.... в общем земля тебе пухом ....")
            Point5, Point6 = intersection(Ax, Ay, Bx, By, x1, y1, x2, y2)

            glBegin(GL_LINES)
            glColor3d(0, 0, 0)
            glVertex3d(Point3, Point4, 0)
            glVertex3d(Point5, Point6, 0)
            glEnd()
            return 0

        # если одна точка лежит внутри отсекателя, а вторая где-то снаружи
        # ситуация когда первая точка внутри

    if (x1 >= 0) and (x1 <= 0.5) and (y1 >= 0) and (y1 <= 0.5):
        # print("check")
        if num2 != 0:  # Если второй конец не лежит в центр... -то мы должны укротить по его часть
            if num2 == 1 or num2 == 11 or num2 == 1001:  # слева так же верхний левый угол и нижний левый угол
                    # где Ax и Bx координаты стороны пересекающей прямую
                Ax = 0
                Ay = 0.5
                Bx = 0
                By = 0
            elif num2 == 10 or num2 == 110:  # вверх так же верхний правый угол
                    # где Ax1 и Bx2 координаты стороны пересекающей прямую
                Ax = 0
                Ay = 0.5
                Bx = 0.5
                By = 0.5
            elif num2 == 100 or num2 == 1100:  # право так же нижний правый угол
                    # где Ax1 и Bx2 координаты стороны пересекающей прямую
                Ax = 0.5
                Ay = 0
                Bx = 0.5
                By = 0.5
            elif num2 == 1000:  # нижняя грань!
                    # где Ax1 и Bx2 координаты стороны пересекающей прямую
                Ax = 0
                Ay = 0
                Bx = 0.5
                By = 0
            else:
                print("Ты наверное перепутал или что-то пошло не    так.... в общем земля тебе пухом ....")
            Point5, Point6 = intersection(Ax, Ay, Bx, By, x1, y1, x2, y2)
            glBegin(GL_LINES)
            glColor3d(0, 0, 0)
            glVertex3d(Point5, Point6, 0)
            glVertex3d(x1, y1, 0)
            glEnd()
            return 0

        # ситуация когда вторая точка внутри
    if (x2 >= 0) and (x2 <= 0.5) and (y2 >= 0) and (y2 <= 0.5):
            # print("check2")
        print(num1)
            # нахождение стороны с которой прямая пересекается (по коду)
        if num1 != 0:  # вторая точка внутри, проверям что-бы первая была снаружи
            if num1 == 1 or num1 == 11 or num1 == 1001:  # слева так же верхний левый угол и нижний левый угол
                    # где Ax и Bx координаты стороны пересекающей прямую
                Ax = 0
                Ay = 0.5
                Bx = 0
                By = 0
            elif num1 == 10 or num1 == 110:  # вверх так же верхний правый угол
                    # где Ax1 и Bx2 координаты стороны пересекающей прямую
                Ax = 0
                Ay = 0.5
                Bx = 0.5
                By = 0.5
            elif num1 == 100 or num1 == 1100:  # право так же нижний правый угол
                    # где Ax1 и Bx2 координаты стороны пересекающей прямую
                Ax = 0.5
                Ay = 0
                Bx = 0.5
                By = 0.5
            elif num1 == 1000:  # нижняя грань!
                    # где Ax1 и Bx2 координаты стороны пересекающей прямую
                Ax = 0
                Ay = 0
                Bx = 0.5
                By = 0
            else:
                print("Ты наверное перепутал или что-то пошло не так.... в общем земля тебе пухом ....")
            Point3, Point4 = intersection(Ax, Ay, Bx, By, x1, y1, x2, y2)
            glBegin(GL_LINES)
            glColor3d(0, 0, 0)
            glVertex3d(Point3, Point4, 0)
            glVertex3d(x2, y2, 0)
            glEnd()
            return 0
    return 0
def display(window):
    global marker
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
    glClearColor(1.0, 1.0, 1.0, 1.0)
    glPushMatrix()
    glBegin(GL_LINE_LOOP)
    glColor3d(1, 0, 0)
    glColor3f(1.0, 0.5, 1.0)
    for i in range(len(cutingEdges)):
        glVertex2f(cutingEdges[i][0], cutingEdges[i][1])
    glEnd()
    
    global points
    # ввод данных координаты точек

    for i in range(len(points)):
        glBegin(GL_LINES)
        glColor3d(1, 0, 0)
        glVertex3d(points[i][0], points[i][1], 0)
        glVertex3d(points[i][2], points[i][3], 0)
        glEnd()
    # добавить вызов по кнопке
    if marker == 1:
        for i in range(len(points)):
            # count = crash(points[i][0], points[i][1], points[i][2], points[i][3])
            crash(points[i][0], points[i][1], points[i][2], points[i][3])
            """
            glBegin(GL_LINES)
            glColor3d(0, 0, 0)
            glVertex3d(0.2, 0.2, 0)
            glVertex3d(0.0, 0.2, 0)
            glEnd()
            """
    glPopMatrix()
    glfw.swap_buffers(window)
    glfw.poll_events()

def key_callback(window, key, scancode, action, mods):
    global marker
    global closed
    global edges
    global pix
    if action == glfw.PRESS:
        if key == glfw.KEY_UP:
            pix=[255]*n*n*3
            filpix = [255] * n * n * 3
            edges = []
            closed = 0
        if key == glfw.KEY_ENTER:
            marker = 1

main()
