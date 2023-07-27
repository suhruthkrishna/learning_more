import random
import time
import sys
comp_options=("Rock","Paper","Scissors")
user=input("Choose between Rock, Paper, Scissors")
comp=comp_options[random.randint(0,3)]
if user==comp:
    print(user)
    time.sleep(3)
    print(comp)
    time.sleep(1)
    print("Computer has got you")
else:
    print(user)
    time.sleep(3)
    print(comp)
    time.sleep(1)
    print("You win")

