import turtle 
turtle.bgcolor ("black")
r = turtle.Pen()
t = turtle.Pen() 
t.speed(30)
r.speed(30)
circles = 50
r.color("orange")
t.color("yellow")
t.shape('turtle')
r.shape('turtle')
for sdcxsxswf in range(circles * 100):
    t.circle(50)
    r.circle(100)
    t.left(360/circles)
    r.right(360/circles)

