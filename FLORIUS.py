import tkinter as tk

import turtle

import random




# Créer une fenêtre d'accueil

accueil = tk.Tk()

accueil.title("Bienvenue à FLORIUS ")



# Fonction pour fermer la fenêtre d'accueil et ouvrir la fenêtre principale

def ouvrir_fenetre_principale():

    accueil.destroy()  # Ferme la fenêtre d'accueil

    fenetre.deiconify()  # Affiche la fenêtre principale


# Label de bienvenue dans la fenêtre d'accueil

label_bienvenue = tk.Label(accueil, text="Bienvenue dans l'univers de FLORIUS,\n une application étonnante qui simule la croissance d'une fleur unique en son genre !\n Imaginez pouvoir contrôler les différents critères qui influencent la floraison, tels que le climat,\n la météo et la luminosité, pour obtenir une fleur totalement personnalisée.\n Chaque choix que vous ferez aura un impact direct sur la croissance de votre fleur,\n ce qui la rendra véritablement unique en son genre.\n Vous serez mis au défi de trouver les facteurs qui influencent les différentes caractéristiques de votre fleur,\n ce qui rendra l'expérience encore plus intéressante.\n Êtes-vous prêt à relever le défi et à créer votre propre chef-d'œuvre floral ?\n Venez découvrir l'univers de FLORIUS dès maintenant !", font=("Arial", 15), bg='lightblue', fg='darkblue')

label_bienvenue.pack(expand=tk.YES, padx=10, pady=10)


# Bouton pour ouvrir la fenêtre principale

bouton_demarrer = tk.Button(accueil, text="Démarrer", font=("Arial", 20), command=ouvrir_fenetre_principale)

bouton_demarrer.pack(padx=10, pady=10)


# Créer une fenêtre principale (cachée)

fenetre = tk.Toplevel()

fenetre.title("FLORIUS")

fenetre.withdraw()  # Cache la fenêtre principale jusqu'à ce qu'elle soit ouverte depuis l'accueil

fenetre.resizable(width=False, height=False)

# Lancer la boucle principale de l'application

accueil.mainloop()


# Créer une fenêtre

fenetre = tk.Tk()

fenetre.title("FLORIUS")

fenetre.resizable(width=False, height=False)

canvas_frame = tk.Frame(fenetre)

canvas_frame.pack(side=tk.RIGHT, padx=10, pady=10)

canvas = tk.Canvas(canvas_frame, width=400, height=600)

canvas.pack()

label1 = tk.Label(fenetre, text="FLORIUS", font=("Arial", 30), bg='lightblue', fg='#96d9bf')

label1.pack(expand=tk.YES)

label1.place(relx=0.5, rely=0, anchor=tk.N)



def get_choices():

    print(climat.get(), saison.get(), condition.get(), nutriments.get(), luminosite.get())



# Catégorie 5 : Luminosité

luminosite_frame = tk.LabelFrame(fenetre, text="Luminosité")

luminosite_frame.pack(padx=10, pady=10)


luminosite = tk.StringVar()

luminosite.set(None)


Faible_button = tk.Radiobutton(luminosite_frame, text="Forte", variable=luminosite, value="Forte", fg="black",

                               bg="#edb47e")

Faible_button.pack(pady=5)


Moyenne_button = tk.Radiobutton(luminosite_frame, text="Moyenne", variable=luminosite, value="Moyenne", fg="black",

                                bg="#edb47e")

Moyenne_button.pack(pady=5)


Forte_button = tk.Radiobutton(luminosite_frame, text="Faible", variable=luminosite, value="Faible", fg="black",

                              bg="#edb47e")

Forte_button.pack(pady=5)


# Catégorie 2 : Saison

saison_frame = tk.LabelFrame(fenetre, text="Saison")

saison_frame.pack(padx=10, pady=10)


saison = tk.StringVar()

saison.set(None)


ete_button = tk.Radiobutton(saison_frame, text="Été", variable=saison, value="Été", fg="black", bg="#edb47e")

ete_button.pack(pady=5)


Printemps_button = tk.Radiobutton(saison_frame, text="Printemps", variable=saison, value="Printemps", fg="black",

                                  bg="#edb47e")

Printemps_button.pack(pady=5)


Automne_button = tk.Radiobutton(saison_frame, text="Automne", variable=saison, value="Automne", fg="black", bg="#edb47e")

Automne_button.pack(pady=5)


# Catégorie 3 : Condition météo

condition_frame = tk.LabelFrame(fenetre, text="Condition météo")

condition_frame.pack(padx=10, pady=10)


condition = tk.StringVar()

condition.set(None)


soleil_button = tk.Radiobutton(condition_frame, text="Soleil", variable=condition, value="Soleil", fg="black",

                               bg="#edb47e")

soleil_button.pack(pady=5)


Unpeudepluie_button = tk.Radiobutton(condition_frame, text="Un peu de pluie", variable=condition,

                                     value="Un peu de pluie",

                                     fg="black", bg="#edb47e")

Unpeudepluie_button.pack(pady=5)


pluiediluvienne_button = tk.Radiobutton(condition_frame, text="Pluie diluvienne", variable=condition,

                                        value="Pluie diluvienne", fg="black", bg="#edb47e")

pluiediluvienne_button.pack(pady=5)


# Catégorie 4 : Nutriments du sol

nutriments_frame = tk.LabelFrame(fenetre, text="Nutriments du sol")

nutriments_frame.pack(padx=10, pady=10)


nutriments = tk.StringVar()

nutriments.set(None)


solnaturellementpauvre_button = tk.Radiobutton(nutriments_frame, text="Utilisation d’engrais", variable=nutriments,

                                               value="Utilisation d’engrais", fg="black", bg="#edb47e")

solnaturellementpauvre_button.pack(pady=5)


solnaturellementriche_button = tk.Radiobutton(nutriments_frame, text="Sol naturellement riche", variable=nutriments,

                                              value="Sol naturellement riche", fg="black", bg="#edb47e")

solnaturellementriche_button.pack(pady=5)


utilisationdengrais_button = tk.Radiobutton(nutriments_frame, text="Sol naturellement pauvre", variable=nutriments,

                                            value="Sol naturellement pauvre", fg="black", bg="#edb47e")

utilisationdengrais_button.pack(pady=5)



def pluie():

    t = turtle.RawTurtle(canvas)

    t.hideturtle()

    t.penup()

    t.hideturtle()

    t.goto(-200, 400)  # coordonnées de départ en haut du canvas

    t.pendown()


    vitesse_pluie = 5

    nombre_lignes_pluie = 800

    longueur_lignes_pluie = 10

    couleur_lignes_pluie = "blue"


    # Créer les lignes de la pluie

    lignes_pluie = []

    for i in range(nombre_lignes_pluie):

        x = random.randint(-1500, 1500)  # plage de valeurs pour x

        y1 = random.randint(-1500, 1500)

        y2 = y1 - longueur_lignes_pluie  # y2 est maintenant en haut du canvas

        ligne = canvas.create_line(x, y1, x, y2, fill=couleur_lignes_pluie)

        lignes_pluie.append(ligne)


    # Fonction de déplacement de la pluie

    def deplacer_pluie():

        # Déplacer chaque ligne de la pluie vers le bas


        for ligne in lignes_pluie:

            canvas.move(ligne, 0, vitesse_pluie)

            if ligne:

                if canvas.coords(ligne)[1] >= 1000:

                    # Si la ligne atteint le bas du canevas, la déplacer au-dessus du canevas

                    canvas.move(ligne, 0, -1000)  # déplacement vers le haut du canvas


        # Appeler la fonction de déplacement de la pluie à nouveau après un délai de 50 millisecondes

        canvas.after(101, deplacer_pluie)


    deplacer_pluie()



def pluie1():

    t = turtle.RawTurtle(canvas)

    t.hideturtle()

    t.penup()

    t.hideturtle()

    t.goto(-200, 400)  # coordonnées de départ en haut du canvas

    t.pendown()


    vitesse_pluie = 5

    nombre_lignes_pluie = 800

    longueur_lignes_pluie = 10

    couleur_lignes_pluie = "blue"


    # Créer les lignes de la pluie

    lignes_pluie = []

    for i in range(nombre_lignes_pluie):

        x = random.randint(-1500, 1500)  # plage de valeurs pour x

        y1 = random.randint(-1500, 1500)

        y2 = y1 - longueur_lignes_pluie  # y2 est  en haut du canvas

        ligne = canvas.create_line(x, y1, x, y2, fill=couleur_lignes_pluie)

        lignes_pluie.append(ligne)


    # Fonction de déplacement de la pluie

    def deplacer_pluie():

        # Déplacer chaque ligne de la pluie vers le bas


        for ligne in lignes_pluie:

            canvas.move(ligne, 0, vitesse_pluie)

            if ligne:

                if canvas.coords(ligne)[1] >= 800:

                    # Si la ligne atteint le bas du canevas, la déplacer au-dessus du canevas

                    canvas.move(ligne, 0, -1000)  # déplacement vers le haut du canvas


        # Appeler la fonction de déplacement de la pluie à nouveau après un délai de 50 millisecondes

        canvas.after(10, deplacer_pluie)


    deplacer_pluie()



# Fonction pour récupérer les choix de l'utilisateur

def dessin():

    canvas.delete('all')

    t = turtle.RawTurtle(canvas)

    t.hideturtle()

    t.pensize(3)

    t.speed(0)

    t.penup()

    t.hideturtle()

    t.goto(0, -150)

    t.pendown()

    t.hideturtle()


    # Taille de la tige en fonction de la saison

    if saison.get() == "Été":

        t.pensize(20)

        t.pencolor("yellow")

    elif saison.get() == "Printemps":

        t.pensize(10)

        t.pencolor("green")

    elif saison.get() == "Automne":

        t.pensize(10)

        t.pencolor("brown")

    elif saison.get() == "Hiver":

        t.pensize(0)


    # Couleur du cercle en fonction de la condition météo

    if condition.get() == "Soleil":

        t.fillcolor("yellow")

    elif condition.get() == "Un peu de pluie":

        t.fillcolor("cyan")

        pluie()

    elif condition.get() == "Pluie diluvienne":

        t.fillcolor("blue")

        pluie1()


    # Nombre de pétales en fonction des nutriments du sol

    if nutriments.get() == "Sol naturellement pauvre":

        nbr_petales = 4

    elif nutriments.get() == "Sol naturellement riche":

        nbr_petales = 6

    elif nutriments.get() == "Utilisation d’engrais":

        nbr_petales = 12


    # Couleur du cercle en fonction de la condition météo

    if condition.get() == "Soleil":

        t.fillcolor("yellow")

    elif condition.get() == "Un peu de pluie":

        t.fillcolor("cyan")

    elif condition.get() == "Pluie diluvienne":

        t.fillcolor("blue")


    # Dessin de la tige

    t.hideturtle()

    t.penup()

    t.hideturtle()

    t.goto(0, -250)

    t.pendown()


    t.setheading(90)

    t.forward(400)


    # Couleur des pétales en fonction de la luminosité

    if luminosite.get() == "Faible":

        t.fillcolor("white")

    elif luminosite.get() == "Moyenne":

        t.fillcolor("pink")

    elif luminosite.get() == "Forte":

        t.fillcolor("hotpink")


    # Dessin des pétales

    angle = 360 / nbr_petales

    t.hideturtle()

    t.penup()

    t.goto(0, 150)

    t.pendown()

    for i in range(nbr_petales):

        t.begin_fill()

        t.circle(100, 70)

        t.left(180 - 70)

        t.circle(100, 70)

        t.left(180 - 70 + 360 / nbr_petales)

        t.end_fill()


    # Dessin du cercle

    t.penup()

    t.hideturtle()

    t.goto(30, 150)

    t.pendown()

    t.begin_fill()

    t.circle(30)

    t.end_fill()


    t.penup()

    t.hideturtle()

    t.goto(-200, -300)

    t.pendown()

    t.color("green")

    t.begin_fill()

    t.forward(50)

    t.right(90)

    t.forward(4000)

    t.right(90)

    t.forward(50)

    t.right(90)

    t.forward(4000)

    t.end_fill()


    # Cacher la tortue et afficher la fenêtre

    t.hideturtle()



def effacer_fleur():

    canvas.delete('all')



def quitter():

    exit()



# Bouton pour validez les choix de l'utilisateur

bouton_dessin = tk.Button(fenetre, text="Dessiner la fleur", command=dessin)

bouton_effacer = tk.Button(fenetre, text="Effacer la fleur", command=effacer_fleur)

bouton_quiter = tk.Button(fenetre, text="Quitter le jeu", command=quitter)


bouton_dessin.pack(side=tk.LEFT, padx=15, pady=15)


fenetre.mainloop()


#Version 1.3
