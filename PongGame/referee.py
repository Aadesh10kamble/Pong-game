from turtle import Turtle 

class Referee (Turtle) :

    def __init__ (self) :
        super ().__init__ ()
        self.hideturtle ()
        self.speed ("fastest")
        self.penup ()
        self.color ("white")
        self.pensize (3)

    def boundary (self,x_cor,y_cor) :
        self.goto (- x_cor/2 , - y_cor/2)
        self.pendown ()
        for (angle , distance)  in [(90,y_cor),(0,x_cor),(270,y_cor),(180,x_cor)] :
            self.setheading (angle)
            self.forward (distance)

    def partition (self,y_cor) :
        self.penup ()
        self.goto (0,y_cor/2)
        self.setheading (270)
        while self.ycor () != (- y_cor / 2):
            self.pendown () , self.forward (10)
            self.penup () , self.forward (10)
    


