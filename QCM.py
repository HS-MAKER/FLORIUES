import random
import tkinter as tk
import tkinter.font as font
import tkinter.messagebox
import os

# Les 10 questions et réponses
questions = {
"Quel est le plus grand type de fleur ?": {
"a": "Rose",
"b": "Tulipe",
"c": "Tournesol",
"réponse": "c",
"explication": "Le tournesol de son nom latin Helianthus annuus, est une plante annuelle (il existe aussi des Hélianthus vivaces) dont la particularité réside dans sa grande taille, jusqu'à 4 mètres de hauteur, ."
},
"De quelles couleurs sont les coquelicots ?": {
"a": "Blanc et rouge",
"b": "Jaune et bleu",
"c": "Rouge et noir",
"réponse": "c",
"explication": " Les coquelicots sont des plantes à fleurs annuelles appartenant à la famille des Papaveraceae. Les fleurs de coquelicot sont composées de quatre pétales rouges vifs, qui peuvent parfois être orangés. Les pétales ont souvent une texture légèrement froissée et peuvent mesurer jusqu'à 10 centimètres de diamètre.."
},
"Quel est le nom de la fleur de lotus en Inde ?": {
"a": "Padma",
"b": "Sakura",
"c": "Orchidée",
"réponse": "a",
"explication": " En Inde, la fleur de lotus est communément appelée ""Padma"" ou ""Kamal"" en hindi, qui sont les noms locaux pour le lotus. Le lotus est souvent représenté dans l'art et l'architecture indiens, notamment dans les temples, les monuments historiques et les peintures. Il est également considéré comme un symbole de pureté, de beauté, de paix et de prospérité."
},
"Quel est le nom de la fleur nationale du Japon ?": {
"a": "Rose",
"b": "Sakura",
"c": "Tulipe",
"réponse": "b",
"explication": "La fleur nationale du Japon est la fleur de cerisier, également connue sous le nom de sakura en japonais. La floraison des cerisiers est un événement très important au Japon et attire chaque année de nombreux touristes du monde entier. La beauté éphémère des fleurs de cerisier est souvent associée à la fragilité et à la transitoire nature de la vie, ce qui est un thème important dans la culture japonaise. Les fleurs de cerisier sont également utilisées dans de nombreux événements et célébrations japonaises, y compris le festival traditionnel Hanami, où les gens se réunissent pour pique-niquer sous les cerisiers en fleurs."
},
"Quelle fleur symbolise la beauté éphémère en Chine ?": {
"a": "Orchidée",
"b": "Lotus",
"c": "Pivoine",
"réponse": "c",
"explication": "La pivoine est En Chine, la fleur qui symbolise la beauté éphémère est la pivoine. La pivoine est une fleur très appréciée en Chine pour sa beauté et sa couleur vive. Elle est souvent considérée comme la ""reine des fleurs"" en raison de sa grande taille et de sa beauté majestueuse. Traditionnellement, la pivoine est associée à la saison du printemps et à la beauté éphémère de la vie, car elle fleurit seulement pendant une courte période chaque année. Dans la culture chinoise, la pivoine est également considérée comme un symbole de richesse, de réussite et de bonne fortune. La fleur est souvent utilisée dans l'art et l'artisanat chinois, ainsi que dans la médecine traditionnelle chinoise pour ses propriétés médicinales.."
},
"Quel est le nom de la fleur nationale de l'Inde ?": {
"a": "Rose",
"b": "Jasmin",
"c": "Lys",
"réponse": "b",
"explication": " la fleur de jasmin (Jasminum sambac), qui est très parfumée et est souvent utilisée dans les offrandes religieuses et les décorations de mariage, et la fleur de palash (Butea monosperma), qui est également connue sous le nom de ""flamboyant des Indes"" et est considérée comme un symbole de l'arrivée du printemps.."
},
"Quelle fleur est souvent associée à l'amour et à la passion ?": {
"a": "Tulipe",
"b": "Rose",
"c": "Marguerite",
"réponse": "b",
"explication": "La fleur qui est souvent associée à l'amour et à la passion est la rose . Depuis des siècles, la rose  a été utilisée comme symbole de l'amour et de la romance, et elle est souvent offerte comme cadeau pour exprimer des sentiments d'amour et de passion. La couleur rouge vif de la rose est associée au cœur et au sang, ce qui renforce l'association avec les émotions fortes et passionnées. Les roses  sont souvent utilisées dans les arrangements floraux pour les occasions romantiques telles que les anniversaires, les mariages et la Saint-Valentin. Cependant, d'autres fleurs peuvent également être associées à l'amour et à la passion, telles que les tulipes rouges et les orchidées"
},
"De quelle famille fait partie la fleur de tournesol ?": {
"a": "Astéracées",
"b": "Liliacées",
"c": "Rosacées",
"réponse": "a",
"explication": "La fleur de tournesol appartient à la famille des Asteraceae, également connue sous le nom de famille des Composées. Cette famille est l'une des plus grandes familles de plantes à fleurs, comprenant environ 32 000 espèces différentes réparties dans plus de 1 900 genres différents. Les Asteraceae sont caractérisées par des fleurs en forme de capitule, qui sont constituées de nombreux petits fleurons disposés en cercle autour d'un centre. Les tournesols ont des fleurs de capitule très grandes et plates, avec des pétales jaunes autour d'un disque central de fleurons sombres. Les tournesols sont originaires d'Amérique du Nord et sont cultivés dans le monde entier pour leur huile, leurs graines comestibles et leur utilisation décorative en tant que fleurs coupées.."
},
"Quel est le nom de la fleur nationale du Mexique ?": {
"a": "Clematites ",
"b": " Amaryllis",
"c": "Dahlia ",
"réponse": "c",
"explication": "La fleur nationale du Mexique est la dahlia (Dahlia pinnata). Les dahlias sont des plantes herbacées originaires du Mexique et de l'Amérique centrale, qui produisent des fleurs spectaculaires dans une large gamme de couleurs et de formes. Les fleurs de dahlia sont souvent associées à la fierté et à la beauté mexicaines, et elles sont très appréciées pour leur utilisation décorative dans les arrangements floraux et les jardins. Les dahlias sont également cultivées pour leur utilisation médicinale, car elles contiennent des composés bioactifs qui ont des propriétés anti-inflammatoires et analgésiques. La dahlia a été déclarée fleur nationale du Mexique en 1963."
},
}
# Sélectionner 5 questions au hasard
selected_questions = random.sample(list(questions.keys()), 5)

# Fonction pour afficher les réponses
def check_answer(question, user_answer):
    correct_answer = questions[question]["réponse"]
    explication = questions[question]["explication"]
    if user_answer == correct_answer:
         return( "Correct !. C'était {}".format(explication))
    else:
        return ( "Incorrect .C'était {}".format(explication))

# Interface utilisateur
class QCM(tk.Tk):
    def __init__(self, questions):
        super().__init__()
        self.questions = questions
        self.score = 0
        self.question_number = 0
        self.title("QCM sur les fleurs")
        self.geometry("700x500+0+5")
        self.config(bg = "#0dbbe9")
        self.iconbitmap("lfbp.ico")
        self.create_widgets()

    def create_widgets(self):
        self.question_label = tk.Label(self, text="",font=("Terminal", 20),bg="#0dbbe9", highlightbackground="white", highlightthickness=2, padx=10, pady=10)
        self.question_label.pack(pady=30)
        self.var = tk.StringVar()
        cadre_choix = tk.Frame(self, highlightbackground="white", highlightthickness=1, bg="#0dbbe9")
        cadre_choix.pack(pady=15)
        self.radio_button1 = tk.Radiobutton(cadre_choix, text="", variable=self.var, value="a",font=("Fixedsys", 8),bg="#0dbbe9")
        self.radio_button1.pack(pady=10, padx=10)
        self.radio_button2 = tk.Radiobutton(cadre_choix, text="", variable=self.var, value="b",font=("Fixedsys", 8),bg="#0dbbe9")
        self.radio_button2.pack(pady=10, padx=10)
        self.radio_button3 = tk.Radiobutton(cadre_choix, text="", variable=self.var, value="c",font=("Fixedsys", 8), bg="#0dbbe9")
        self.radio_button3.pack(pady=10, padx=10)
        self.submit_button = tk.Button(self, text="Valider",font=("Fixedsys", 8), command=self.submit_answer)
        self.submit_button.pack(pady=(30,0))

    def load_question(self):
        question = self.questions[self.question_number]
        self.question_label.config(text=question)
        self.radio_button1.config(text=questions[question]["a"])
        self.radio_button2.config(text=questions[question]["b"])
        self.radio_button3.config(text=questions[question]["c"])
        self.var.set(None)

    def submit_answer(self):
        user_answer = self.var.get()
        result = check_answer(self.questions[self.question_number], user_answer)
        if not user_answer:
            tkinter.messagebox.showerror('Error', 'Please select an answer')
        elif result.startswith('Correct'):
            self.score += 1
            tkinter.messagebox.showinfo('Correct', result)
        else:
            tkinter.messagebox.showinfo('Incorrect', result)
        self.question_number += 1
        if self.question_number < len(self.questions):
            self.load_question()
        else:
            tkinter.messagebox.showinfo('Score', ' Votre score est de {} sur  {}'.format(self.score, len(self.questions)))
            self.destroy()
            os.popen("python menu_principal.py")


# Créer l'interface utilisateur avec les questions sélectionnées
qcm = QCM(selected_questions)

def menu():
    qcm.destroy()
    os.popen("python menu_principal.py")
    
def quitter():
    exit()

bouton_menu = tk.Button(qcm, text="<- Menu", command=menu)
bouton_quiter = tk.Button(qcm, text="Quitter", command=quitter)

taille_btn = font.Font(font = ("Fixedsys" , 8))
bouton_menu['font'] = taille_btn
bouton_quiter['font'] = taille_btn

bouton_menu.pack(side=tk.LEFT, padx=(5,0), pady=(130,0))
bouton_quiter.pack(side=tk.RIGHT,padx=(0,5), pady=(130,0))

qcm.load_question()
qcm.mainloop()
