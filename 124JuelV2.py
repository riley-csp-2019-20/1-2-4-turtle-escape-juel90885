import turtle as turtle 
gary = turtle.Turtle()
gary.pensize(5)
gary.pencolor("lightgreen")
gary.ht()

amount = 30
wall_width = 10
gap_size = 20

for i in range(40):
    gary.forward(amount/3)
    # creating gap
    gary.pu()
    gary.forward(gap_size)
    gary.pd()
    #creating barrier
    gary.forward(10)
    gary.left(90)
    gary.forward(wall_width*2)
    gary.back(wall_width*2)
    gary.right(90)
    gary.forward(2*amount/3)
    gary.left(90)
    amount += wall_width



wn = turtle.Screen()
wn.mainloop()