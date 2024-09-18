import random
import time
score = int(0)

file = open("musiclist.txt", "r")
for line in file:
    line = file.readlines()
    choice = random.choice(line)
    data = choice.split(",")
file.close()

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

print("1. Play music quiz")
print("2. Enter STN")
gme = input("What would you like to do?: ")
chances = int(2)
if gme == "1":
    zzyz = "yes"
    while zzyz == "yes":
        import time
        file = open("musiclist.txt", "r")
        for line in file:
            line = file.readlines()
            choice = random.choice(line)
            data = choice.split(",")
        file.close()
        print (data[1],data[2])
        while chances >= 1:
            ans = input("What is the answer?: ").title()
            if ans == data[0]:
                score = score+1
                print("""                               ……….""")
                print("""                     ……………….......""")
                print("""                   ……       ✨           …""")
                print("""              …    ✨                ✨     ….""")
                print("""        ……              𝐜𝐨𝐧𝐠𝐫𝐚𝐭s            ……""")
                print("""    ………            👏    🎉   👍           ………""")
                print("""         ……✨           ◝(ᵔᵕᵔ)◜     ✨   ……""")
                print("""              ……                             …….""")
                print("""                   ……        ✨        ….""")
                print("""                         ……………....""")
                print("""                              …….""")
                print("""              Well done! you got it right!""")
                print("""                Your score is now:""",score)
                chances = -5
            else:
                chances = chances-1
                print("That is wrong. You now have",chances,"chance")
        while chances == 0:
            print("Womp womp, the answer was:",data[0])
            chances = chances-5
        zzyz = input("Play again?: ")

elif gme == "2":

        
    print("Welcome to the STN (Score Tracker Network)")
    print("1. Display high scores")
    print("2. Add a new high score")
    print("3. Clear all high scores")
    print("4. Quit") 

    optn = input("What would you like to do?: ")
    if optn == "1":
        file = open("highScores.txt", "r")
        cont = file.read()
        print(cont)
        file.close()
        optn = "0"

    elif optn == "2":
        name = input("What is your name?: ")
        score = input("What is your high score?: ")
        file = open("highScores.txt", "a")
        file.write(name + ","+score+"\n")
        file.close()
        print("Your score has been added")
        optn = "0"

    elif optn == "3":
        open("highScores.txt", "w").close()
        print("All scores erased")
        optn = "0"

    elif optn == "4":
        print("STN will close in 3..")
        time.sleep(1)
        print("2..")
        time.sleep(1)
        print("1..")
        time.sleep(1)
        exit()
    else:
        exit()
else:
    exit()
