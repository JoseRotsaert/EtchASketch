from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forward():
    tim.fd(10)


def move_backward():
    tim.bk(10)


def rotate_clockwise():
    current_heading = tim.heading()
    current_heading += 5
    tim.setheading(current_heading)


def rotate_counter_clockwise():
    current_heading = tim.heading()
    current_heading -= 5
    tim.setheading(current_heading)


def clear():
    screen.clear()
    tim.home()


screen.listen()

screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=rotate_counter_clockwise)
screen.onkey(key="d", fun=rotate_clockwise)
screen.onkey(key="c", fun=clear)

screen.exitonclick()
