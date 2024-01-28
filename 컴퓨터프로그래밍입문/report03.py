import turtle
import math

u = 200
w = 3*u     #테극기의 폭
h = 2*u     #태극기의 높이

width = int(1.5*w)   #화면의 폭
height = int(1.5*h)  #화면의 높이
angle = math.degrees(math.acos(3/math.sqrt(9+4)))   #각도

turtle.setup(width, height)
pen = turtle.Turtle()


#태극기 테두리
pen.penup()
pen.goto(int(-1.5*u), -u)

pen.pendown()
pen.pensize(3)
for side in 2*[3*u, 2*u]:
    pen.forward(side)
    pen.left(90)

pen.penup()
pen.home()

# 태극 큰 원의 빨간 반원 만들기
pen.setheading(90-angle)
pen.color('red')
c1 = int(u/2 * 3/math.sqrt(9+4))
c2 = -int(u/2 * 2/math.sqrt(9+4))

pen.goto(c1, c2)
pen.pendown()
pen.begin_fill()
pen.circle(u//2, extent = 180)
pen.end_fill()


# 파란색 반원 만들기
pen.color('blue')
pen.begin_fill()
pen.circle(u//2, extent=180)
pen.end_fill()

# 파란색 작은 반원 그리기
pen.begin_fill()
pen.circle(u//4, extent=180)
pen.end_fill()

# 빨간색 작은 반원 그리기
pen.color('red')
pen.right(90)
pen.forward(u//2)
pen.left(90)
pen.begin_fill()
pen.circle(u//4, extent=180)
pen.end_fill()

# 궤의 색 지정
pen.color('black')


# 건괘 (좌측 상단)
pen.penup()
pen.setheading(180-angle)
pen.forward(3*u//4)
pen.right(90)


pen.begin_fill()
for side in [u//4, u//12, u//2, u//12, u//4]:
    pen.forward(side)
    pen.left(90)
pen.end_fill()

pen.penup()
pen.forward(3*u//24)
pen.right(90)
pen.pendown()

pen.begin_fill()
for side in [u//4, u//12, u//2, u//12, u//4]:
    pen.forward(side)
    pen.left(90)
pen.end_fill()

pen.penup()
pen.forward(3*u//24)
pen.right(90)
pen.pendown()

pen.begin_fill()
for side in [u//4, u//12, u//2, u//12, u//4]:
    pen.forward(side)
    pen.left(90)
pen.end_fill()


# 감괘(우측 상단)
pen.penup()
pen.home()
pen.setheading(angle)
pen.forward(3*u//4)
pen.left(90)

pen.pendown()

pen.begin_fill()
for side in [u//4, u//12, u//2, u//12, u//4]:
    pen.forward(side)
    pen.right(90)
pen.end_fill()

pen.color('white')
pen.setheading(90+angle)

pen.begin_fill()
for side in [u//48, u//12, u//24, u//12, u//48]:
    pen.forward(side)
    pen.right(90)
pen.end_fill()

pen.color('black')
pen.penup()
pen.forward(3*u//24)
pen.right(90)
pen.pendown()

pen.begin_fill()
for side in [u//4, u//12, u//2, u//12, u//4]:
    pen.forward(side)
    pen.left(90)
pen.end_fill()

pen.penup()
pen.forward(3*u//24)
pen.right(90)
pen.pendown()

pen.begin_fill()
for side in [u//4, u//12, u//2, u//12, u//4]:
    pen.forward(side)
    pen.left(90)
pen.end_fill()

pen.color('white')
pen.setheading(90+angle)

pen.begin_fill()
for side in [u//48, u//12, u//24, u//12, u//48]:
    pen.forward(side)
    pen.right(90)
pen.end_fill()

# 이괘 (좌측 하단)
pen.color('black')
pen.penup()
pen.home()
pen.setheading(180+angle)
pen.forward(3*u//4)
pen.right(90)

pen.pendown()

pen.begin_fill()
for side in [u//4, u//12, u//2, u//12, u//4]:
    pen.forward(side)
    pen.left(90)
pen.end_fill()


pen.penup()
pen.forward(3*u//24)
pen.right(90)
pen.pendown()

pen.begin_fill()
for side in [u//4, u//12, u//2, u//12, u//4]:
    pen.forward(side)
    pen.left(90)
pen.end_fill()

pen.color('white')
pen.setheading(90+angle)
pen.begin_fill()
for side in [u//48, u//12, u//24, u//12, u//48]:
    pen.forward(side)
    pen.left(90)
pen.end_fill()

pen.color('black')
pen.penup()
pen.forward(3*u//24)
pen.right(90)
pen.pendown()

pen.begin_fill()
for side in [u//4, u//12, u//2, u//12, u//4]:
    pen.forward(side)
    pen.left(90)
pen.end_fill()

# 곤괘 그리기(우측 하단)

pen.penup()
pen.home()
pen.setheading(-angle)
pen.forward(3*u//4)
pen.right(90)

pen.pendown()

pen.begin_fill()
for side in [u//4, u//12, u//2, u//12, u//4]:
    pen.forward(side)
    pen.left(90)
pen.end_fill()
pen.pendown()

pen.color('white')
pen.setheading(90-angle)

pen.begin_fill()
for side in [u//48, u//12, u//24, u//12, u//48]:
    pen.forward(side)
    pen.right(90)
pen.end_fill()

pen.color('black')
pen.penup()
pen.forward(3*u//24)
pen.right(90)
pen.pendown()

pen.begin_fill()
for side in [u//4, u//12, u//2, u//12, u//4]:
    pen.forward(side)
    pen.left(90)
pen.end_fill()

pen.color('white')
pen.setheading(90-angle)

pen.begin_fill()
for side in [u//48, u//12, u//24, u//12, u//48]:
    pen.forward(side)
    pen.right(90)
pen.end_fill()

pen.color('black')
pen.penup()
pen.forward(3*u//24)
pen.right(90)
pen.pendown()

pen.begin_fill()
for side in [u//4, u//12, u//2, u//12, u//4]:
    pen.forward(side)
    pen.left(90)
pen.end_fill()

pen.color('white')
pen.setheading(90-angle)

pen.begin_fill()
for side in [u//48, u//12, u//24, u//12, u//48]:
    pen.forward(side)
    pen.right(90)
pen.end_fill()

#pen.hideturtle()
turtle.done()