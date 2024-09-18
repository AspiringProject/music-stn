score = 0

import random
import time

sign = "qwerty"

print("You must register for an account before you can sign in")

namef = input("What is your first name?: ")
namel = input("What is your last name?: ")
dob = input("What is your year of birth?: ")

userpass = namef[0]+namel+dob[2]+dob[3]
print("Your password is:",userpass)

print("Please sign in")
while sign != userpass:
    sign = input("What is your password?")
    if sign != userpass:
        print("Try again")

file = open("musiclist.txt", "r")
for line in file:
    line = file.readlines()
    choice = random.choice(line)
    data = choice.split(",")
print (data[1],data[2])
file.close()

set chances to 2
ask the user to guess the song
if song == data[0] and chances == 2:
    award score and provide message
elif song correct and chances = 1:
    award score and provide mesaage

chances = 2

while chances >= 1:
    ans = input("What is the answer?: ").title()
    if ans == data[0]:
        score = score+1
        print("                               ……….")
        print("                      ……………….......")
        print("                   ……       ✨           …")
        print("              …    ✨                ✨     ….")
        print("         ……              𝐜𝐨𝐧𝐠𝐫𝐚𝐭s             ……")
        print("    ………            👏    🎉   👍           ………")
        print("         ……✨           ◝(ᵔᵕᵔ)◜     ✨   ……")
        print("              ……                             …….")
        print("                   ……        ✨        ….")
        print("                         ……………....")
        print("                              …….")
        print("              Well done! you got it right!")
        print("                Your score is now:",score)
        chances = -5
    else:
        chances = chances-1
        print("That is wrong. You now have",chances,"chance")
while chances == 0:
    print("Womp womp, the answer was:",data[0])
    chances = -5
    
    
    


