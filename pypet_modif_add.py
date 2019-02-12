
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
game = ["(╯#°□°#）╯︵ ┻━┻ (❤)", "(╯#‾□‾#）╯ ︵ ┻━┻ ((❤))"]
hunger = ["(╯‾□‾）╯ ︵ ┻━┻ (j'ai faim !)", "(╯+.+）╯︵ ┻━┻ (je vais te tuer !!!... puis te bouffer)"]
mad = ["(╯>□<）╯︵ ┻━┻ (tu m'énerves !)", "(╯✖⊙▂⊙）╯︵ ┻━┻ (va te faire foutre !!!)"]
chifumi = ["pierre", "papier", "ciseau"]


#Stat
hungry=True
hug=False


#Hungry gestion

lock = threading.Lock()

def hungergestion():
    global weight
    if weight > 0:
        threading.Timer(1, hungergestion).start()  
        lock.acquire()
        weight = - 50
        lock.release()
        hungry=True

threading.Timer(1,hungergestion).start()

lock.acquire()


#Age gestion



#Program

def startup_pypet():
    print ("Bienvenue " + master)
    print ("Je m'appelle " + name)
    print ()
    if hungry:
         print(photo)
    else:
         print(random.choice(hunger))
    print()

def pypet_stats():
    print ("Age : " + str(age))
    print ("Poids : " + str(weight) + " gramme(s)")
    print ("Attachement : "+ str(cuddle))
    print ("Niveau de fatigue : " + str(sleep))
    print ()
    print("Note :")
    if hungry:
        print(random.choice(hunger))
        print("Bidule a faim et il te mangera si tu ne te dépêches pas de le nourrir !")
    else:
        print(photo)
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


    #nourrir le pypet
    elif user_input == "feed":
        print("ლ(´ڡ`ლ) ︵ ┻━┻ (Chomp chomp chomp !!)")
        weight = int(weight) + 5
        cuddle = int(cuddle) + 1
        print("\n Bidule à bien mangé, il fait maintenant " + str(weight) + " grammes tout mouillés")
        hungry=False
        print ("*bloups* Puisqu'il n'a pas faim, il t'ignore superbement !")


    #jouer avec le pypet
    elif user_input == "play":
        if hungry == False and sleep > 0:
            print(random.choice(game))
            print("*Bidule court après les escargots* uff uff uff !!!")
            weight = int(weight) - 5
            print("\n Bidule à bien courru, il fait maintenant " + str(weight) + " grammes tout mouillés")
            hungry=True
            sleep = int(sleep) - 1
            print ("*uffff* Essouflé et fatigué, il t'ignore superbement !")
        else:
            print(photo)
            print("Bidule est trop fatigué pour jouer... fiche lui un peu la paix, ok !")


    #jouer à chifumi
    elif user_input == "chifumi":
        user_input = input('>')
        bchoice= random.choice(chifumi)
        print(bchoice)
        
        if user_input == "pierre":
            if bchoice == "papier":
                print("perdu !")
            if bchoice == "pierre":
                print("égalité !")
            else: #le joueur choisi papier
                print("Tu as battu Bidule... bravo, maintenant il va partir bouder !")

        if user_input == "papier":
            if bchoice == "ciseau":
                print("perdu !")
            if bchoice == user_input:
                print("égalité !")
            else: #le joueur choisi pierre
                print("Tu as battu Bidule... bravo, maintenant il va partir bouder !")

        else: 
            if bchoice == "pierre":
                print("perdu !")
            if bchoice == user_input:
                print("égalité !")
            else: #le joueur choisi ciseau
                print("Tu as battu Bidule... bravo, maintenant il va partir bouder !")



    #faire dormir le pypet
    elif user_input == "sleep":
        if sleep < 5:
            print("*Bidule dort à point fermé* ! (╯-□-）╯ zzzzzz")
            time.sleep(180)
            sleep = int(sleep) +2
            hungry=True
        else:
            print("Bidule n'a pas envie de dormir... fiche lui un peu la paix, ok !")



    #gestion des erreurs
    else:
        print ("(╯✖⊙▂⊙）╯︵ ┻━┻ (tu ne pourrais pas parler meilleur... ?!)")


    
    
#message si l'utilisateur quitte le programme
print("ne reviens pas trop vite <3 ")
