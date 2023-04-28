import tkinter as tk
import tkinter.font as font
import turtle
import random
import os

# Créer une fenêtre d'accueil
accueil = tk.Tk()
accueil.geometry("700x700+0+5")
accueil.iconbitmap("lfbp.ico")
accueil.title("Accueil")
accueil.config(bg = "#0dbbe9")

# Fonction pour fermer la fenêtre d'accueil et ouvrir la fenêtre principale
def ouvrir_fenetre_principale():

    accueil.destroy()  # Ferme la fenêtre d'accueil

#taille et style des boutons
taille_btn = font.Font(font = ("Fixedsys" , 8))

#bordure des boutons
bordure_boutons = tk.Frame(accueil, highlightbackground = "white", highlightthickness = 2, bd = 2)

#fonction si boutons appuyer
def continuer():
    accueil.destroy()
    os.popen("python MENU_PRINCIPAL.py")

#creation de la frame et des boutons
btn_frame = tk.Frame(accueil, bordure_boutons , bg = "#0dbbe9")
btn_continuer = tk.Button(btn_frame, text = "continuer ->", bg = "black", fg = "white", height = 1, width = 12, command=continuer)

#taille et style des boutons
taille_btn = font.Font(font = ("Fixedsys" , 8))
btn_continuer['font'] = taille_btn

# Label de bienvenue dans la fenêtre d'accueil
label_bienvenue = tk.Label(accueil, text="Bienvenue dans l'univers de FLORIUS,\n une application étonnante qui simule la croissance d'une fleur unique en son genre !\n Imaginez pouvoir contrôler les différents critères qui influencent la floraison, tels que le climat,\n la météo et la luminosité, pour obtenir une fleur totalement personnalisée.\n Chaque choix que vous ferez aura un impact direct sur la croissance de votre fleur,\n ce qui la rendra véritablement unique en son genre.\n Vous serez mis au défi de trouver les facteurs qui influencent les différentes caractéristiques de votre fleur,\n ce qui rendra l'expérience encore plus intéressante.\n Êtes-vous prêt à relever le défi et à créer votre propre chef-d'œuvre floral ?\n Venez découvrir l'univers de FLORIUS dès maintenant !"
                           ,wraplength=650, font=("System", 17), bg='#0dbbe9', fg='#1d2c88')

#afficher le label ainsi que les boutons
label_bienvenue.pack(fill="both",expand=tk.YES, padx=10, pady=10)
btn_frame.pack(padx = (0,5), pady = (0,5), side="right")
btn_continuer.pack()

#afficher la fenetre
accueil.mainloop()