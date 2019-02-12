import random
import threading,time,sys


#Infos
master="Ophélie"

#bio pypet
photo= "(╯°□°）╯︵ ┻━┻"
name= "Bidule"
age= 1
weight= 485



#Phrases
happy = ["(╯・ω・）╯︵ ┻━┻ (je te déteste ❤)", "(╯⌒□⌒）╯︵ ┻━┻ (je te déteste ❤)"]
love = ["(╯#°□°#）╯︵ ┻━┻ (❤)", "(╯#‾□‾#）╯ ︵ ┻━┻ ((❤))"]
hungry = ["(╯‾□‾）╯ ︵ ┻━┻ (j'ai faim !)", "ლ(´ڡ`ლ) ︵ ┻━┻ (j'ai faim !!!)", "(╯+.+）╯︵ ┻━┻ (je vais te tuer !!!... puis te bouffer)"]
mad = ["(╯>□<）╯︵ ┻━┻ (tu m'énerves !)", "(╯✖⊙▂⊙）╯︵ ┻━┻ (va te faire foutre !!!)"]



#Stat
hungry=True
hug=False


#Hungry gestion

lock = threading.Lock()

def hunger():
    global weight
    if weight > 0:
        threading.Timer(1, hunger).start()  
        lock.acquire()
        weight = - 50
        lock.release()
        hungry=True

threading.Timer(1,hunger).start()

lock.acquire()


#Age gestion



#Program


def startup_pypet():
    print ("Bienvenue " + master)
    print ("Je m'appelle " + name)

def pypet_stats():
    print (name + " fait " + str(weight) + " gramme(s)")
    if hungry:
        print("Bidule a faim et il te mangera si tu ne te dépêches pas de le nourrir !")
    else:
        print("*bloups* Puisqu'il n'a pas faim, il t'ignore superbement !")
        print ("... Il se demande d'ailleurs pourquoi tu traines encore vers lui")



#Program
startup_pypet()

pypet_stats()

terminate=False

while not terminate:
    print("__________________________________________")
    user_input = input('>')
    
    if user_input == "quit":
        terminate=True

    elif user_input == "stats":
        pypet_stats()

    #discuter
    elif user_input == "chat":
        if hungry == False:
            print(random.choice(happy))
        else:
            print(random.choice(mad))
        

    #nourrir le pypet
    elif user_input == "feed":
        print("chomp chomp chomp !!!")
        weight = int(weight) + 5
        print("Bidule à bien mangé, il fait maintenant " + str(weight) + " grammes tout mouillés")
        hungry=False
        print ("*bloups* Puisqu'il n'a pas faim, il t'ignore superbement !")

    #jouer avec le pypet
    elif user_input == "play":
        print("*Bidule court après les escargots* uff uff uff !!!")
        weight = int(weight) - 5
        print("Bidule à bien courru, il fait maintenant " + str(weight) + " grammes tout mouillés")
        hungry=True
        print ("*uffff* Essouflé et fatigué, il t'ignore superbement !")

    #gestion des erreurs
    else:
        print ("(╯✖⊙▂⊙）╯︵ ┻━┻ (tu ne pourrais pas parler meilleur... ?)")


    
    
#message si l'utilisateur quitte le programme
print("ne reviens pas trop vite <3 ")
