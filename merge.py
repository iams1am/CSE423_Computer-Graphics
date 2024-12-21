
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random

#task 1

class Rain:
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed

direction = 0
day = False

rains = []
for i in range(100):
    x = random.uniform(500, 0)
    y = random.uniform(0, 500)
    speed = random.uniform(2, 6)
    rains.append(Rain(x, y, speed))
    

def update_position(): # animating positions of rain from top to bottom
    for i in rains:
        i.x += direction
        i.y -= i.speed
        if(i.y < 0): # if rain hits ground it changes to random position
            i.y = random.uniform(0, 500)
            i.x = random.uniform(0, 500)

def rerender(i):
    glutPostRedisplay()
    glutTimerFunc(16, rerender, 0)

def points(x, y, s): #drawing points
    glPointSize(s)
    glBegin(GL_POINTS)
    glVertex2f(x,y)
    glEnd()
def line(x1, y1, x2, y2): #drawing lines
    glPointSize(100)
    glLineWidth(4)
    glBegin(GL_LINES)
    glVertex2f(x1, y1)
    glVertex2f(x2, y2)
    glEnd()




def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def rain_change(key, x, y): # right and left updating positions of rain
    global direction

    if(key == GLUT_KEY_RIGHT):
        direction += 1

    if(key == GLUT_KEY_LEFT):
        direction -= 1

def keys(key, x, y):
    global day
    if(key == b"d"): # click d for day
        day = True

    if(key == b"n"): # click n for night
        day = False

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()

    if(day == True):
        glClearColor(1, 1, 1, 1)
        glColor3f(0, 0, 0)
    else:
        glClearColor(0, 0, 0, 0)
        glColor3f(1, 1, 1)

    #house
    line(100, 250, 250, 400) #upper /
    line(250, 400, 400, 250) #upper \
    line(100, 250, 400, 250) #roof -

    points(265, 100, 5)
    line(110, 50, 390, 50) # house bottom
    line(110, 250, 110, 50) #house left wall
    line(390, 250, 390, 50) #house right wall

    #door
    line(225, 150, 225, 50) #door left wall
    line(223, 150, 276, 150) #door upper wall
    line(275, 150, 275, 50) #door right wall

      #window
    # line(320, 200, 370, 150)
    line(320, 200, 320, 150) # left
    line(370, 150, 370, 200) #right
    line(320, 175, 370, 175) # center line
    line(320, 200, 370, 200) # top
    line(370, 150, 320, 150) # bottom
    line(345, 200, 345, 150) # horizontal |


    update_position()

    for i in rains: # changing rain color based on day and night
        if(day == True):
            glColor3f(0, 0, 0)
        else:
            glColor3f(1, 1, 1)
        line(i.x, i.y, i.x, i.y + 20)
    glutSwapBuffers()

glutInit()
glutTimerFunc(0, rerender, 0)
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"Task 1")
glutDisplayFunc(showScreen)
glutSpecialFunc(rain_change)
glutKeyboardFunc(keys)

glutMainLoop()


#task 2

# points = []
# speed = 1
# play = True
# blink = False
#
# def mouse(button, state, x, y):
#     global blink
#     if button == GLUT_RIGHT_BUTTON and state == GLUT_DOWN:
#         color = [random.random(), random.random(), random.random(), 1]
#         direction = random.choice([(1, 1), (-1, 1), (1, -1), (-1, -1)])
#         point = [x, 500-y, direction[0], direction[1], color]
#         points.append(point)
#     elif button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
#         if blink:
#             blink = False
#         else:
#             blink = True
#
# def keyboardListener(key, x, y): #entering keys
#     global speed, play
#     if key == b' ': # click space for stop and play
#         if play:
#             play = False
#         else:
#             play = True
#     elif key == GLUT_KEY_UP: #up key for speed ++
#         speed += 1
#     elif key == GLUT_KEY_DOWN: # down key for speed --
#         if speed > 1:
#             speed -= 1
#         else:
#             speed = 1 # speed reduces to 1 atmost
#
# def point(x, y, size, color): #drawing points
#     glColor4f(color[0], color[1], color[2], color[3])
#     glPointSize(size)
#     glEnable(GL_POINT_SMOOTH)
#     glBegin(GL_POINTS)
#     glVertex2f(x,y)
#     glEnd()vbbb
#
# def iterate():
#     glViewport(0, 0, 500, 500)
#     glMatrixMode(GL_PROJECTION)
#     glLoadIdentity()
#     glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
#     glMatrixMode (GL_MODELVIEW)
#     glLoadIdentity()
#
# def showScreen():
#     glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
#     glEnable(GL_BLEND)
#     glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
#     glLoadIdentity()
#     iterate()
#
#     for p in points:
#         point(p[0], p[1], 10, p[4])
#     glutSwapBuffers()
#
# def animate(ball):
#     if play:
#         for p in points:
#             p[0] += p[2]*speed
#             p[1] += p[3]*speed
#             if blink:
#                 p[4][3] = (p[4][3]+0.1)%1
#             if p[0] > 500 or p[0] < 0:
#                 p[2] *= -1
#             if p[1] > 500 or p[1] < 0:
#                 p[3] *= -1
#
#     glutTimerFunc(30, animate, "ball")
#     glutPostRedisplay()
#
# glutInit()
# glutInitDisplayMode(GLUT_RGBA)
# glutInitWindowSize(500, 500)
# glutInitWindowPosition(0, 0)
# wind = glutCreateWindow(b"Task 2")
# glutDisplayFunc(showScreen)
# glutIdleFunc(animate("ball"))
# glutMouseFunc(mouse)
# glutKeyboardFunc(keyboardListener)
# glutSpecialFunc(keyboardListener)
# glutMainLoop()