from turtle import Screen, Turtle
from referee import Referee
from racket import Racket
from ball import Ball
import time

display = Screen ()
display.canvwidth = 800
display.canvheight = 600
display.setup (1000,800)
display.bgcolor ("black")
display.tracer (0)
ref = Referee ()

ref.boundary (display.canvwidth,display.canvheight)
ref.partition (display.canvheight)

player_1 = Racket ()
player_1.body ()
player_1.starting_position (display.canvwidth)

player_2 = Racket ()
player_2.body ()
player_2.starting_position (- display.canvwidth)

pong = Ball ()
display.listen ()
display.onkey (key = 'Up' , fun = player_1.moveup)
display.onkey (key = 'Down' , fun = player_1.movedown)
display.onkey (key = 'w' , fun = player_2.moveup)
display.onkey (key = 's' , fun = player_2.movedown)

display.update ()
player1_counter = Turtle ()
player2_counter = Turtle ()
player1_counter.penup () , player2_counter.penup ()
player1_counter.color ("white") , player2_counter.color ("white")
player1_counter.hideturtle () , player2_counter.hideturtle () 
player1_counter.goto (-100,display.canvheight/2) , player2_counter.goto (100,display.canvheight/2)
player2_score = 0
player1_score = 0

while player2_score != 10 and player1_score != 10 :
    player1_counter.write (f"{player1_score}",align = "center",font = ("Arial",30,"normal"))
    player2_counter.write (f"{player2_score}",align = "center",font = ("Arial",30,"normal"))
    pong.goto (0,0)
    while pong.xcor () > - 400 and pong.xcor () < 400 :
        time.sleep (0.03)
        pong.forward (10)
        display.update ()
        pong.racketcollision (player_1,player_2) 
        pong.wallcollision ()
        if pong.xcor () < - 398 :
            player2_counter.clear ()
            player2_score += 1
            player_1.afterpoint () , player_2.afterpoint ()
            pong.setheading (180)
        elif pong.xcor () > 398 :
            player1_counter.clear ()
            player1_score += 1
            player_1.afterpoint () , player_2.afterpoint ()
            pong.setheading (0)

exclaim = Turtle ()
exclaim.penup () , exclaim.hideturtle ()
exclaim.pencolor ("white")
if player1_score == 10 :
    exclaim.write ("Player 1 Won!!!!",align = "center",font = ("Arial",30,"normal"))
elif player2_score == 10 :
    exclaim.write ("Player 2 Won!!!!",align = "center",font = ("Arial",30,"normal"))
display.update ()

display.exitonclick ()   