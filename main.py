import random

from tkinter import *


def gameInit(n, m=-1):
    global bricks
    if m == -1:
        m = n
    i, posX, posY = 0, 0, 0

    while i <= m:
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


def paddleInit(size=30):
    paddle = mainCanvas.create_rectangle(screen_width / 2 - size, screen_height - 30, screen_width / 2 + size,
                                         screen_height - 15, fill='YELLOW')
    return paddle


def droite(size=30):
    mainCanvas.move(paddle, 10, 0)


def gauche(size=30):
    mainCanvas.move(paddle, -10, 0)


def collision():
    global dx, dy
    if mainCanvas.coords(ball)[0] >= mainCanvas.coords(paddle)[0] and mainCanvas.coords(ball)[2] <= \
            mainCanvas.coords(paddle)[2] and mainCanvas.coords(ball)[3] >= mainCanvas.coords(paddle)[1] and \
            mainCanvas.coords(ball)[1] <= mainCanvas.coords(paddle)[3]:
        dy = -1 * dy
    elif mainCanvas.coords(ball)[0] <= 0:
        dx = -1 * dx
    elif mainCanvas.coords(ball)[1] <= 0:
        dy = -1 * dy
    elif mainCanvas.coords(ball)[3] >= screen_height:
        dy = -1 * dy
    elif mainCanvas.coords(ball)[2] >= screen_width:
        dx = -1 * dx


def deplacement():
    global dx, dy
    mainCanvas.bind_all('<Right>', droite)
    mainCanvas.bind_all('<Left>', gauche)
    collision()
    mainCanvas.move(ball, dx, dy)
    mainCanvas.move(ball, dx, dy)
    mainCanvas.after(20, deplacement)
    coll = mainCanvas.find_overlapping(*mainCanvas.coords(ball))
    if len(coll) >= 2:
        if coll[1] > 2:
            print(coll[1])
            mainCanvas.delete(coll[1])
            dy = -1 * dy


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

speed = 1
ball1 = None

paddle = paddleInit()
ball = mainCanvas.create_oval(screen_width / 2 - 10, screen_height / 2 - 10, screen_width / 2 + 10,
                              screen_height / 2 + 10, fill="orange", width=1)
gameInit(15, 3)
deplacement()
print('ok')
window.mainloop()