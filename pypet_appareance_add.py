#Fonctions importées

import random #fonction random dans le choix des phrases

import threading,time,sys #pour faire diminuer ou augmenter la valeur d'une variable avec le temps

from datetime import datetime #Pour utiliser des informations de temps

import os #pour changer la localisation du fichier
os.chdir("F:\Memory") #pour accéder au dossier "mémoire"

import pickle #sert à importer et enregistrer des objets dans des fichiers





#Basics informations______________________________


#Master's name
master="Ophélie"

#Time information
today = time.localtime()




#Bio pypet
name= "Bidule"

def photo():

    print('         _____  _ ')
    print('      __)     \ )\ ') 
    print("   __)       _/   \ ") 
    print(" _)       _/    _/''--._ ")
    print("/__     \___.-'    {>(9 / ")
    print(" )__        ;-...;__;-'' ")
    print("    )__      /)  /|)) ")
    print("       )_   / \/\/ )// ")
    print("         )_/ ")







#Ajout de la mémoire - récupération des données enregistrer

with open('bmemory', 'rb') as fichier:
    memory = pickle.Unpickler(fichier)
    bstats = memory.load()
    #Lecture des objets contenus dans le fichier...


#statistiques pypet
age= datetime.now() - datetime(2019, 2, 5, 12, 0)
weight = bstats [0]
cuddle = bstats [1] 
sleep = bstats [2]
hungry= bstats [3]

sleep_level_max = 10



#Fonction gérant l'affichage des informations du pypet

def cuddle_level():
    if cuddle <= 0:
        print("Niveau d'affection : ♡")
    elif cuddle < 5:
        print("Niveau d'affection : ❤")
    elif cuddle < 10:
        print("Niveau d'affection : ❤❤")
    elif cuddle < 15:
        print("Niveau d'affection : ❤❤❤")
    elif cuddle < 20:
        print("Niveau d'affection : ❤❤❤❤") 



def sleep_level():
    if sleep >5:
        print("Niveau d'énergie : " + ("▰"*sleep) +("▱"* (int(sleep_level_max) - int(sleep))))
    else:
        print("Niveau d'énergie : " + ("▰"*sleep) +("▱"* (int(sleep_level_max) - int(sleep))))




def startup_pypet():
    print ("Bienvenue " + master)
    print ("Je m'appelle " + name)
    print ()
    print()

def pypet_stats():
    photo()
    print()
    print ("Age : " + str(age))
    print ("Poids : " + str(weight) + " grammes")
    cuddle_level()
    sleep_level()
    print ()
    if hungry:
        print(random.choice(hunger))
        print("Bidule a faim et il te mangera si tu ne te dépêches pas de le nourrir !")
    else:
        print("*bloups* Puisqu'il n'a pas faim, il t'ignore superbement !")
        print ("... Il se demande d'ailleurs pourquoi tu traines encore vers lui")



#Hungry gestion



#Age gestion



#Phrases_humor
happy = ["(╯・ω・）╯︵ ┻━┻ (je te déteste ❤)", "(╯⌒□⌒）╯︵ ┻━┻ (je te déteste ❤)"]
game = ["(╯#°□°#）╯︵ ┻━┻ (❤)", "(╯#‾□‾#）╯ ︵ ┻━┻ ((❤))"]
hunger = ["(╯‾□‾）╯ ︵ ┻━┻ (j'ai faim !)", "(╯+.+）╯︵ ┻━┻ (je vais te tuer !!!... puis te bouffer)"]
mad = ["(╯>□<）╯︵ ┻━┻ (tu m'énerves !)", "(╯✖⊙▂⊙）╯︵ ┻━┻ (va te faire foutre !!!)"]

#Liste game shifumi
shifumi = ["pierre", "papier", "ciseau"]


#Diece_game
bdiece = [1, 2, 3, 4, 5, 6]
pdiece = [1, 2, 3, 4, 5, 6]






#Program_________________________________________

startup_pypet()

pypet_stats()

terminate=False

while not terminate:
    print("\n ◄■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■► \n")
    user_input = input('➜ ')
    
    if user_input == "quit":
        terminate=True

    elif user_input == "stats":
        pypet_stats()
        

    #discuter avec le pypet
    elif user_input == "chat":
        if hungry == False:
            cuddle = cuddle + 1
            print(random.choice(happy))
        else:
            cuddle = cuddle - 1
            print(random.choice(mad))

    #câliner le pypet
    elif user_input == "hug":
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
            if weight < 500 or hungry == True:
                weight = int(weight) + 5
                cuddle = int(cuddle) + 1
                print()
                print("Chomp chomp chomp !!")
                print("\n Bidule à bien mangé, il fait maintenant " + str(weight) + " grammes tout mouillés")
                hungry=False
                print ("*bloups* Puisqu'il n'a pas faim, il t'ignore superbement !")
            else:
                photo()
                print("Tu n'essaierais pas de gaver ce pauvre Bidule... ")


    #jouer avec le pypet
    elif user_input == "play":
        if hungry == False and sleep > 0 and cuddle > 0:
            print(random.choice(game))
            print("*Bidule court après les escargots* uff uff uff !!!")
            weight = int(weight) - 10
            print("\n Bidule à bien courru, il fait maintenant " + str(weight) + " grammes tout mouillés")
            hungry=True
            sleep = int(sleep) - 1
            print ("*uffff* Essouflé et fatigué, il t'ignore superbement !")
        else:
            photo()
            print("Bidule est trop fatigué pour jouer... ")


    #jouer à shifumi
    elif user_input == "shifumi":
        if hungry == False and sleep > 0 and cuddle > 0:

            continuer = True
            while continuer == True:
            
                user_input = input('\n ➜ ')

                bchoice= random.choice(shifumi)
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
                    print("Tu as gagné... Bidule ne voudra certainement plus jouer avec toi maintenant !")
                else: 
                    cuddle = cuddle + 1
                    print("Bidule t'a écrasé... tu peux aller pleurer !")

                choice = input ("\n Veux-tu continuer de jouer avec Bidule ? ")
                if choice == "oui" and cuddle > 0:
                    continuer = True
                else:
                    continuer = False
                    print("De toute façon, Bidule n'avait plus envie de jouer avec toi !") 

            
        else:
            photo()
            print("Bidule est trop fatigué pour jouer... ")


    #jouer au jeu de dés
    elif user_input == "diece":
        if hungry == False and sleep > 0 and cuddle > 0:
            continuer = True

            while continuer == True:

                bdchoice = random.choice(bdiece)
                pdchoice = random.choice(pdiece)

                print(master + ' : ')
                if pdchoice == 1:
                    print('⚀')

                elif pdchoice == 2:
                    print('⚁')

                elif pdchoice == 3:
                    print('⚂')

                elif pdchoice == 4:
                    print('⚃')

                elif pdchoice == 5:
                    print('⚄')

                elif pdchoice == 6:
                    print('⚅')


                print(name + ' : ')
                if bdchoice == 1:
                    print('⚀')

                elif bdchoice == 2:
                    print('⚁')

                elif bdchoice == 3:
                    print('⚂')

                elif bdchoice == 4:
                    print('⚃')

                elif bdchoice == 5:
                    print('⚄')

                elif bdchoice == 6:
                    print('⚅')
                    

                if bdchoice == pdchoice:
                    print("\n égalité... essaie encore ;)")
                elif bdchoice > pdchoice:
                    cuddle = cuddle + 1
                    print("\n Bidule à gagné... tu peux aller te rhabiller")
                else:
                    cuddle = cuddle - 1
                    print("\n Bravo, tu as gagné... mais Bidule risque de ne plus vouloir jouer avec toi !")


                choice = input ("\n Veux-tu continuer de jouer avec moi ? ")
                if choice == "oui" and cuddle > 0:
                    continuer = True
                else:
                    continuer = False
                    print("De toute façon, Bidule n'avait plus envie de jouer avec toi !") 


        else:
            photo()
            print("Bidule est trop fatigué pour jouer... fiche lui un peu la paix, ok !")

    

    #faire dormir le pypet
    elif user_input == "sleep":
        if sleep <= 5:
            photo()
            print("*Bidule dort à poings fermés* ! zzzzzz")
            time.sleep(180)
            sleep = int(sleep) +5
            hungry=True
            print("Bidule vient de se réveiller... Et il a faim !!!")
        else:
            print("Bidule n'a pas envie de dormir... fiche lui un peu la paix, ok !")



    #gestion des erreurs
    else:
        print ("(╯✖⊙▂⊙）╯︵ ┻━┻ (tu ne pourrais pas parler meilleur... ?!)")



#Enregistrement des statistiques du pypet_________
        
bstats = [weight, cuddle, sleep, hungry]

with open('bmemory', 'wb') as fichier: #ouvre le fichier
    memory = pickle.Pickler(fichier) #appelle la fonction pickel pour dire qu'il va écrire dans le fichier
    memory.dump(bstats)
    
    
#Message si l'utilisateur quitte le programme_____

print("ne reviens pas trop vite ❤ ")
