
import random as random

#add if block
mode = int(input('Enter mode: '))# user input for difficulty
computer = []


def square_select():  # add turtle input
    rand_list = [bttn1, bttn2, bttn3, bttn4, bttn5, bttn6, bttn7, bttn8, bttn9]
    for tile in range(mode):
        sequence = random.choice(rand_list)
        computer.append(sequence)
        #blink turtle
    return computer

print(square_select())

