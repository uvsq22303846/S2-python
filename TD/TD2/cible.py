import tkinter as tk
import math

# Définition des couleurs
couleurs = ["blue", "green", "black", "yellow", "magenta", "red"]


# Fonction pour dessiner un cercle
def dessiner_cercle(x, y, rayon, couleur):
    canvas.create_oval(x-rayon, y-rayon, x+rayon, y+rayon, fill=couleur)


# Définition de la taille de l'image
largeur = 500
hauteur = 500

# Création de la fenêtre
fenetre = tk.Tk()
fenetre.geometry(f"{largeur}x{hauteur}")

# Création du canvas
canvas = tk.Canvas(fenetre, width=largeur, height=hauteur)
canvas.pack()

# Nombre de cercles
nb_cercles = 20

# Rayon du cercle central
rayon_central = 20

# Dessin des cercles
for i in range(nb_cercles):
    rayon = rayon_central + (i + 1) * 10 + 10 * math.sin(2 * math.pi * i / nb_cercles)

    angle = 2 * math.pi * i / nb_cercles
    x = largeur / 2 + rayon * math.cos(angle)
    y = hauteur / 2 + rayon * math.sin(angle)

    dessiner_cercle(x, y, rayon, couleurs[i % len(couleurs)])

# Affichage de la fenêtre
fenetre.mainloop()