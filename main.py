import tkinter
from tkinter import *
# variable initialisation


# Function to create all bricks
def bricksInit():
    i, posX, posY = 0, 0, 0
    while i < 32:

        briksCanva = Canvas(window, width=round((screen_width / 2) / 8), height=(screen_height / 2) / 15, bg='RED')
        briksCanva.pack()
        briksCanva.place(x=posX, y=posY)

        posX = posX + ((screen_width / 2) / 8)

        if i % 8 == 7:
            posY = round(posY + (screen_height / 2) / 15)
            posX = 0
        i = i + 1

def ball():
    ball = Canvas(window, width=20, height=20,bd=0)
    ball.create_oval(150, 150, 350, 350, fill="orange", width=4)
    ball.pack()
    ball.place(x=200, y=200)

window = Tk()
window.configure(bg='#e5e7e6')
window.title('Casse-brique')
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window.geometry(f'{round(screen_width / 2)}x{round(screen_height / 2)}+{round(screen_width / 4)}+{round(screen_height / 4)}')

bricksInit()

zone_dessin = Canvas(window, width=20, height=20, bd=0)
zone_dessin.pack()  # Affiche le Canvas

# Nous allons maintenant utiliser quelques methodes du widget "zone_dessin"
zone_dessin.create_oval(3, 3, 20, 20, fill="orange", width=1)  # Dessine un cercle

window.mainloop()
