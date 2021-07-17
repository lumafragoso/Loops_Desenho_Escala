import turtle
t = turtle.Turtle()
valor = int(input('Digite um valor para o lado do triângulo: '))
for i in range(5):
    if i >= 1:
        # escolhi a escala de 5
        t.pendown()
        t.left(60)
        t.forward(valor * 5 * i)
        for j in range(2) :
            t.right(120)
            t.forward(valor * 5 * i)
        t.right(180)
        t.forward(valor * 2.5 * i)
        t.penup()
        t.right(90)
        t.forward(8)
        t.write(str(i) + 'X', align='left', font=('Arial', 5, 'normal'))
        t.left(180)
        t.forward(8)
        t.right(90)
        t.forward((valor * 2.5 * i) + 15)
