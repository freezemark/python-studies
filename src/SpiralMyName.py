import turtle

t = turtle.Pen()
turtle.bgcolor('white')
colors = ['red', 'yellow', 'blue', 'green', 'purple', 'black']

names = ['', '', '', '']
names[0] = turtle.textinput('Введите имя', 'Как тебя зовут?')
names[1] = turtle.textinput('Введите имя', 'Как зовут твою сестру?')
names[2] = turtle.textinput('Введите имя', 'Как зовут твою маму?')
names[3] = turtle.textinput('Введите имя', 'Как зовут твоего папу?')

for x in range(100):
    t.pencolor(colors[x % 6])
    t.penup()
    t.forward(x * 4)
    t.pendown()
    t.write(names[x%4], font=['Arial', int((x+4)/4), 'bold'])
    t.left(92)
