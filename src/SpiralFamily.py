import turtle
pen = turtle.Pen()
turtle.bgcolor("black")
all_colors = ["red", "blue","yellow","green", "orange", 'purple', "white","brown",'gray','pink']
family = []
colors = []

def get_name_and_color():
    name = turtle.textinput("моя семья", "введите имя или нажмите Enter чтобы выйти ")

    if name != "":
        color = int(turtle.numinput("моя семья", "введите номер цвета или нажмите Enter чтобы выйти [1,10]", 1, 1, len(all_colors)))
    else:
        color = None

    return name, color

name, color = get_name_and_color()
while name != '':
    family.append(name)
    colors.append(all_colors[color - 1])
    name, color = get_name_and_color()

cnt = len(family)
for x in range(100):
    pen.pencolor(colors[x % cnt])
    pen.penup()
    pen.forward(x * 4)
    pen.pendown()
    pen.write(family[x % cnt], font = ["Arial", int((x+4)/4), "bold"])
    pen.left(360 / cnt + 2)