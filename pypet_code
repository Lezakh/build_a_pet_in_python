#Import the used module in the program

import random
import threading,time,sys


#About you
master="Ophélie"

#Bio of pypet
photo= "╯°□°╯"
name= "Bidule"
age= 1
weight= 500
hungry=True
hug=False


#Phrases used to display random sentence with the random module
happy = ["(╯・ω・）╯︵ ┻━┻ (je te déteste ❤)", "(╯⌒□⌒）╯︵ ┻━┻ (je te déteste ❤)"]
love = ["(╯#°□°#）╯︵ ┻━┻ (❤)", "(╯#‾□‾#）╯ ︵ ┻━┻ ((❤))"]
hungry = ["(╯‾□‾）╯ ︵ ┻━┻ (j'ai faim !)", "ლ(´ڡ`ლ) ︵ ┻━┻ (j'ai faim !!!)", "(╯+.+）╯︵ ┻━┻ (je vais te tuer !!!... puis te bouffer)"]
mad = ["(╯>□<）╯︵ ┻━┻ (tu m'énerves !)", "(╯✖⊙▂⊙）╯︵ ┻━┻ (va te faire foutre !!!)"]




#Function used bellow in program


def startup_pypet():
    print ("Bienvenue " + master)

def pypet_stats():
    print ("Not hello, it's " + name)
    print(photo)
    print (name + " fait " + str(weight) + " gramme(s)")
    if hungry:
        print("Bidule a faim et il te mangera si tu ne te dépêches pas de le nourrir !")
    else:
        print("*bloups* Puisqu'il n'a pas faim, il t'ignore superbement !")





#Program
startup_pypet()
pypet_stats()

terminate=False


while not terminate:
    print("__________________________________________")
    user_input = input('>')
    
    if user_input == "quit": #go to the end of the program and close it
        terminate=True

    elif user_input == "stats": #give the actual stats of the pypet
        pypet_stats()
        

    #chat with the pypet by picking a random sentence in the list happy
    elif user_input == "chat": 
        print (random.choice(happy))

    
    #feed the pypet, add 5 pound to the weight and turn the hungry variable to false
    elif user_input == "feed": 
        print("chomp chomp chomp !!!")
        weight = int(weight) + 5
        hungry=False

    #if something wrong is written
    else:
        print ("tu ne pourrais pas parler meilleur... ?")


    
    
#message si l'utilisateur quitte le programme
print("ne reviens pas trop vite <3 ")
