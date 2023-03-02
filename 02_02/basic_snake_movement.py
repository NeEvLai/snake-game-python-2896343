# Import the Turtle Graphics module
import turtle

# Define program constants
WIDTH = 500
HEIGHT = 500
DELAY = 400 # MILLISENCONDS between updates

def move_snake():
    stamper.clearstamps()

    new_head = snake[-1].copy()
    new_head[0] += 20

    snake.append(new_head)

    snake.pop(0)

    for segment in snake:
        stamper.goto(segment[0], segment[1])
        stamper.stamp()

    screen.update()

    turtle.ontimer(move_snake, DELAY)


# Create a window where we will do our drawing.
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)  # Set the dimensions of the Turtle Graphics window.
screen.title("Snake")
screen.bgcolor("pink")
screen.tracer(0)

# Create a turtle to do your bidding
stamper = turtle.Turtle()
stamper.shape("square")
stamper.penup()

snake = [[0,0],[20,0],[40,0],[60,0]]

for segment in snake:
    stamper.goto(segment[0], segment[1])
    stamper.stamp()

move_snake()

# Finish
turtle.done()
