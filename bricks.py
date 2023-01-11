import random

from tkinter import *


# Function to create all bricks
def gameInit(n, m=-1):
    global bricks
    if m == -1:
        m = n
    i, posX, posY = 0, 0, 0

    while i < m:
        posX = 0
        j = 0
        if i % 2 == 0:
            posX = posX - screen_width / 2 / n
            j = -1

        while j <= n:
            color = 'red'
            if j % 2 == 0:
                color = 'blue'

            mainCanvas.create_rectangle(posX, posY, posX + (screen_width / n), posY + screen_height / n, fill=color,
                                        outline="#e5e7e6")
            j = j + 1
            posX = posX + (screen_width / n)
        posY = i * screen_height / n
        print(i)
        i = i + 1

dx = random.randint(2, 4)
dy = random.randint(2, 6)
bricks = []

window = Tk()
window.configure(bg='#e5e7e6')
window.title('Casse-brique')
window.resizable(height=False, width=False)
screen_width = window.winfo_screenwidth() / 2
screen_height = window.winfo_screenheight() / 2
window.geometry(f'{round(screen_width)}x{round(screen_height)}+{round(screen_width / 2)}+{round(screen_height / 2)}')

mainCanvas = Canvas(window, width=screen_width, height=screen_height, bg='white')
mainCanvas.pack()

# variables
gameInit(1, 1)
print('ok')
window.mainloop()
