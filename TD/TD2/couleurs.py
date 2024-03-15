import tkinter as tk
import random


def get_color(r, g, b):
    """ Retourne une couleur à partir de ses composantes r, g, b entre 0 et 255"""
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)


def draw_pixel(i, j, color):
    canvas.create_rectangle(i, j, i+1, j+1, fill=color, outline="")


def ecran_aleatoire():
    for i in range(256):
        for j in range(256):
            color = get_color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            draw_pixel(i, j, color) 


def degrade_gris():
    for i in range(256):
        gris = i
        couleur = get_color(gris, gris, gris)
        for j in range(256):
            draw_pixel(i, j, couleur)


def degrade_2D():
    for i in range(256):
        for j in range(256):
            couleur = get_color(i, 0, j)
            draw_pixel(i, j, couleur)


root = tk.Tk()

canvas = tk.Canvas(root, width=256, height=256, bg="black")
bouton1 = tk.Button(root, text="Aléatoire", fg="blue", command=ecran_aleatoire)
bouton2 = tk.Button(root, text="Dégradé gris", fg="blue", command=degrade_gris)
bouton3 = tk.Button(root, text="Dégradé 2D", fg="blue", command=degrade_2D)

canvas.grid(column=1, row=0, rowspan=3)
bouton1.grid(column=0, row=0)
bouton2.grid(column=0, row=1)
bouton3.grid(column=0, row=2)

root.mainloop()
