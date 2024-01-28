import turtle
import math

unit = 300
angle = math.degrees(math.asin(2 / math.hypot(3, 2)))


def draw_rectangle(x, y, w, h, direction, size=1, p_color='black', f_color=None):
    pen = turtle.Turtle()
    pen.setheading(direction)
    pen.pensize(size)
    pen.pencolor(p_color)

    pen.penup()
    pen.goto(x, y)
    pen.pendown()

    if f_color:
        pen.fillcolor(f_color)
        pen.begin_fill()
        for side in [w / 2, h, w, h, w / 2]:
            pen.forward(side)
            pen.left(90)
        pen.end_fill()
    else:
        for side in [w / 2, h, w, h, w / 2]:
            pen.forward(side)
            pen.left(90)
    pen.hideturtle()


def draw_half_circle(x, y, radius, direction, size=1, p_color='black', f_color=None):
    pen = turtle.Turtle()
    pen.setheading(direction)  # 펜의 방향 설정
    pen.pensize(size)  # 펜의 굵기를 설정
    pen.pencolor(p_color)  # 펜의 색을 설정

    pen.penup()
    pen.goto(x, y)
    pen.pendown()  # 반원을 그릴 준비

    if f_color:  # 채우기 색이 있으면
        pen.fillcolor(f_color)  # 반원의 채우기 색 설정
        pen.begin_fill()
        pen.circle(radius, extent=180)
        pen.end_fill()
    else:  # 채우기 색이 없으면
        pen.circle(radius, extent=180)

    pen.hideturtle()


def draw_taegeuk(unit, direction):
    pen = turtle.Turtle()
    pen.setheading(direction)
    x = (3 * unit) / (2 * math.sqrt(13))
    y = unit / math.sqrt(13)

    xx = [x, -x, x, -x]
    yy = [-y, y, -y, y]
    radius = [unit / 2, unit / 2, unit / 4, unit / 4]
    p_color = ['red', 'blue', 'blue', 'red']
    f_color = ['red', 'blue', 'blue', 'red']
    theta = [90 - angle, 270 - angle, 90 - angle, 270 - angle]

    for x_val, y_val, r_val, t_val, p_val, f_val in zip(xx, yy, radius, theta, p_color, f_color):
        draw_half_circle(x_val, y_val, r_val, t_val, 2, p_val, f_val)


def draw_guae(kind, unit, direction):
    pen = turtle.Turtle()
    pen.setheading(direction)

    if kind == 'gun':
        x = [-(9 * unit) / (4 * math.sqrt(13)), -(21 * unit) / (8 * math.sqrt(13)), -(unit * 3) / math.sqrt(13)]
        y = [(3 * unit) / (2 * math.sqrt(13)), (14 * unit) / (8 * math.sqrt(13)), (unit * 2) / math.sqrt(13)]
        for x_val, y_val in zip(x, y):
            draw_rectangle(x_val, y_val, unit / 2, unit / 12, 90 - angle, 2, 'black', 'black')
    pen.hideturtle()

    if kind == 'gon':
        x = [(9 * unit) / (4 * math.sqrt(13)), (21 * unit) / (8 * math.sqrt(13)), (unit * 3) / math.sqrt(13)]
        y = [-(3 * unit) / (2 * math.sqrt(13)), -(14 * unit) / (8 * math.sqrt(13)), -(unit * 2) / math.sqrt(13)]
        for x_val, y_val in zip(x, y):
            draw_rectangle(x_val, y_val, unit / 2, unit / 12, 270 - angle, 2, 'black', 'black')

        a = [(9 * unit) / (4 * math.sqrt(13)), (21 * unit) / (8 * math.sqrt(13)), (3 * unit) / math.sqrt(13)]
        b = [-(3 * unit) / (2 * math.sqrt(13)), -(14 * unit) / (8 * math.sqrt(13)), -(2 * unit) / math.sqrt(13)]
        for a_val, b_val in zip(a, b):
            draw_rectangle(a_val, b_val, unit / 24, unit / 12, 270 - angle, 2, 'white', 'white')

    pen.hideturtle()

    if kind == 'gam':
        x = [(9 * unit) / (4 * math.sqrt(13)), (21 * unit) / (8 * math.sqrt(13)), (3 * unit) / math.sqrt(13)]
        y = [(3 * unit) / (2 * math.sqrt(13)), (14 * unit) / (8 * math.sqrt(13)), (2 * unit) / math.sqrt(13)]
        for x_val, y_val in zip(x, y):
            draw_rectangle(x_val, y_val, unit / 2, unit / 12, -90 + angle, 2, 'black', 'black')

        a = [(9 * unit) / (4 * math.sqrt(13)), (3 * unit) / math.sqrt(13)]
        b = [(3 * unit) / (2 * math.sqrt(13)), (2 * unit) / math.sqrt(13)]
        for a_val, b_val in zip(a, b):
            draw_rectangle(a_val, b_val, unit / 24, unit / 12, -90 + angle, 2, 'white', 'white')
    pen.hideturtle()

    if kind == 'yee':
        x = [-(9 * unit) / (4 * math.sqrt(13)), -(21 * unit) / (8 * math.sqrt(13)), -(3 * unit) / math.sqrt(13)]
        y = [-(3 * unit) / (2 * math.sqrt(13)), -(14 * unit) / (8 * math.sqrt(13)), -(2 * unit) / math.sqrt(13)]
        for x_val, y_val in zip(x, y):
            draw_rectangle(x_val, y_val, unit / 2, unit / 12, 90 + angle, 2, 'black', 'black')

        a = [-(21 * unit) / (8 * math.sqrt(13))]
        b = [-(14 * unit) / (8 * math.sqrt(13))]
        for a_val, b_val in zip(a, b):
            draw_rectangle(a_val, b_val, unit / 24, unit / 12, 90 + angle, 2, 'white', 'white')

    pen.hideturtle()