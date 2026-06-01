import turtle
import math
import random
import time

t = turtle.Turtle()
t.hideturtle()
t.speed(0)
turtle.bgcolor("black")
t.color("lime")

def draw_square(x, y, size, angle):
    t.penup()
    t.goto(x, y)
    t.setheading(angle)
    t.pendown()

    for _ in range(4):
        t.forward(size)
        t.left(90)

def pythagoras_tree(x, y, size, angle, depth, max_depth):
    if depth == 0:
        return

    colors = ["saddle brown", "forest green", "lime green", "green yellow", "light green"]
    t.color(colors[min(depth - 1, len(colors) - 1)])

    draw_square(x, y, size, angle)
    time.sleep(0.02)

    'angle_variation = random.randint(-10, 10)'

    x1 = x + size * math.cos(math.radians(angle + 90))
    y1 = y + size * math.sin(math.radians(angle + 90))
    new_size = size / math.sqrt(2)

    'pythagoras_tree(x1, y1, new_size, angle + 45 + angle_variation, depth - 1, max_depth)'
    pythagoras_tree(x1, y1, new_size, angle + 45, depth - 1, max_depth)

    x2 = x1 + new_size * math.cos(math.radians(angle + 45))
    y2 = y1 + new_size * math.sin(math.radians(angle + 45))
    'pythagoras_tree(x2, y2, new_size, angle - 45 - angle_variation, depth - 1, max_depth)'
    pythagoras_tree(x2, y2, new_size, angle - 45, depth - 1, max_depth)


pythagoras_tree(-50, -200, 100, 0, 8, 8)

turtle.done()