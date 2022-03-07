from turtle import Turtle 

class Ball (Turtle) :

    def __init__ (self) :
        super ().__init__ () 
        self.shape ("circle")
        self.color ("white")
        self.shapesize (stretch_len = 0.5 , stretch_wid = 0.5)
        self.speed ('fastest')
        self.penup ()

    def racketcollision (self,player1,player2) :
        if self.distance (player1.racket_body[0]) < 30 :
            self.setheading (180)
        elif self.distance (player1.racket_body[1]) < 30 :
            self.setheading (90 + 30)
        elif self.distance (player1.racket_body[-1]) < 30 :
            self.setheading (180 + 30)
        elif self.distance (player2.racket_body[0]) < 30 :
            self.setheading (0)
        elif self.distance (player2.racket_body[1]) < 30 :
            self.setheading (30)
        elif self.distance (player2.racket_body[-1]) < 30 :
            self.setheading (-30)

    def wallcollision (self) :
        if (int (self.ycor ()) >  290) and ((self.heading () > 90) and (self.heading () < 180)):
            self.setheading (self.heading () + 50)
        elif (int (self.ycor ())) < - 290 and ((self.heading () > 180) and (self.heading () < 270))  :
            self.setheading (self.heading () - 50)
        elif (int (self.ycor ()) >  290) and ((self.heading () > 0) and (self.heading () < 90)):
            self.setheading (self.heading () + 310)
        elif (int (self.ycor ()) < - 290) and ((self.heading () > 270) and (self.heading () < 360)):
            self.setheading (self.heading () - 310)
    

    
        