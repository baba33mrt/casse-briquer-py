import random
from tkinter import *
from math import *


def gameInit(n, m=-1, bricksrandom=False):
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
            if (bricksrandom == True and random.randint(0, 10) != 1) or bricksrandom == False:
                mainCanvas.create_rectangle(posX, posY, posX + (screen_width / n), posY + screen_height / n,
                                            fill=f'#{random.randint(0, 255):02x}{random.randint(0, 255):02x}{random.randint(0, 255):02x}',
                                            outline="#e5e7e6")
            j = j + 1
            posX = posX + (screen_width / n)
        posY = posY + screen_height / n
        print(i)
        i = i + 1


def paddleInit(size=30):
    paddle = mainCanvas.create_rectangle(screen_width / 2 - size, screen_height - 30, screen_width / 2 + size,
                                         screen_height - 15, fill='YELLOW')
    return paddle


def droite(size=30):
    if mainCanvas.coords(paddle)[2] <= screen_width:
        mainCanvas.move(paddle, 15, 0)


def gauche(size=30):
    if mainCanvas.coords(paddle)[0] >= 0:
        mainCanvas.move(paddle, -15, 0)


def collision():
    global dx, dy, score

    coll = mainCanvas.find_overlapping(*mainCanvas.coords(ball))
    if len(coll) >= 2:
        if coll[1] == 2:  #### contact avec la raquette
            pass
        if coll[1] > 2:  #### contact avec brique
            mainCanvas.delete(coll[1])
            score = score + 1
            if score % 10 == 0:
                dx, dy = sqrt(dx*dx) + random.randint(0, 1), sqrt(dy*dy) + random.randint(0, 1)
                print(dx, dy)
            dy = -dy
    if mainCanvas.coords(ball)[0] >= mainCanvas.coords(paddle)[0] and mainCanvas.coords(ball)[2] <= \
            mainCanvas.coords(paddle)[2] and mainCanvas.coords(ball)[3] >= mainCanvas.coords(paddle)[1] and \
            mainCanvas.coords(ball)[1] <= mainCanvas.coords(paddle)[3]:
        dy = -1 * dy
    elif mainCanvas.coords(ball)[0] <= 0:
        dx = -1 * dx
    elif mainCanvas.coords(ball)[1] <= 0:
        dy = -1 * dy
    elif mainCanvas.coords(ball)[3] >= screen_height:
        print('Vous avez perdu')
        dy = -1 * dy
        mainCanvas.delete(ball)
        return True
    elif mainCanvas.coords(ball)[2] >= screen_width:
        dx = -1 * dx


def game():
    global dx, dy
    if collision() != True:
        mainCanvas.bind_all('<Right>', droite)
        mainCanvas.bind_all('<Left>', gauche)
        mainCanvas.move(ball, dx, dy)
        mainCanvas.move(ball, dx, dy)
        mainCanvas.after(20, game)


dx = random.randint(1, 2) * random.choice([-1, 1])
dy = random.randint(1, 2) * -1
score = 0
window = Tk()
window.configure(bg='#e5e7e6')
window.title('Casse-brique')
window.resizable(height=False, width=False)
screen_width, screen_height = window.winfo_screenwidth() / 2, window.winfo_screenheight() / 2
window.geometry(f'{round(screen_width)}x{round(screen_height)}+{round(screen_width / 2)}+{round(screen_height / 2)}')

mainCanvas = Canvas(window, width=screen_width, height=screen_height, bg='#e5e7e6')
mainCanvas.pack()

paddle = paddleInit(300)
ball = mainCanvas.create_oval(screen_width / 2 - 10, screen_height / 2 - 10, screen_width / 2 + 10,
                              screen_height / 2 + 10, fill="orange", width=1)
gameInit(random.randint(12, 20), random.randint(3, 5), True)
game()
print('ok')
window.mainloop()
