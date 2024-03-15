import tkinter as tk
import tkinter.colorchooser as cc
import random

CANVAS_WIDTH, CANVAS_HEIGHT = 600, 400
DEFAULT_COLOR = "blue"
selected_color = DEFAULT_COLOR  # Couleur par défaut


def dessiner_cercle():
    global selected_color
    x = random.randint(50, CANVAS_WIDTH - 50)
    y = random.randint(50, CANVAS_HEIGHT - 50)
    canvas.create_oval(x - 50, y - 50, x + 50, y + 50, fill=selected_color)


def dessiner_carre():
    global selected_color
    x = random.randint(50, CANVAS_WIDTH - 50)
    y = random.randint(50, CANVAS_HEIGHT - 50)
    canvas.create_rectangle(x - 50, y - 50, x + 50, y + 50, fill=selected_color)


def dessiner_croix():
    global selected_color
    x = random.randint(50, CANVAS_WIDTH - 50)
    y = random.randint(50, CANVAS_HEIGHT - 50)
    canvas.create_rectangle(x - 50, y - 50, x + 50, y + 50, outline="black")
    canvas.create_line(x - 50, y, x + 50, y, fill=selected_color)
    canvas.create_line(x, y - 50, x, y + 50, fill=selected_color)


def choisir_couleur():
    global selected_color
    couleur = cc.askcolor(initialcolor=selected_color)[1]
    if couleur:
        selected_color = couleur


root = tk.Tk()
root.title("Mon dessin")

canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="black")
bouton1 = tk.Button(root, text="Choisir une couleur", fg="purple", command=choisir_couleur)
bouton2 = tk.Button(root, text="Cercle", fg="blue", command=dessiner_cercle)
bouton3 = tk.Button(root, text="Carré", fg="red", command=dessiner_carre)
bouton4 = tk.Button(root, text="Croix", fg="yellow", command=dessiner_croix)

canvas.grid(row=1, column=1, rowspan=3)
bouton1.grid(row=0, column=1)
bouton2.grid(row=1, column=0)
bouton3.grid(row=2, column=0)
bouton4.grid(row=3, column=0)

root.mainloop()