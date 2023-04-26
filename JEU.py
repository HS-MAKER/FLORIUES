import tkinter as tk
import tkinter.font as font
import turtle
import random
import os

# Créer une fenêtre
fenetre = tk.Tk()
fenetre.title("FLORIUS")
fenetre.geometry("700x700+0+5")
fenetre.config(bg = "#0dbbe9")
fenetre.iconbitmap("lfbp.ico")
fenetre.resizable(width=False,height=False)
canvas_frame = tk.Frame(fenetre, highlightthickness = 0.2, bd = 0.2)
canvas_frame.pack(side=tk.RIGHT, padx=10, pady=(50,0))
canvas = tk.Canvas(canvas_frame, width=350, height=575, bg="#0dbbe9")
canvas.pack()
label1 = tk.Label(fenetre, text="FLORIUS", font=("System", 40), bg='#0dbbe9', fg='black')
label1.pack(expand=tk.YES)
label1.place(relx=0.5, rely=0, anchor=tk.N)


def get_choices():
    print(saison.get(), condition.get(), nutriments.get(), luminosite.get())






# Catégorie 5 : Luminosité
luminosite_frame = tk.LabelFrame(fenetre, text="LUMINOSITÉ",font=("System", 4), bg="#0dbbe9")
luminosite_frame.pack(padx=10, pady=(80,10))

luminosite = tk.StringVar()
luminosite.set(None)


Forte_button = tk.Radiobutton(luminosite_frame, text="Forte",font=("Courier", 10), variable=luminosite, value="Forte", fg="black",
                              bg="#9E7BFF")
Forte_button.pack(pady=5)

Moyenne_button = tk.Radiobutton(luminosite_frame, text="Moyenne",font=("Courier", 10), variable=luminosite, value="Moyenne", fg="black",
                                bg="#9E7BFF")
Moyenne_button.pack(pady=5)

Faible_button = tk.Radiobutton(luminosite_frame, text="Faible",font=("Courier", 10), variable=luminosite, value="Faible", fg="black",
                               bg="#9E7BFF")
Faible_button.pack(pady=5)

# Catégorie 2 : Saison
saison_frame = tk.LabelFrame(fenetre, text="SAISON",font=("System", 4), bg="#0dbbe9")
saison_frame.pack(padx=10, pady=10)

saison = tk.StringVar()
saison.set(None)

ete_button = tk.Radiobutton(saison_frame, text="Été",font=("Courier", 10), variable=saison, value="Été", fg="black", bg="#01F9C6")
ete_button.pack(pady=5)

Automne_button = tk.Radiobutton(saison_frame, text="Automne",font=("Courier", 10), variable=saison, value="Automne", fg="black", bg="#01F9C6")
Automne_button.pack(pady=5)

Printemps_button = tk.Radiobutton(saison_frame, text="Printemps",font=("Courier", 10), variable=saison, value="Printemps", fg="black",
                                  bg="#01F9C6")
Printemps_button.pack(pady=5)

# Catégorie 3 : Condition météo
condition_frame = tk.LabelFrame(fenetre, text="CONDITION MÉTÉO",font=("System", 4), bg="#0dbbe9")
condition_frame.pack(padx=10, pady=10)

condition = tk.StringVar()
condition.set(None)

soleil_button = tk.Radiobutton(condition_frame, text="Soleil",font=("Courier", 10), variable=condition, value="Soleil", fg="black",
                               bg="#FFC0CB")
soleil_button.pack(pady=5)

Unpeudepluie_button = tk.Radiobutton(condition_frame, text="Un peu de pluie",font=("Courier", 10), variable=condition, value="Un peu de pluie",
                                     fg="black", bg="#FFC0CB")
Unpeudepluie_button.pack(pady=5)

pluiediluvienne_button = tk.Radiobutton(condition_frame, text="Pluie diluvienne",font=("Courier", 10), variable=condition,
                                        value="Pluie diluvienne", fg="black", bg="#FFC0CB")
pluiediluvienne_button.pack(pady=5)

# Catégorie 4 : Nutriments du sol
nutriments_frame = tk.LabelFrame(fenetre, text="NUTRIMENTS DU SOL",font=("System", 4), bg="#0dbbe9")
nutriments_frame.pack(padx=10, pady=10)

nutriments = tk.StringVar()
nutriments.set(None)

utilisationdengrais_button = tk.Radiobutton(nutriments_frame, text="Utilisation d’engrais",font=("Courier", 10), variable=nutriments,
                                            value="Utilisation d’engrais", fg="black", bg="#F7FF3C")
utilisationdengrais_button.pack(pady=5)


solnaturellementriche_button = tk.Radiobutton(nutriments_frame, text="Sol naturellement riche",font=("Courier", 10), variable=nutriments,
                                              value="Sol naturellement riche", fg="black", bg="#F7FF3C")
solnaturellementriche_button.pack(pady=5)

solnaturellementpauvre_button = tk.Radiobutton(nutriments_frame, text="Sol naturellement pauvre",font=("Courier", 10), variable=nutriments,
                                               value="Sol naturellement pauvre", fg="black", bg="#F7FF3C")
solnaturellementpauvre_button.pack(pady=5)



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
                if canvas.coords(ligne)[1] >= 600:
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
                if canvas.coords(ligne)[1] >= 600:
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

def menu():
    fenetre.destroy()
    os.popen("python menu_principal.py")
    
def quitter():
    exit()



# Boutons pour validez les choix de l'utilisateur
bouton_menu = tk.Button(fenetre, text="<- Menu",command=menu)
bouton_dessin = tk.Button(fenetre, text="Dessiner",command=dessin)
bouton_quiter = tk.Button(fenetre, text="Quitter", command=quitter)

#taille et style des boutons
taille_btn = font.Font(font = ("Fixedsys" , 8))
bouton_menu['font'] = taille_btn
bouton_dessin['font'] = taille_btn
bouton_quiter['font'] = taille_btn

bouton_menu.pack(side=tk.LEFT, padx=(7,0), pady=(0,0))
bouton_dessin.pack(side=tk.LEFT,padx=(50,50), pady=(0,0))
bouton_quiter.pack(side=tk.LEFT,padx=(0,0), pady=(0,0))

fenetre.mainloop()
