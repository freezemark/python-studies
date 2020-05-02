import turtle
colors = ["red", "yellow", "green", "blue","purple"]
t = turtle.Pen()
for x in range(360):
    t.pencolor(colors[x % len(colors)])
    t.circle(x+10)
    t.left(91)
    turtle.bgcolor(colors[(x + 1) % len(colors)])
