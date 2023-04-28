import tkinter as tk
import tkinter.font as font
import os



#création de la fenetre du menu principal
menu = tk.Tk()
menu.title("Menu principal")
menu.iconbitmap("lfbp.ico")
menu.config(bg ="#0dbbe9")
menu.geometry("700x700+0+5")

#titre et affichage
titre = tk.Label(menu, text = "FLORIUS", font = ("System", 60, "bold"), bg = "#0dbbe9", fg = "black", pady = 25)
titre.pack()

#definir la taille des boutons
taille_btn = font.Font(font = ("Fixedsys" , 24))
taille_btn_revenir = font.Font(font = ("Fixedsys" , 8))

#bordures des boutons
bordure_boutons = tk.Frame(menu, highlightbackground = "white", highlightthickness = 3, bd = 2)
bordure_boutons_retour = tk.Frame(menu, highlightbackground = "white", highlightthickness = 2, bd = 2)
btn_frame = tk.Frame(menu, bordure_boutons , bg = "#0dbbe9")
btn_frame2 = tk.Frame(menu, bordure_boutons , bg = "#0dbbe9")
btn_frame3 = tk.Frame(menu, bordure_boutons , bg = "#0dbbe9")
btn_frame4 = tk.Frame(menu, bordure_boutons_retour , bg = "#0dbbe9")

def jeu():
    menu.destroy()
    os.popen("python jeu.py")

def qcm():
    menu.destroy()
    os.popen("Python qcm.py")

def quitter():
    exit()

def retour():
    menu.destroy()
    os.popen("Python accueil.py")

#creations de boutons
btn_jouer = tk.Button(btn_frame, text = "JOUER", bg = "black", fg = "white", height = 1, width = 10, command = jeu)
btn_qcm = tk.Button(btn_frame2, text = "QCM", bg = "black", fg = "white", height = 1, width = 10, command = qcm)
btn_quitter = tk.Button(btn_frame3, text = "QUITTER", bg = "black", fg = "white", height = 1, width = 10, command = quitter)
btn_retour = tk.Button(btn_frame4, text = "<- retour", bg = "black", fg = "white", height = 1, width = 12, command = retour)


#taille boutons
btn_jouer['font'] = taille_btn
btn_qcm['font'] = taille_btn
btn_quitter['font'] = taille_btn
btn_retour['font'] = taille_btn_revenir

#affichage des frames des boutons 
btn_frame.pack(pady = (40, 75))
btn_frame2.pack(pady = (0, 75))
btn_frame3.pack()
btn_frame4.pack(side="left", pady = (127,0), padx = (6,0))

#affichage des boutons
btn_jouer.pack()
btn_qcm.pack(pady = 0)
btn_quitter.pack()
btn_retour.pack()

#affichage fenetre
menu.mainloop()