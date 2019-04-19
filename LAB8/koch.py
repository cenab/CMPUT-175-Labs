import turtle

def Koch(length, order):
    '''
    order 0 Koch is just a straight line
    '''
    if order == 0:
        turtle.forward(length)
    else:
        '''
        TODO:
        make recursive calls to do the drawing

        order d Koch is composed of 4 of order (d-1) Koch


        for i in range(order+1):
            if i == 1:
                turtle.left(60)
            if i == 2:
                turtle.right(120)
            if i == 3:
                turtle.left(60)
            for i in range(4):
                if i == 1:
                    turtle.left(60)
                if i == 2:
                    turtle.right(120)
                if i == 3:
                    turtle.left(60)
                turtle.forward(length/(16*(order+1)))
                turtle.left(60)
                turtle.forward(length/(16*(order+1)))
                turtle.right(120)
                turtle.forward(length/(16*(order+1)))
                turtle.left(60)
                turtle.forward(length/(16*(order+1)))
                '''
        Koch(length/3, order-1)
        turtle.left(60)
        Koch(length/3, order-1)
        turtle.right(120)
        Koch(length/3, order-1)
        turtle.left(60)
        Koch(length/3, order-1)
#test
def main():
    turtle.setworldcoordinates(-1, -1, 150, 150)
    turtle.penup()
    turtle.goto(10,70)
    turtle.pendown()
    Koch(120, 4)
    turtle.mainloop()

main()
