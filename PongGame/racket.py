from turtle import Turtle , Screen 

class Racket :

    def __init__ (self) :
        self.racket_body = []
        self.starting_y = [0,20,-20]
         
    def body (self) :
        for ypos in self.starting_y :
            body_element = Turtle (shape = "square")
            body_element.penup ()
            body_element.color ("white")
            body_element.goto (0,ypos)
            self.racket_body.append (body_element)
            
    def starting_position (self,x_cor) :
        if x_cor > 0 :
            for body_element in self.racket_body :
                body_element.setx (x_cor/2 - 20)
        elif x_cor < 0 :
            for body_element in self.racket_body :
                body_element.setx (x_cor/2 + 20)
    
    def moveup (self) :
        if self.racket_body[1].ycor () != 290 :
            for body_element in self.racket_body :
                body_element.setheading (90)
                body_element.forward (30)
    
    def movedown (self) :
        if self.racket_body[-1].ycor () != - 290 :
            for body_element in self.racket_body :
                body_element.setheading (90)
                body_element.backward (30)

    def afterpoint (self) :
        for body_element in self.racket_body :
            body_element.sety (self.starting_y[self.racket_body.index (body_element)])

    
        






