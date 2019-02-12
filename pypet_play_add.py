
#pour utiliser la fonction random dans le choix des phrases
import random

#pour faire diminuer ou augmenter la valeur d'une variable avec le temps
import threading,time,sys

#Pour utiliser des informations de temps
from datetime import datetime


#pour créer une interface visuelle
from tkinter import *



#interface graphique
Canvas(width=200, height=200, bg='white').pack(side=TOP, padx=5, pady=5)
Button(text ='Feed').pack(side=LEFT, padx=5, pady=5)
Button(text ='Play').pack(side=RIGHT, padx=5, pady=5)

# entrée
value = StringVar() 
value.set("texte par défaut")
entree = Entry(textvariable=string, width=30)
entree.pack()




#Infos
master="Ophélie"

#general information
today = time.localtime()



#bio pypet
photo= "(╯°□°）╯︵ ┻━┻"
name= "Bidule"


#statistiques pypet
age= datetime.now() - datetime(2019, 2, 5, 12, 0)
weight= 485
cuddle= - 10
sleep = 10


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

canvas:
    def startup_pypet():
        print ("Bienvenue " + master)
        print ("Je m'appelle " + name)

    def pypet_stats():
        print (name + " fait " + str(weight) + " gramme(s)")
        print (str(cuddle) + " : niveau d'affection")
        print (str(sleep) + " : niveau de fatigue")
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
        

    #obtenir l'heure
    elif user_input == "time":
        if hungry == False:
            print(today)
        else:
            print(random.choice(mad))


    #obtenir l'age du pyper
    elif user_input == "age":
        if hungry == False:
            print(age)
        else:
            print(random.choice(mad))


    #nourrir le pypet
    elif user_input == "feed":
        print("chomp chomp chomp !!!")
        weight = int(weight) + 5
        cuddle = int(cuddle) + 1
        print("Bidule à bien mangé, il fait maintenant " + str(weight) + " grammes tout mouillés")
        hungry=False
        print ("*bloups* Puisqu'il n'a pas faim, il t'ignore superbement !")


    #jouer avec le pypet
    elif user_input == "play":
        if hungry == False and sleep > 0:
            print("*Bidule court après les escargots* uff uff uff !!!")
            weight = int(weight) - 5
            print("Bidule à bien courru, il fait maintenant " + str(weight) + " grammes tout mouillés")
            hungry=True
            sleep = int(sleep) - 1
            print ("*uffff* Essouflé et fatigué, il t'ignore superbement !")
        else:
            print("Bidule est trop fatigué pour jouer... fiche lui un peu la paix, ok !")

    #gestion des erreurs
    else:
        print ("(╯✖⊙▂⊙）╯︵ ┻━┻ (tu ne pourrais pas parler meilleur... ?!)")


    
    
#message si l'utilisateur quitte le programme
print("ne reviens pas trop vite <3 ")
