#importe la librairie graphique

from tkinter import *


#Importe les fonctions nécessaire au fonctionnement du programme

import random #fonction random dans le choix des phrases
import threading,time,sys #pour faire diminuer ou augmenter la valeur d'une variable avec le temps
from datetime import datetime #Pour utiliser des informations de temps
import os #pour changer la localisation du fichier
os.chdir("F:\Memory") #pour accéder au dossier "mémoire"
import pickle #sert à importer et enregistrer des objets dans des fichiers


#créer une fenêtre principale

fenetre = Tk()


#Mise à jour de la fênetre

def delete_frame_texte():
    for widget in frame_texte.winfo_children(): #winfo_children parcours le widget
        widget.pack_forget() #.pack_forget permet d'effacer tout ce qu'il contient si la fonction .pack a été utilisée

def delete_frame_photo():
    for widget in frame_photo.winfo_children(): #winfo_children parcours le widget
        widget.pack_forget() #.pack_forget permet d'effacer tout ce qu'il contient si la fonction .pack a été utilisée

def delete_frame_button():
    for widget in frame_button.winfo_children(): #winfo_children parcours le widget
        widget.pack_forget() #.pack_forget permet d'effacer tout ce qu'il contient si la fonction .pack a été utilisée


#Ajout de la mémoire - récupération des données enregistrer

with open('bmemory', 'rb') as fichier:
    memory = pickle.Unpickler(fichier)
    bstats = memory.load()
    #Lecture des objets contenus dans le fichier...



#Variables de base

##statistiques du pypet
name = "Bidule"

###calcul de l'âge

def age():
    from datetime import date

    birthday = datetime(2019, 2, 5, 12, 0)
    actual_date = datetime.now()
    age_calc = actual_date - birthday
    age_bidule = age_calc.days #permet d'afficher les jours sur la différence de deux dates
    age_s = Label(frame_texte, bg ="white", text="Age : " + str(age_bidule) + " jours")
    age_s.pack(fill= BOTH)
    

#age= datetime.now() - datetime(2019, 2, 5, 12, 0) #ancien affichage de l'âge, trop précis
weight = bstats [0]
cuddle = bstats [1] 
sleep = bstats [2]
hungry= bstats [3]

sleep_level_max = 10


##Phrases d'humeur
happy = ["(╯・ω・）╯︵ ┻━┻ (je te déteste ❤)", "(╯⌒□⌒）╯︵ ┻━┻ (je te déteste ❤)"]
game = ["(╯#°□°#）╯︵ ┻━┻ (❤)", "(╯#‾□‾#）╯ ︵ ┻━┻ ((❤))"]
hunger = ["(╯‾□‾）╯ ︵ ┻━┻ (j'ai faim !)", "(╯+.+）╯︵ ┻━┻ (je vais te tuer !!!... puis te bouffer)"]
mad = ["(╯>□<）╯︵ ┻━┻ (tu m'énerves !)", "(╯✖⊙▂⊙）╯︵ ┻━┻ (va te faire foutre !!!)"]




#Apparence visuel du pypet

frame_photo = Frame(bd = 0, height="600", width="600")
frame_photo.pack(side = TOP)

def photo():
    photo = PhotoImage(file="bidule_nb.gif") #je créer la variable photo
    label_photo = Label(frame_photo, image=photo) #je créer le label de mon image, je peux définir la couleur de fond avec bg="couleur"
    label_photo.image = photo # je garde une référence pour que le garbage collector de python n'empêche pas son afficage
    label_photo.pack() # .pack permet l'affichage du label sélectionné


def photo_sleep():
    delete_frame_photo()
    photo_sleep_i = PhotoImage(file="bidule_sleep_ani.gif")
    label_photo_sleep = Label(frame_photo, image=photo_sleep_i)
    label_photo_sleep.image = photo_sleep_i
    label_photo_sleep.pack()
    label_photo_sleep.after(10000, delete_frame_photo)
    label_photo_sleep.after(10000, photo)


def photo_feed():
    delete_frame_photo()
    photo_eat_i = PhotoImage(file="bidule_eat.gif")
    label_photo_eat = Label(frame_photo, image=photo_eat_i)
    label_photo_eat.image = photo_eat_i
    label_photo_eat.pack()
    label_photo_eat.after(10000, delete_frame_photo)
    label_photo_eat.after(10000, photo)
    


#Affichage du visuel à l'entrée
photo()


#Text d'entrée de programme

frame_texte = Frame(bd = 0, height="50", bg="white")
frame_texte.pack(fill = BOTH)


#texte d'entrée

master = 'Ophélie'
reaction = Label(frame_texte, bg="white", text="Encore toi " + master + " !? Qu'est-ce que tu me veux cette fois ?")
reaction.pack(fill = BOTH)



#fonctions du pypet

## Afficher les statistiques


def pypet_stats():
    delete_frame_texte()
    presentation = Label(frame_texte, bg ="white", text="Nom : " + name)
    age()
    poids_s = Label(frame_texte, bg ="white", text="Poids : " + str(weight) + " grammes")
    poids_s.pack(fill = BOTH)

    if cuddle <= 0:
        cuddle_s = Label(frame_texte, bg="white", text="Niveau d'affection : ♡")
        cuddle_s.pack(fill = BOTH)
    elif cuddle < 5:
        cuddle_s = Label(frame_texte, bg="white", text="Niveau d'affection : ❤")
        cuddle_s.pack(fill = BOTH)
    elif cuddle < 10:
        cuddle_s = Label(frame_texte, bg="white", text="Niveau d'affection : ❤❤")
        cuddle_s.pack(fill = BOTH)
    elif cuddle < 15:
        cuddle_s = Label(frame_texte, bg="white", text="Niveau d'affection : ❤❤❤")
        cuddle_s.pack(fill = BOTH)
    else:
        cuddle_s = Label(frame_texte, bg="white", text="Niveau d'affection : ❤❤❤❤")
        cuddle_s.pack(fill = BOTH)

    if sleep >5:
        sleep_s = Label(frame_texte, bg="white", text="Niveau d'énergie : " + ("▰"*sleep) +("▱"* (int(sleep_level_max) - int(sleep))))
        sleep_s.pack(fill = BOTH)
    else:
        sleep_s = Label(frame_texte, bg="white", text="Niveau d'énergie : " + ("▰"*sleep) +("▱"* (int(sleep_level_max) - int(sleep))))
        sleep_s.pack(fill = BOTH)


## Nourrir
def feed():
    delete_frame_texte()
    
    global hungry
    global weight
    global cuddle

    if weight < 500 or hungry == True:
        delete_frame_photo()
        photo_feed()
        weight = int(weight) + 5
        cuddle = int(cuddle) + 1
        manger = Label(frame_texte, bg = "white", text="Bidule a bien mangé, il fait maintenant " + str(weight) + " grammes tout mouillées. \n *bloups* Puisqu'il n'a pas faim, il t'ignore superbement !")
        hungry=False
        manger.pack(fill = BOTH)
    else:
        manger = Label(frame_texte, bg = "white", text="Inutile d'essayer de me gaver... ! Monstre !!!")
        manger.pack(fill = BOTH)


## Parler
def chat():
    delete_frame_texte()
    global cuddle

    if hungry == False:
        cuddle= int(cuddle) + 1
        chat_h = Label(frame_texte, bg ="white", text=random.choice(happy))
        chat_h.pack(fill = BOTH)
        
    else:
        cuddle= int(cuddle) - 1
        chat_h = Label(frame_texte, bg ="white", text=random.choice(mad))
        chat_h.pack(fill = BOTH)


## Jouer
def play():
    delete_frame_texte()
    global hungry
    global cuddle
    global weight
    global sleep
    global frame_button
    
    if hungry == False and weight > 450 and sleep > 0 and cuddle > 0:
        jouer = Label(frame_texte, bg="white", text="*échauffement en cours " + random.choice(game) + " \n*Bidule court après les escargots* uff uff uff !!! \n \n Le menu des jeux va s'afficher dans un instant...")

        weight = int(weight) - 10
        #hungry=True
        sleep = int(sleep) - 1

        jouer.pack(fill = BOTH)
        jouer.after(5000, lambda: jouer.config(text="Bidule est prêt à t'écraser ! \n A quoi souhaites-tu le défier ?"))

        frame_button.after(5000, menu_jeux)
        
    else:
        jouer = Label(frame_texte, bg = "white", text="Bidule a trop faim pour jouer... ")
        jouer.pack(fill = BOTH)


#Dormir
def dormir():
    delete_frame_texte()
    global sleep
    global hungry
    
    if sleep <= 5:
        photo_sleep()
        sleep_s = Label(frame_texte, bg ="white", text="*Bidule dort à poings fermés* ! zzzzzz")
        sleep_s.pack(fill = BOTH)
        sleep = int(sleep) +5
        hungry=True
        sleep_s.after(10000, lambda: sleep_s.config(text="Bidule vient de se réveiller... Et il a faim !!!"))

    else:
        sleep_s = Label(frame_texte, bg ="white", text="Bidule n'a pas envie de dormir... fiche lui un peu la paix, ok !")
        sleep_s.pack(fill = BOTH)



#Boutons d'interaction principaux

frame_button = Frame(bd = 0, height=600, width=600)
frame_button.pack(side = LEFT)



def home():
    delete_frame_button()
    delete_frame_texte()

    global reaction
    reaction.pack(fill = BOTH)

    bouton_feed = Button(frame_button, text="Home ", fg="red", command=home)
    bouton_feed.pack(side = LEFT)
    
    bouton_stats = Button(frame_button, text="Stats ", fg="grey", command=pypet_stats)
    bouton_stats.pack(side = LEFT)

    bouton_feed = Button(frame_button, text="Nourrir ", fg="black", command=feed)
    bouton_feed.pack(side = LEFT)

    bouton_chat = Button(frame_button, text="Chat ", fg="black", command=chat)
    bouton_chat.pack(side = LEFT)

    bouton_play = Button(frame_button, text="Jouer ", fg="black", command=play)
    bouton_play.pack(side = LEFT)

    bouton_dormir = Button(frame_button, text="Dormir ", fg="black", command=dormir)
    bouton_dormir.pack(side = LEFT)

    bouton_quitter = Button(frame_button, text=" Quitter", command=fenetre.quit)
    bouton_quitter.pack(side = RIGHT)


home()

#Fonctions liés aux jeux

##shifumi_game

def menu_shifumi():
    delete_frame_button()

    bouton_feed = Button(frame_button, text="Home ", fg="red", command=home)
    bouton_feed.pack(side = LEFT)

    button_rock = Button(frame_button, text="Pierre", fg="black", command=rock)
    button_rock.pack(side = LEFT)

    button_paper = Button(frame_button, text="Papier", fg="black", command=paper)
    button_paper.pack(side = LEFT)

    button_scisor = Button(frame_button, text="Ciseaux", fg="black", command=scisor)
    button_scisor.pack(side = LEFT)


### défini la valeur de 
user_input = StringVar() #garde en mémoire une chaine de caractère

def rock():
    user_input.set('pierre')


def paper():
    user_input.set('papier')


def scisor():
    user_input.set('ciseaux')



    

def shifumi_g():

    delete_frame_texte()
    start_t = Label(frame_texte, bg="white", text="Alors, qu'attends-tu pour jouer... \n Aurais-tu peur de perdre contre moi ?")
    start_t.pack(fill= BOTH)

    shifumi = ["pierre", "papier", "ciseaux"]
    
    global hungry
    global sleep
    global cuddle
    global user_input

    menu_shifumi()

    frame_texte.wait_variable(user_input) #attends que la variable user_input soit définie

    player_choice = Label(frame_texte, bg="white", text=master + " : " + str(user_input.get()))
    player_choice.pack(fill = BOTH)

    
    bchoice = random.choice(shifumi)
    bchoice_p= Label(frame_texte, bg="white", text="Bidule : " + str(bchoice))
    bchoice_p.pack(fill= BOTH)


    if (user_input.get() == bchoice): #on utilise .get() pour accèder à la valeur de la variable, sinon python retourne py_var0 qui est sa référence
        result_shifumi= Label(frame_texte, bg="white", text="Egalité... tu l'avais presque battu ;)")
        result_shifumi.pack(fill = BOTH)
    elif (user_input.get() == "pierre" and bchoice == "ciseaux"):
        cuddle = cuddle - 1
        hungry = True
        result_shifumi= Label(frame_texte, bg="white", text="Tu as gagné... Bidule ne voudra certainement plus jouer avec toi maintenant !")
        result_shifumi.pack(fill = BOTH)
    elif (user_input.get() == "papier" and bchoice == "pierre"):
        cuddle = cuddle - 1
        hungry = True
        result_shifumi= Label(frame_texte, bg="white", text="Tu as gagné... Bidule ne voudra certainement plus jouer avec toi maintenant !")
        result_shifumi.pack(fill = BOTH)
    elif (user_input.get() == "ciseaux" and bchoice == "papier"):
        cuddle = cuddle - 1
        hungry = True
        result_shifumi= Label(frame_texte, bg="white", text="Tu as gagné... Bidule ne voudra certainement plus jouer avec toi maintenant !")
        result_shifumi.pack(fill = BOTH)
    else: 
        cuddle = cuddle + 1
        result_shifumi= Label(frame_texte, bg="white", text="Bidule t'a écrasé... tu peux aller pleurer !")
        result_shifumi.pack(fill = BOTH)
        

    if hungry == False and cuddle > 0:
        retry = Label(frame_texte, bg="white", text="Veux-tu rejouer ?")
        retry.pack(fill = BOTH)
        delete_frame_button()

        button_yes_s = Button(frame_button, text="Oui", fg="black", command=shifumi_g)
        button_yes_s.pack(side = LEFT)

        button_no_s = Button(frame_button, text="Non", fg="black", command=home)
        button_no_s.pack(side = LEFT)

        frame_texte.wait_variable(user_input)
            
        menu_shifumi()
        frame_texte.wait_variable(button_yes_s)
        shifumi_g()
        

    else:
        frame_texte.after(5000, delete_frame_texte)
        frame_button. after(5000, home)




##diece_game

def menu_diece():
    delete_frame_button()

    button_yes = Button(frame_button, text="Lancer le dès", fg="black", command=diece_g)
    button_yes.pack(side = LEFT)

    button_no = Button(frame_button, text="Quitter", fg="black", command=home)
    button_no.pack(side = LEFT)


def diece_g():

    delete_frame_texte()

    bdiece = [1, 2, 3, 4, 5, 6]
    pdiece = [1, 2, 3, 4, 5, 6]
    global hungry
    global sleep
    global cuddle

    menu_diece()


    bdchoice = random.choice(bdiece)
    pdchoice = random.choice(pdiece)
    
    bdchoice_p = Label(frame_texte, bg="white", text="Dès lancé par Bidule : " + str(bdchoice))
    bdchoice_p.pack(fill = BOTH)
    pdchoice_p =  Label(frame_texte, bg="white", text="Dès lancé par " + master + " : " + str(pdchoice))
    pdchoice_p.pack(fill = BOTH)

    
    if bdchoice == pdchoice:
        diece_result = Label(frame_texte, bg="white", text="Egalité... essaie encore ;)")
        diece_result.pack(fill = BOTH)
        
    elif bdchoice > pdchoice:
        cuddle = cuddle + 1
        diece_result = Label(frame_texte, bg="white", text="Bidule à gagné... tu peux aller te rhabiller")
        diece_result.pack(fill = BOTH)
        
    else:
        cuddle = cuddle - 1
        hungry = True
        diece_result = Label(frame_texte, bg="white", text="Bravo, tu as gagné... \n Maintenant Bidule à faim et refuse de jouer avec toi !")
        diece_result.pack(fill = BOTH)


    if hungry == False and cuddle > 0:
        menu_diece()

    else:
        home()



##hanged_man_game    
def hanged_g():
    print()


#Boutons d'interaction jeux
    

def menu_jeux():
    delete_frame_button()

    bouton_feed = Button(frame_button, text="Home ", fg="red", command=home)
    bouton_feed.pack(side = LEFT)

    bouton_stats = Button(frame_button, text="Shifumi ", fg="black", command=shifumi_g)
    bouton_stats.pack(side = LEFT)

    bouton_feed = Button(frame_button, text="Dès ", fg="black", command=diece_g)
    bouton_feed.pack(side = LEFT)

    bouton_feed = Button(frame_button, text=" Pendu", fg="black", command=hanged_g)
    bouton_feed.pack(side = LEFT)


fenetre.mainloop()


#Enregistrement des statistiques du pypet
        
bstats = [weight, cuddle, sleep, hungry]

with open('bmemory', 'wb') as fichier: #ouvre le fichier
    memory = pickle.Pickler(fichier) #appelle la fonction pickel pour dire qu'il va écrire dans le fichier
    memory.dump(bstats)
    

