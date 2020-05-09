import time
import turtle
turtle.bgcolor ("black")
circles = int(turtle.numinput('Количество кругов', 'Сколько будет кругов? (1-10)?', 3, 1, 10))
t = turtle.Pen()
t.speed(100)
all_colors = ["red", "blue","yellow","green", "orange", 'purple', "white","brown",'gray','pink']

inner = 100
size = 50 * circles
for n in range(circles):
    t.color(all_colors[n])
    for ght in range(inner):
            t.circle(size)
            t.left(360/inner)
    print(n)
    size = size - 50

time.sleep(3)
