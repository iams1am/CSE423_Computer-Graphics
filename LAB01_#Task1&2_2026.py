#Task 1

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

import math

W_Width, W_Height = 500, 500

dropx1, dropy1 = 0, 220
dropx2, dropy2 = 0, 250
raindrops = [[0,250,0,220], [30,220,30,190], [-50,260,-50,230], [70,170,70,140],
            [-80,220,-80,190], [120,100,120,70], [-150,120,-150,90], [200,30,200,0],
            [-225,40,-225,10], [-210,90,-210,60], [220,55,220,25], [150,230,150,200],
            [-125,200,-125,170], [-190,200,-190,170],
            [100,180,100,150], [-170,140,-170,110], [50,90,50,60],
            [-30,270,-30,240], [180,200,180,170], [-240,160,-240,130],
            [240,130,240,100], [-100,80,-100,50], [160,260,160,230],
            [-200,250,-200,220], [90,240,90,210], [-60,150,-60,120],
            [40,200,40,170], [-140,270,-140,240], [210,180,210,150],
            [-180,60,-180,30], [130,50,130,20], [-20,110,-20,80],
            [250,220,250,190], [-250,200,-250,170], [75,270,75,240],
            [-110,240,-110,210], [190,100,190,70], [-230,130,-230,100],
            ] #[[x2,y2,x1,y1]]
speed_2 = 0.2
dark = 0.0
key_count = 0

def convert_coordinate(x, y):
   global W_Width, W_Height
   a = x - (W_Width / 2)
   b = (W_Height / 2) - y
   return a, b


def draw_background(dark):
   # Sky quad (changes with dark)
   sky_r = max(0, 0.0 + dark * 1.0)
   sky_g = max(0, 0.0 + dark * 1.0)
   sky_b = max(0, 0.0 + dark * 1.0)
   glColor3f(sky_r, sky_g, sky_b)
   glBegin(GL_QUADS)
   glVertex2f(-260, 260)
   glVertex2f(260, 260)
   glVertex2f(260, 55)
   glVertex2f(-260, 55)
   glEnd()
   # Brown ground
   glColor3f(0.55, 0.42, 0.12)
   glBegin(GL_QUADS)
   glVertex2f(-260, 55)
   glVertex2f(260, 55)
   glVertex2f(260, -260)
   glVertex2f(-260, -260)
   glEnd()
   # Green grass strip
   glColor3f(0.0, 0.85, 0.0)
   glBegin(GL_QUADS)
   glVertex2f(-260, 58)
   glVertex2f(260, 58)
   glVertex2f(260, 42)
   glVertex2f(-260, 42)
   glEnd()
   # Trees on both sides of house
   for tx in range(-240, 250, 28):
       if -155 < tx < 155:
           continue
       glColor3f(0.0, 0.75, 0.0)
       glBegin(GL_TRIANGLES)
       glVertex2f(tx, 80)
       glVertex2f(tx - 13, 42)
       glVertex2f(tx + 13, 42)
       glEnd()


# def draw_house(dark, x1, y1, x2, y2, x3, y3, x4, y4, x5, y5,
#                 x6, y6, x7, y7, x8, y8, x9, y9, x10, y10,
#                 x11, y11, x12, y12, x13, y13, x14, y14, x15, y15,
#                 x16, y16, x17, y17, x18, y18, x19, y19, x20, y20,
#                ):
def draw_house(dark, x1=-150, y1=50, x2=0, y2=100, x3=150, y3=50,
               x4=-135, y4=50, x5=-135, y5=-100, x6=135, y6=50, x7=135, y7=-100,
               x8=-75, y8=-10, x9=-75, y9=-100, x10=-30, y10=-10, x11=-30, y11=-100,
               x12=-40, y12=-65,
               x13=30, y13=15, x14=30, y14=-25, x15=75, y15=15, x16=75, y16=-25,
               x17=52.5, y17=15, x18=52.5, y18=-25, x19=30, y19=-5, x20=75, y20=-5,):
   # Filled roof (purple)
   glColor3f(0.4, 0.3, 0.9)
   glBegin(GL_TRIANGLES)
   glVertex2f(x1, y1)
   glVertex2f(x2, y2)
   glVertex2f(x3, y3)
   glEnd()
   # Filled walls (cream)
   glColor3f(1.0, 0.96, 0.86)
   glBegin(GL_QUADS)
   glVertex2f(x4, y4)
   glVertex2f(x6, y6)
   glVertex2f(x7, y7)
   glVertex2f(x5, y5)
   glEnd()
   # Filled door (blue)
   glColor3f(0.2, 0.5, 1.0)
   glBegin(GL_QUADS)
   glVertex2f(x8, y8)
   glVertex2f(x10, y10)
   glVertex2f(x11, y11)
   glVertex2f(x9, y9)
   glEnd()
   # Filled window (blue)
   glColor3f(0.2, 0.5, 1.0)
   glBegin(GL_QUADS)
   glVertex2f(x13, y13)
   glVertex2f(x15, y15)
   glVertex2f(x16, y16)
   glVertex2f(x14, y14)
   glEnd()
   glPointSize(3)
   glBegin(GL_POINTS) #for doorknob
   glVertex2f(x12, y12)
   glEnd() #end door

   glLineWidth(2) #window outline
   glBegin(GL_LINES)
   glVertex2f(x13, y13)
   glVertex2f(x14, y14)
   glVertex2f(x15, y15)
   glVertex2f(x16, y16)
   glVertex2f(x13, y13)
   glVertex2f(x15, y15)
   glVertex2f(x14, y14)
   glVertex2f(x16, y16)
   glEnd()
   glLineWidth(1)  # window grid
   glBegin(GL_LINES)
   glVertex2f(x17, y17)
   glVertex2f(x18, y18)
   glVertex2f(x19, y19)
   glVertex2f(x20, y20)
   glEnd()

def draw_rain(rain, x):
   glLineWidth(1)
   glColor3f(0.5, 0.7, 1.0)
   glBegin(GL_LINES)
   # glVertex2f(x1, y1)
   # glVertex2f(x2, y2)
   for i in range(len(rain)):
       glVertex2f(rain[i][0], rain[i][1])
       glVertex2f(rain[i][2], rain[i][3])
   glEnd()

def keyboardListener(key, x, y):
   global raindrops, dark

   if key == b'd':
       if dark <= 1:
           dark += 0.05
           draw_rain(raindrops, dark)
           draw_house(dark, )
           print('darkened')

   if key==b'b':
       if dark >= 0:
           dark -= 0.05
           print('brightened')
           draw_rain(raindrops, dark)

   glutPostRedisplay()


def specialKeyListener(key, x, y):
   global key_count
   if key == GLUT_KEY_RIGHT:
       if key_count <= 4:
           key_count += 1
           for i in range(len(raindrops)):
               if raindrops[i][0]-raindrops[i][2] == 0 or abs((raindrops[i][1]-raindrops[i][3])/(raindrops[i][0]-raindrops[i][2])) >= 1: #theta>=45degrees
                   raindrops[i][0] += 1.0
                   raindrops[i][1] -= 1.0
                   raindrops[i][2] -= 1.0
                   raindrops[i][3] += 1.0
   if key == GLUT_KEY_LEFT:
       if key_count >= -4:
           key_count -= 1
           for i in range(len(raindrops)):
               if raindrops[i][0] - raindrops[i][2] == 0 or abs((raindrops[i][1] - raindrops[i][3]) / (raindrops[i][0] - raindrops[i][2])) >= 1:  # theta<=45degrees
                   raindrops[i][0] -= 1.0
                   raindrops[i][1] -= 1.0
                   raindrops[i][2] += 1.0
                   raindrops[i][3] += 1.0
   glutPostRedisplay()

def display():
   # //clear the display
   global dark
   glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
   glClearColor(0, 0, 0, 0)
   glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
   # //load the correct matrix -- MODEL-VIEW matrix
   glMatrixMode(GL_MODELVIEW)
   # //initialize the matrix
   glLoadIdentity()
   # //now give three info
   # //1. where is the camera (viewer)?
   # //2. where is the camera looking?
   # //3. Which direction is the camera's UP direction?
   gluLookAt(0, 0, 200, 0, 0, 0, 0, 1, 0)
   glMatrixMode(GL_MODELVIEW)

   # draw_house(-150, 50, 0, 100, 150, 50, #roof
   #             -135, 50, -135, -100, 135, 50, 135, -100, #house_body
   #             -75, -10, -75, -100, -30, -10, -30, -100, #door
   #             -40, -65, #doorknob
   #             30, 15, 30, -25, 75, 15, 75, -25,#window
   #             52.5, 15, 52.5, -25, 30, -5, 75, -5, #window_grid
   #             )
   global dropx1, dropy1, dropx2, dropy2, raindrops
   draw_background(dark)
   draw_house(dark)
   # draw_rain(dropx1, dropy1, dropx2, dropy2)
   draw_rain(raindrops, dark)

   glutSwapBuffers()


def animate():
   # //codes for any changes in Models, Camera
   glutPostRedisplay()
   global dropy1, dropy2, speed_2, raindrops

   for i in range(len(raindrops)):
       if raindrops[i][3] <= -250:
           raindrops[i][1] = 250
           raindrops[i][3] = 220
       else:
           raindrops[i][1] = raindrops[i][1] - speed_2
           raindrops[i][3] = raindrops[i][3] - speed_2


def init():
   # //clear the screen
   glClearColor(0, 0, 0, 0)
   # //load the PROJECTION matrix
   glMatrixMode(GL_PROJECTION)
   # //initialize the matrix
   glLoadIdentity()
   # //give PERSPECTIVE parameters
   gluPerspective(104, 1, 1, 1000.0)
   # **(important)**aspect ratio that determines the field of view in the X direction (horizontally). The bigger this angle is, the more you can see of the world - but at the same time, the objects you can see will become smaller.
   # //near distance
   # //far distance


glutInit()
glutInitWindowSize(W_Width, W_Height)
glutInitWindowPosition(0, 0)
glutInitDisplayMode(GLUT_DEPTH | GLUT_DOUBLE | GLUT_RGB)  # //Depth, Double buffer, RGB color

# glutCreateWindow("My OpenGL Program")
wind = glutCreateWindow(b"OpenGL Coding Practice")
init()

glutDisplayFunc(display)  # display callback function
glutIdleFunc(animate)  # what you want to do in the idle time (when no drawing is occuring)

glutKeyboardFunc(keyboardListener)
glutSpecialFunc(specialKeyListener)

glutMainLoop()  # The main loop of OpenGL

######################################################

#Task 2

########################################################


# from OpenGL.GL import *
# from OpenGL.GLUT import *
# from OpenGL.GLU import *

# import math, random

# W_Width, W_Height = 500, 500

# speed = 0.01
# create_new = False
# newpoints = []
# point_colors = []
# sp_count = 0
# spacebar = False


# def convert_coordinate(x, y):
#    global W_Width, W_Height
#    a = x - (W_Width / 2)
#    b = (W_Height / 2) - y
#    return a, b

# def create_point(x,y):
#    global newpoints, W_Width, W_Height
#    a = x - (W_Width / 2)
#    b = (W_Height / 2) - y
#    color1 = random.random()
#    color2 = random.random()
#    color3 = random.random()
#    x_sign = random.choice([-1,1])
#    y_sign = random.choice([-1,1])
#    newpoints.append([a,b,color1,color2,color3,x_sign,y_sign])
#    point_colors.append(color1)
#    point_colors.append(color2)
#    point_colors.append(color3)
#    # return a, b, color1, color2, color3

# def drawAxes():
#    pass


# def keyboardListener(key, x, y):
#    global sp_count, spacebar
#    if key == b' ':
#        sp_count += 1
#        if sp_count % 2 != 0:
#            spacebar = True
#        else:
#            spacebar = False

#    # if key==b's':
#    #    print(3)
#    # if key==b'd':
#    #     print(4)

#    glutPostRedisplay()


# def specialKeyListener(key, x, y):
#    global speed, spacebar
#    if spacebar == False:
#        if key == GLUT_KEY_UP:
#            speed *= 2
#            print("Speed Increased")
#        if key == GLUT_KEY_DOWN:  # // up arrow key
#            speed /= 2
#            print("Speed Decreased")

#    glutPostRedisplay()
#    # if key==GLUT_KEY_RIGHT:

#    # if key==GLUT_KEY_LEFT:

#    # if key==GLUT_KEY_PAGE_UP:

#    # if key==GLUT_KEY_PAGE_DOWN:

#    # case GLUT_KEY_INSERT:
#    #
#    #
#    # case GLUT_KEY_HOME:
#    #
#    # case GLUT_KEY_END:
#    #


# def mouseListener(button, state, x, y):  # /#/x, y is the x-y of the screen (2D)
#    global create_new, newpoints, point_colors, spacebar
#    if button == GLUT_LEFT_BUTTON and spacebar == False:
#        if (state == GLUT_DOWN):  # // 2 times?? in ONE click? -- solution is checking DOWN or UP
#            for i in range(len(newpoints)):
#                newpoints[i][2], newpoints[i][3], newpoints[i][4] = 0, 0, 0
#        if (state == GLUT_UP):
#            for i in range(len(newpoints)):
#                newpoints[i][2],newpoints[i][3],newpoints[i][4] = point_colors[i],point_colors[i+1],point_colors[i+2]

#    if button == GLUT_RIGHT_BUTTON and spacebar == False:
#        if state == GLUT_DOWN:
#            create_new = create_point(x, y)
#            create_new = True
#    # case GLUT_MIDDLE_BUTTON:
#    #     //........

#    glutPostRedisplay()


# def display():
#    # //clear the display
#    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
#    glClearColor(0, 0, 0, 0)  # //color black
#    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
#    # //load the correct matrix -- MODEL-VIEW matrix
#    glMatrixMode(GL_MODELVIEW)
#    # //initialize the matrix
#    glLoadIdentity()
#    # //now give three info
#    # //1. where is the camera (viewer)?
#    # //2. where is the camera looking?
#    # //3. Which direction is the camera's UP direction?
#    gluLookAt(0, 0, 200, 0, 0, 0, 0, 1, 0)
#    glMatrixMode(GL_MODELVIEW)

#    drawAxes()
#    global newpoints, spacebar

#    if (create_new):
#        # m, n, c1, c2, c3 = create_new
#        for i in range(len(newpoints)):
#            glPointSize(10)
#            glBegin(GL_POINTS)
#            glColor3f(newpoints[i][2],newpoints[i][3],newpoints[i][4])
#            glVertex2f(newpoints[i][0], newpoints[i][1])
#            glEnd()

#    glutSwapBuffers()


# def animate():
#    # //codes for any changes in Models, Camera
#    glutPostRedisplay()
#    global speed, newpoints, spacebar
#    for i in range(len(newpoints)):
#        if spacebar == False:
#            if newpoints[i][0] <= -250 or newpoints[i][0] >= 250:
#                newpoints[i][5] *= -1
#            if newpoints[i][1] <= -250 or newpoints[i][1] >= 250:
#                newpoints[i][6] *= -1
#            newpoints[i][0] = newpoints[i][0] + (newpoints[i][5] * speed)
#            newpoints[i][1] = newpoints[i][1] + (newpoints[i][6] * speed)
#        # newpoints[i][0] = (newpoints[i][0] + (1 * speed)) % 180
#        # newpoints[i][1] = (newpoints[i][1] + (-1 * speed)) % 180


# def init():
#    # //clear the screen
#    glClearColor(0, 0, 0, 0)
#    # //load the PROJECTION matrix
#    glMatrixMode(GL_PROJECTION)
#    # //initialize the matrix
#    glLoadIdentity()
#    # //give PERSPECTIVE parameters
#    gluPerspective(104, 1, 1, 1000.0)
#    # **(important)**aspect ratio that determines the field of view in the X direction (horizontally). The bigger this angle is, the more you can see of the world - but at the same time, the objects you can see will become smaller.
#    # //near distance
#    # //far distance


# glutInit()
# glutInitWindowSize(W_Width, W_Height)
# glutInitWindowPosition(0, 0)
# glutInitDisplayMode(GLUT_DEPTH | GLUT_DOUBLE | GLUT_RGB)  # //Depth, Double buffer, RGB color

# # glutCreateWindow("My OpenGL Program")
# wind = glutCreateWindow(b"OpenGL Coding Practice")
# init()

# glutDisplayFunc(display)  # display callback function
# glutIdleFunc(animate)  # what you want to do in the idle time (when no drawing is occuring)

# glutKeyboardFunc(keyboardListener)
# glutSpecialFunc(specialKeyListener)
# glutMouseFunc(mouseListener)

# glutMainLoop()  # The main loop of OpenGL




