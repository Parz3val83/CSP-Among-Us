import time
import random as random

#add if block
mode = int(input('Enter mode: '))# user input for difficulty
computer = []


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
    return computer

print(square_select())

