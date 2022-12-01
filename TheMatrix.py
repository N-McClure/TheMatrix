#TheMatrix:

import random as r
import time
import colorama
from colorama import Fore, Back,Style
colorama.init(autoreset=True)

symbols = ['0','1', " "," "]
line = []
counter = 0

#Intro:
time.sleep(1)
user = input("enter your name: ")
print(f"{Fore.GREEN}Hello " + user)
time.sleep(5)

#Choice:
print(f"{Fore.GREEN}you have 2 choices...Red or Blue?")
time.sleep(2)
print(f"{Fore.BLUE}Blue = you continue to live your life. Completely oblivious to the truth.")
time.sleep(2)
print(f"{Fore.GREEN}or")
time.sleep(2)
print(f"{Fore.RED}Red = i show you just how deep the rabbit hole truly goes.")
time.sleep(2)
choice = input("the choice is yours...Red or Blue?: ")

if choice.lower() == 'blue':
    print()
    print(f"{Fore.GREEN}Good bye " + user )
    time.sleep(5)
    exit()

if choice.lower() == 'red':
    print()
    print(f"{Fore.GREEN}once you go in, there is no turning back.")
    print()
    time.sleep(2)
    print(f"{Fore.GREEN}let us begin... and jump into The Matrix.")
    time.sleep(5)

    for i in range(118):
        x = r.randint(0, 3)
        line.append(symbols[x])

        counter += i
    for i in range (10000):
        
        if counter % 5 -- 0:
            r_symbols = [r.randint(0, 117) for x in range (10)]

            for i in r_symbols:
                line[i] = symbols[r.randint(0, 3)]

        print(*line)
        counter += i
        time.sleep(0.01)
