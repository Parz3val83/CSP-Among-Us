#----1.2.5 - Make A Game Group----
  #----Cam, Fletcher, John----
  #----Simon Says----
#----Imports----
import turtle as trtl
#----Named Turtles----
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


wn = trtl.Screen()
wn.mainloop()