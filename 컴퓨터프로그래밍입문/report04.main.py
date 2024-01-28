from report04 import *
import turtle
import math

unit = 300
kinds_guae = ['gun', 'gon', 'gam', 'yee']

width = 3*unit
height = 2*unit
angle = math.degrees(math.asin(2/math.hypot(3,2)))  #태극 기울기 angle

turtle.setup(int(1.2*width), int(1.2*height))


draw_rectangle(0, - height/2, width, height, 0, 3)  #태극기 테두리 그리기

draw_taegeuk(unit, angle)

direction = [90-angle, 270-angle, -90+angle, 90+angle]

for n in range(4):
    draw_guae(kinds_guae[n], unit, direction[n])

turtle.done()