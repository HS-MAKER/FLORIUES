import tkinter as tk
import turtle

# Créer une fenêtre
fenetre = tk.Tk()
fenetre.title("FLORIUS")
fenetre.resizable(width=False,height=False)
canvas_frame = tk.Frame(fenetre)
canvas_frame.pack(side=tk.RIGHT, padx=10, pady=10)
canvas = tk.Canvas(canvas_frame, width=400, height=600)
canvas.pack()
label1 = tk.Label(fenetre, text="Générations de fleurs", font=("Arial", 30), bg='lightblue', fg='darkblue')
label1.pack(expand=tk.YES)


def get_choices():
    print(climat.get(), saison.get(), condition.get(), nutriments.get(), luminosite.get())


# Catégorie 1 : climat
climat_frame = tk.LabelFrame(fenetre, text="climat")
climat_frame.pack(padx=10, pady=10)

climat = tk.StringVar()
climat.set(None)
# Les fonctions tk.Radiobutton permettent de choisir une seul option
Tropical_button = tk.Radiobutton(climat_frame, text="Tropical", variable=climat, value="Tropical", fg="black",
                                 bg="yellow")
Tropical_button.pack(pady=5)

Méditerranée_button = tk.Radiobutton(climat_frame, text="Méditerranée", variable=climat, value="Méditerranée",
                                     fg="black", bg="yellow")
Méditerranée_button.pack(pady=5)

continental_button = tk.Radiobutton(climat_frame, text="Continental", variable=climat, value="Continental", fg="black",
                                    bg="yellow")
continental_button.pack(pady=5)

# Catégorie 2 : Saison
saison_frame = tk.LabelFrame(fenetre, text="Saison")
saison_frame.pack(padx=10, pady=10)

saison = tk.StringVar()
saison.set(None)

ete_button = tk.Radiobutton(saison_frame, text="Été", variable=saison, value="Été", fg="black", bg="yellow")
ete_button.pack(pady=5)

Printemps_button = tk.Radiobutton(saison_frame, text="Printemps", variable=saison, value="Printemps", fg="black",
                                  bg="yellow")
Printemps_button.pack(pady=5)

Automne_button = tk.Radiobutton(saison_frame, text="Automne", variable=saison, value="Automne", fg="black", bg="yellow")
Automne_button.pack(pady=5)

# Catégorie 3 : Condition météo
condition_frame = tk.LabelFrame(fenetre, text="Condition météo")
condition_frame.pack(padx=10, pady=10)

condition = tk.StringVar()
condition.set(None)

soleil_button = tk.Radiobutton(condition_frame, text="Soleil", variable=condition, value="Soleil", fg="black",
                               bg="yellow")
soleil_button.pack(pady=5)

Unpeudepluie_button = tk.Radiobutton(condition_frame, text="Un peu de pluie", variable=condition, value="Un peu de pluie",
                                     fg="black", bg="yellow")
Unpeudepluie_button.pack(pady=5)

pluiediluvienne_button = tk.Radiobutton(condition_frame, text="Pluie diluvienne", variable=condition,
                                        value="Pluie diluvienne", fg="black", bg="yellow")
pluiediluvienne_button.pack(pady=5)

# Catégorie 4 : Nutriments du sol
nutriments_frame = tk.LabelFrame(fenetre, text="Nutriments du sol")
nutriments_frame.pack(padx=10, pady=10)

nutriments = tk.StringVar()
nutriments.set(None)

solnaturellementpauvre_button = tk.Radiobutton(nutriments_frame, text="Sol naturellement pauvre", variable=nutriments,
                                               value="Sol naturellement pauvre", fg="black", bg="yellow")
solnaturellementpauvre_button.pack(pady=5)

solnaturellementriche_button = tk.Radiobutton(nutriments_frame, text="Sol naturellement riche", variable=nutriments,
                                              value="Sol naturellement riche", fg="black", bg="yellow")
solnaturellementriche_button.pack(pady=5)

utilisationdengrais_button = tk.Radiobutton(nutriments_frame, text="Utilisation d’engrais", variable=nutriments,
                                            value="Utilisation d’engrais", fg="black", bg="yellow")
utilisationdengrais_button.pack(pady=5)

# Catégorie 5 : Luminosité
luminosite_frame = tk.LabelFrame(fenetre, text="Luminosité")
luminosite_frame.pack(padx=10, pady=10)

luminosite = tk.StringVar()
luminosite.set(None)

Faible_button = tk.Radiobutton(luminosite_frame, text="Faible", variable=luminosite, value="Faible", fg="black",
                               bg="yellow")
Faible_button.pack(pady=5)

Moyenne_button = tk.Radiobutton(luminosite_frame, text="Moyenne", variable=luminosite, value="Moyenne", fg="black",
                                bg="yellow")
Moyenne_button.pack(pady=5)

Forte_button = tk.Radiobutton(luminosite_frame, text="Forte", variable=luminosite, value="Forte", fg="black",
                              bg="yellow")
Forte_button.pack(pady=5)


# Fonction pour récupérer les choix de l'utilisateur
def dessin():
    canvas.delete('all')
    t = turtle.RawTurtle(canvas)
    t.pensize(3)
    t.speed(0)
    t.penup()
    t.goto(0, -150)
    t.pendown()

    # Couleur des pétales en fonction du climat
    if climat.get() == "Tropical":
        t.pencolor("red")
    elif climat.get() == "Méditerranée":
        t.pencolor("brown")
    elif climat.get() == "Continental":
        t.pencolor("yellow")

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

    # Dessin de la tige
    t.penup()
    t.goto(0, -250)
    t.pendown()
    t.pensize(5)
    t.setheading(90)
    t.forward(400)

    # Couleur du cercle en fonction de la condition météo
    if condition.get() == "Soleil":
        t.fillcolor("yellow")
    elif condition.get() == "Un peu de pluie":
        t.fillcolor("cyan")
    elif condition.get() == "Pluie diluvienne":
        t.fillcolor("blue")

   

    # Nombre de pétales en fonction des nutriments du sol
    if nutriments.get() == "Sol naturellement pauvre":
        nbr_petales = 4
    elif nutriments.get() == "Sol naturellement riche":
        nbr_petales = 6
    elif nutriments.get() == "Utilisation d’engrais":
        nbr_petales = 12

    # Couleur des pétales en fonction de la luminosité
    if luminosite.get() == "Faible":
        t.fillcolor("lightpink")
    elif luminosite.get() == "Moyenne":
        t.fillcolor("pink")
    elif luminosite.get() == "Forte":
        t.fillcolor("hotpink")

    # Dessin des pétales
    angle = 360 / nbr_petales
    t.penup()
    t.goto(0, 150)
    t.pendown()
    for i in range(nbr_petales):
        t.circle(100, 70)
        t.left(180 - 70)
        t.circle(100, 70)
        t.left(180 - 70 + 360 / nbr_petales)

    # Couleur du cercle en fonction de la condition météo
    if condition.get() == "Soleil":
        t.fillcolor("yellow")
    elif condition.get() == "Un peu de pluie":
        t.fillcolor("cyan")
    elif condition.get() == "Pluie diluvienne":
        t.fillcolor("blue")

    # Dessin du cercle
    t.penup()
    t.goto(30, 150)
    t.pendown()
    t.begin_fill()
    t.circle(30)
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

bouton_dessin.pack(side=tk.LEFT,padx=15, pady=15)
bouton_effacer.pack(side=tk.LEFT,padx=20, pady=15)
bouton_quiter.pack(side=tk.LEFT,padx=20, pady=15)
fenetre.mainloop()
