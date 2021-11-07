from turtle import *
from random import randrange

score = 0
high_score = 0

snake = [[10, 0]]
aim = [0, -10]
food = [20, 0]

pen = Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))


def change(x, y):
    aim[0] = x
    aim[1] = y


def draw_square(x, y, size, name):
    up()
    goto(x, y)
    down()
    color(name)
    begin_fill()

    for count in range(4):
        forward(size)
        left(90)

    end_fill()


def inside(head):
    return -200 < head[0] < 190 and -200 < head[1] < 190


def move():
    head = [snake[-1][0] + aim[0], snake[-1][1] + aim[1]]

    if not inside(head) or head in snake:
        draw_square(head[0], head[1], 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        food[0] = randrange(-15, 15) * 10
        food[1] = randrange(-15, 15) * 10
    else:
        snake.pop(0)
        # score += 10
    clear()

    for body in snake:
        draw_square(body[0], body[1], 9, 'black')

    draw_square(food[0], food[1], 9, 'green')
    update()
    Screen().ontimer(move, 100)


Screen().setup(420, 420, 370, 0)
hideturtle()
Screen().tracer(0, 0)

Screen().listen()
Screen().onkey(lambda: change(10, 0), 'Right')
Screen().onkey(lambda: change(-10, 0), 'Left')
Screen().onkey(lambda: change(0, 10), 'Up')
Screen().onkey(lambda: change(0, -10), 'Down')


move()

done()
