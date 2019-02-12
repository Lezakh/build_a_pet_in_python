
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
cuddle= - 5
sleep = 10


def cuddle_level():
    if cuddle < 0:
        print("Pour l'instant, il te déteste!")
    elif cuddle == 0:
        print("Pour l'instant, il te supporte... a peu près")
    elif cuddle < 5:
        print("Actuellement, il t'aime un peu")
    elif cuddle < 10:
        print("Actuellement, il t'aime beaucoup")
    elif cuddle < 15:
        print("Actuellement, il t'aime passionnement")
    elif cuddle < 20:
        print("Actuellement, il t'aime à la folie...")
    elif cuddle > 30:
        print("Y'a pas, il l'a trop vu... Je parle bien évidemment de ton minoi ! Du coup, il ne t'aime plus du tout... De nouveau !")   



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
        weight -= 50
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
    print ("Poids : " + str(weight) + " grammes")
    print (cuddle_level())
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
    user_input = input('> ')
    
    if user_input == "quit":
        terminate=True

    elif user_input == "stats":
        pypet_stats()
        

    #discuter
    elif user_input == "chat":
        if hungry == False:
            cuddle = cuddle + 1
            print(random.choice(happy))
        else:
            cuddle = cuddle - 1
            print(random.choice(mad))
        

    #obtenir l'heure
    elif user_input == "time":
        if hungry == False:
            print(today)
        else:
            print(random.choice(mad))


    #nourrir le pypet
    elif user_input == "feed":
            if weight < 500:
                print("ლ(´ڡ`ლ) ︵ ┻━┻ (Chomp chomp chomp !!)")
                weight = int(weight) + 5
                cuddle = int(cuddle) + 1
                print("\n Bidule à bien mangé, il fait maintenant " + str(weight) + " grammes tout mouillés")
                hungry=False
                print ("*bloups* Puisqu'il n'a pas faim, il t'ignore superbement !")
            else:
                print(photo)
                print("Tu n'essaierais pas de gaver ce pauvre Bidule... fiche lui donc un peu la paix, veux-tu ?")


    #jouer avec le pypet
    elif user_input == "play":
        if hungry == False and sleep > 0 and cuddle > 0:
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


    #jouer à shifumi
    elif user_input == "shifumi":
        if hungry == False and sleep > 0 and cuddle > 0:

            continuer = True
            while continuer == True:
            
                user_input = input('\n > ')

                bchoice= random.choice(chifumi)
                print()
                print(bchoice)
                print()

                if (user_input == bchoice):
                    print("égalité... essaie encore ;)")
                elif (user_input == "pierre" and bchoice == "ciseau"):
                    cuddle = cuddle - 1
                    print("Tu as gagné... Bidule ne voudra certainement plus jouer avec toi maintenant !")
                elif (user_input == "papier" and bchoice == "pierre"):
                    cuddle = cuddle - 1
                    print("Tu as gagné... Bidule ne voudra certainement plus jouer avec toi maintenant !")
                elif (user_input == "ciseau" and bchoice == "papier"):
                    cuddle = cuddle - 1
                    print("Tu as gagné... bidule ne voudra certainement plus jouer avec toi maintenant !")
                else: 
                    cuddle = cuddle + 1
                    print("Bidule t'a écrasé... tu peux aller pleurer !")

                choice = input ("\n Veux-tu continuer de jouer avec moi ? ")
                if choice == "oui" and cuddle > 0:
                    continuer = True
                else:
                    continuer = False
                    print("De toute façon, Bidule n'avait plus envie de jouer avec toi !") 

            
        else:
            print(photo)
            print("Bidule est trop fatigué pour jouer... fiche lui un peu la paix, ok !")


    #faire dormir le pypet
    elif user_input == "sleep":
        if sleep < 5:
            print("*Bidule dort à poings fermés* ! (╯-□-）╯ zzzzzz")
            time.sleep(180)
            sleep = int(sleep) +5
            hungry=True
            print("Bidule vient de se réveiller... Et il a faim !!!")
        else:
            print("Bidule n'a pas envie de dormir... fiche lui un peu la paix, ok !")



    #gestion des erreurs
    else:
        print ("(╯✖⊙▂⊙）╯︵ ┻━┻ (tu ne pourrais pas parler meilleur... ?!)")


    
    
#message si l'utilisateur quitte le programme
print("ne reviens pas trop vite <3 ")
