import turtle
t = turtle.Pen()
t.penup()
turtle.bgcolor('black')
colors = ['red', 'yellow', 'blue', 'green', 'purple', 'orange']
sides = int(turtle.numinput('Количество сторон', 'Сколько сторон будет у спирали (2-6)?', 4, 2, 6))
t.speed(100)

for m in range(100):
    t.forward(m * 4)
    
    position = t.position()
    heading = t.heading()

    for n in range(sides):
        t.pendown()

        t.pencolor(colors[n % sides])
        t.circle(m / 2)
        t.right(360 / sides - 2)

        t.penup()

    t.setx(position[0])
    t.sety(position[1])
    t.setheading(heading)
    t.left(360 / sides + 2)
