#----1.2.5 - Make A Game Group----
  #----Cam, Fletcher, John----
  #----Simon Says----
#----Imports----
import turtle as trtl
import random as random
import time as time
#----Named Turtles----



score = 0
counter_interval = 1000
font_setup = "arial"
neg=-125
mddl=0
posi=125
#bttn1
bttn1 = trtl.Turtle()
bttn1.shapesize(5)
bttn1.shape("square")
bttn1.penup()
bttn1.goto (neg,posi)

#bttn2
bttn2 = trtl.Turtle()
bttn2.shapesize(5)
bttn2.shape("square")
bttn2.penup()
bttn2.goto (mddl,posi)

#bttn3
bttn3 = trtl.Turtle()
bttn3.shapesize(5)
bttn3.shape("square")
bttn3.penup()
bttn3.goto (posi,posi)

#bttn4
bttn4 = trtl.Turtle()
bttn4.shapesize(5)
bttn4.shape("square")
bttn4.penup()
bttn4.goto (neg,mddl)

#bttn5
bttn5 = trtl.Turtle()
bttn5.shapesize(5)
bttn5.shape("square")
bttn5.penup()
bttn5.goto (mddl,mddl)

#bttn6
bttn6 = trtl.Turtle()
bttn6.shapesize(5)
bttn6.shape("square")
bttn6.penup()
bttn6.goto (posi,mddl)

#bttn7
bttn7 = trtl.Turtle()
bttn7.shapesize(5)
bttn7.shape("square")
bttn7.penup()
bttn7.goto (neg,neg)

#bttn8
bttn8 = trtl.Turtle()
bttn8.shapesize(5)
bttn8.shape("square")
bttn8.penup()
bttn8.goto (mddl,neg)

#bttn9
bttn9 = trtl.Turtle()
bttn9.shapesize(5)
bttn9.shape("square")
bttn9.penup()
bttn9.goto (posi,neg)

rand_list = [bttn1, bttn2, bttn3, bttn4, bttn5, bttn6, bttn7, bttn8, bttn9]

def one(x ,y):
  bttn1.color("blue")
  time.sleep(0.5)
  bttn1.color("black")

def two(x ,y):
  bttn2.color("blue")
  time.sleep(0.5)
  bttn2.color("black")

def three(x ,y):
  bttn3.color("blue")
  time.sleep(0.5)
  bttn3.color("black")

def four(x ,y):
  bttn4.color("blue")
  time.sleep(0.5)
  bttn4.color("black")

def five(x ,y):
  bttn5.color("blue")
  time.sleep(0.5)
  bttn5.color("black")

def six(x ,y):
  bttn6.color("blue")
  time.sleep(0.5)
  bttn6.color("black")

def seven(x ,y):
  bttn7.color("blue")
  time.sleep(0.5)
  bttn7.color("black")

def eight(x ,y):
  bttn8.color("blue")
  time.sleep(0.5)
  bttn8.color("black")

def nine(x ,y):
  bttn9.color("blue")
  time.sleep(0.5)
  bttn9.color("black")

#add if block
mode = int(input('Enter mode: '))# user input for difficulty
computer = []

#----Definitions----
def square_select():  # add turtle input
    rand_list = [bttn1, bttn2, bttn3, bttn4, bttn5, bttn6, bttn7, bttn8, bttn9]
    for tile in range(mode):
        sequence = random.choice(rand_list)
        computer.append(sequence)
    for tile in computer: ### use nested for loop with click def
      time.sleep(0.5)
      tile.color('blue')
      time.sleep(0.5)
      tile.color('black')


#----Execute The Code----
print(square_select())

bttn1.onclick(one)
bttn2.onclick(two)
bttn3.onclick(three)
bttn4.onclick(four)
bttn5.onclick(five)
bttn6.onclick(six)
bttn7.onclick(seven)
bttn8.onclick(eight)
bttn9.onclick(nine)

wn = trtl.Screen()
wn.mainloop() 