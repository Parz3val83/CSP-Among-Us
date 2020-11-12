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
bttn1.speed(10)
bttn1.penup()
bttn1.goto (neg,posi)

#bttn2
bttn2 = trtl.Turtle()
bttn2.shapesize(5)
bttn2.shape("square")
bttn2.speed(10)
bttn2.penup()
bttn2.goto (mddl,posi)

#bttn3
bttn3 = trtl.Turtle()
bttn3.shapesize(5)
bttn3.shape("square")
bttn3.speed(10)
bttn3.penup()
bttn3.goto (posi,posi)

#bttn4
bttn4 = trtl.Turtle()
bttn4.shapesize(5)
bttn4.shape("square")
bttn4.speed(10)
bttn4.penup()
bttn4.goto (neg,mddl)

#bttn5
bttn5 = trtl.Turtle()
bttn5.shapesize(5)
bttn5.shape("square")
bttn5.speed(10)
bttn5.penup()
bttn5.goto (mddl,mddl)

#bttn6
bttn6 = trtl.Turtle()
bttn6.shapesize(5)
bttn6.shape("square")
bttn6.speed(10)
bttn6.penup()
bttn6.goto (posi,mddl)

#bttn7
bttn7 = trtl.Turtle()
bttn7.shapesize(5)
bttn7.shape("square")
bttn7.speed(10)
bttn7.penup()
bttn7.goto (neg,neg)

#bttn8
bttn8 = trtl.Turtle()
bttn8.shapesize(5)
bttn8.shape("square")
bttn8.speed(10)
bttn8.penup()
bttn8.goto (mddl,neg)

#bttn9
bttn9 = trtl.Turtle()
bttn9.shapesize(5)
bttn9.shape("square")
bttn9.speed(10)
bttn9.penup()
bttn9.goto (posi,neg)

rand_list = [bttn1, bttn2, bttn3, bttn4, bttn5, bttn6, bttn7, bttn8, bttn9]

#add if block
mode = int(input('Enter mode: '))# user input for difficulty
computer = []
clckd = []

#----Definitions----
def one(x ,y):
  bttn1.color("blue")
  time.sleep(0.5)
  bttn1.color("black")
  clckd.append(bttn1)

def two(x ,y):
  bttn2.color("blue")
  time.sleep(0.5)
  bttn2.color("black")
  clckd.append(bttn2)

def three(x ,y):
  bttn3.color("blue")
  time.sleep(0.5)
  bttn3.color("black")
  clckd.append(bttn3)

def four(x ,y):
  bttn4.color("blue")
  time.sleep(0.5)
  bttn4.color("black")
  clckd.append(bttn4)

def five(x ,y):
  bttn5.color("blue")
  time.sleep(0.5)
  bttn5.color("black")
  clckd.append(bttn5)

def six(x ,y):
  bttn6.color("blue")
  time.sleep(0.5)
  bttn6.color("black")
  clckd.append(bttn6)

def seven(x ,y):
  bttn7.color("blue")
  time.sleep(0.5)
  bttn7.color("black")
  clckd.append(bttn7)

def eight(x ,y):
  bttn8.color("blue")
  time.sleep(0.5)
  bttn8.color("black")
  clckd.append(bttn8)

def nine(x ,y):
  bttn9.color("blue")
  time.sleep(0.5)
  bttn9.color("black")
  clckd.append(bttn9)

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


#----Onclicks----
bttn1.onclick(one)
bttn2.onclick(two)
bttn3.onclick(three)
bttn4.onclick(four)
bttn5.onclick(five)
bttn6.onclick(six)
bttn7.onclick(seven)
bttn8.onclick(eight)
bttn9.onclick(nine)

done = trtl.Turtle()
done.shape("circle")
done.penup()
done.goto(0,-200)
done.pendown()

def printclckd(x, y):
  time.sleep(0.25)
  done.color('blue')
  time.sleep(0.25)
  done.color('black')
  finish = int(input('Do you want to check? Type 1 for Yes 0 for No: '))#Asks the user if they're done
  if (finish == 1):
    if (computer == clckd):
      bttn1.color("green")
      bttn2.color("green")
      bttn3.color("green")
      bttn4.color("green")
      bttn5.color("green")
      bttn6.color("green")
      bttn7.color("green")
      bttn8.color("green")
      bttn9.color("green")
      print ("Congrats! You're good at remembering flashing colors!")
    else:
      bttn1.color("red")
      bttn2.color("red")
      bttn3.color("red")
      bttn4.color("red")
      bttn5.color("red")
      bttn6.color("red")
      bttn7.color("red")
      bttn8.color("red")
      bttn9.color("red")
      print ("Try Again! You need to work on your memory!")

done.onclick(printclckd)





wn = trtl.Screen()
wn.listen()
wn.mainloop() 
