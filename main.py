import time
import random
import wikipedia

name = input("What is your name?")
favouritething = input("Cool! Whats your favourite thing?")
favNum = int(input("Pick a number between 1 and 10"))

print("Here are ", favNum ," sentences about ",favouritething," from wikipedia :)")
print()

print(wikipedia.summary(favouritething, sentences=favNum))