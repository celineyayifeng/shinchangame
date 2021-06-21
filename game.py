# Yayi Feng (yf7qq) and Mingze (Terry) Li (ml3sf)

import pygame
import gamebox
import random
show_splash = True
show_instructions = False
invulnerability = 0
ticks = 0

def splash(keys):
    global show_splash
    global show_instructions
    camera.draw(background)
    camera.draw(gamebox.from_text(camera.x,camera.y,"RUN! SHIN-CHAN!","Chalkboard",40,"white"))
    camera.draw(gamebox.from_text(camera.x, camera.y+40, "By: Yayi Feng (yf7qq) & Mingze Li (ml3sf)", "Chalkboard", 15, "white"))
    camera.draw(gamebox.from_text(camera.x,camera.y+60,"Press i for instructions...","Chalkboard",15,"white"))
    camera.draw(gamebox.from_text(camera.x,camera.y+80,"...or press space to play","Chalkboard",15,"white"))

    if pygame.K_SPACE in keys:
        show_splash = False

    if pygame.K_i in keys:
        show_splash = False
        show_instructions = True
    camera.display()


def instructions(keys):
    global show_instructions
    camera.draw(background)
    camera.draw(gamebox.from_text(500, 140,
    "On a nice and sunny day, Shin-Chan goes out and collect his favorite snack, star cookies.",
                                  "Arial",15,"white")),
    camera.draw(gamebox.from_text(500, 160,
    "However, he also needs to run away from the evil villain, which is his temptation to play around",
                                  "Arial", 15,"white")),
    camera.draw(gamebox.from_text(500, 180,
    "and not get any cookie collected. Try to help Shin-Chan collect as many cookies as he can, ",
                                  "Arial", 15, "white")),
    camera.draw(gamebox.from_text(500, 200, "while staying away from the villain. Enjoy!",
    "Arial", 15, "white"))

    camera.draw(gamebox.from_image(345, 270, "shin.png"))
    camera.draw(gamebox.from_text(500, 270, "Control        with arrow keys. Your lives are shown in the upper left.",
    "Arial", 15, "white"))

    camera.draw(gamebox.from_text(500, 300, "If you are hurt, you will have a few seconds of invulnerability.",
    "Arial", 15, "white"))

    camera.draw(gamebox.from_text(500, 400, "Don't let the buttcheeks touch you.",
    "Arial", 50, "white"))

    camera.draw(gamebox.from_image(583, 450, "villain.png"))
    camera.draw(gamebox.from_text(500, 450, "don't touch this >>>",
                                  "Arial", 15, "white"))

    camera.draw(gamebox.from_text(500, 500, "press space to play",
    "Arial", 15, "white"))

    if pygame.K_SPACE in keys:
        show_instructions = False

    camera.display()

def endgame(keys):
    global ticks
    camera.draw(background)
    camera.draw(gamebox.from_text(camera.x,camera.y,"Game over!", "Chalkboard", 15, "white"))
    camera.draw(gamebox.from_text(camera.x,camera.y+20,"You survived for " + str(ticks // 21) + " seconds and collected"+" "+str(player.score)+" "+"star cookie(s)!","Chalkboard",15,'white'))

def endgame_win(keys):
    global ticks
    camera.draw(background)
    camera.draw(gamebox.from_text(camera.x,camera.y,"YOU WIN!", "Chalkboard", 15, "white"))
    camera.draw(gamebox.from_text(camera.x,camera.y+20,"You played for "+str(ticks//21)+" seconds.","Chalkboard",15,'white'))

camera = gamebox.Camera(1000, 600)
walls = [
    gamebox.from_color(75, 150,"yellow", 20, 200),
    gamebox.from_color(75, 450, "yellow", 20, 200),
    gamebox.from_color(925, 150,"yellow", 20, 200),
    gamebox.from_color(925, 450, "yellow", 20, 200),
    gamebox.from_color(150, 300, "yellow", 20, 300),
    gamebox.from_color(850, 300, "yellow", 20, 300),
    gamebox.from_color(240, 150, "yellow", 200, 20),
    gamebox.from_color(240, 450, "yellow", 200, 20),
    gamebox.from_color(760, 150, "yellow", 200, 20),
    gamebox.from_color(760, 450, "yellow", 200, 20),
    gamebox.from_color(220, 300, "yellow", 20, 180),
    gamebox.from_color(780, 300, "yellow", 20, 180),
    gamebox.from_color(300, 300, "yellow", 20, 180),
    gamebox.from_color(700, 300, "yellow", 20, 180),
    gamebox.from_color(325, 300, "yellow", 200, 20),
    gamebox.from_color(675, 300, "yellow", 200, 20),
    gamebox.from_color(310, 75, "yellow", 320, 20),
    gamebox.from_color(690, 75, "yellow", 320, 20),
    gamebox.from_color(420, 210, "yellow", 60, 60),
    gamebox.from_color(580, 210, "yellow", 60, 60),
    gamebox.from_color(420, 130, "yellow", 60, 20),
    gamebox.from_color(580, 130, "yellow", 60, 20),
    gamebox.from_color(460, 470, "yellow", 20, 180),
    gamebox.from_color(540, 470, "yellow", 20, 180),
    gamebox.from_color(500, 380, "yellow", 200, 20),
    gamebox.from_color(280, 550, "yellow", 20, 100),
    gamebox.from_color(720, 550, "yellow", 20, 100),
    gamebox.from_color(220, 550, "yellow", 120, 20),
    gamebox.from_color(780, 550, "yellow", 120, 20),
    gamebox.from_color(370, 530, "yellow", 60, 60),
    gamebox.from_color(630, 530, "yellow", 60, 60),
    gamebox.from_color(500, 240, "yellow", 20, 150),
    gamebox.from_color(200, 70, "yellow", 20, 70),
    gamebox.from_color(800, 70, "yellow", 20, 70),
    gamebox.from_color(275, 70, "yellow", 20, 70),
    gamebox.from_color(725, 70, "yellow", 20, 70),
    gamebox.from_color(350, 70, "yellow", 20, 70),
    gamebox.from_color(650, 70, "yellow", 20, 70)
]
coins = []
for i in range(100):
    coins.append(gamebox.from_image(
        random.randrange(camera.left, camera.right),
        random.randrange(camera.top, camera.bottom),
        "coin.png"
    ))
for wall in walls:
    for coin in coins:
        if wall.touches(coin):
            coins.remove(coin)

background = gamebox.from_image(500, 200, 'background.png')
player = gamebox.from_image(500, 350, "shin.png")
enemy = gamebox.from_image(5, 20, "villain.png")
player.health = 3
player.score = 0
player.lives = [
    gamebox.from_image(20, 20, "shin.png"),
    gamebox.from_image(60, 20, "shin.png"),
    gamebox.from_image(100, 20, "shin.png")
]
music=gamebox.load_sound('music.ogg')
musicplayer=music.play(-1)

def tick(keys):

    global ticks
    global invulnerability

    if show_splash == True:

        splash(keys)
        return

    if show_instructions == True:
        instructions(keys)
        return

    ticks += 1
    invulnerability += 1

    # camera.clear('black')
    camera.draw(background)
    if pygame.K_RIGHT in keys:
        player.x += 10
    if pygame.K_LEFT in keys:
        player.x -= 10
    if pygame.K_UP in keys:
        player.y -= 10
    if pygame.K_DOWN in keys:
        player.y += 10
    for wall in walls:
        if player.bottom_touches(wall):
            player.speedx = 0
        player.move_to_stop_overlapping(wall)
    for wall in walls:
        # camera.draw(background)
        camera.draw(wall)

    if player.bottom > camera.bottom:
        player.bottom = camera.bottom
    if player.top < camera.top:
        player.top = camera.top
    if player.left < camera.left:
        player.left = camera.left
    if player.right > camera.right:
        player.right = camera.right

    for life in player.lives:
        camera.draw(life)
    if enemy.touches(player) and invulnerability > 100:
        player.health -= 1
        player.lives.pop(-1)
        player.x = 500
        player.y = 350
        invulnerability = 0

    camera.draw(player)

    if enemy.x < player.x:
        enemy.x += 4
    if enemy.x > player.x:
        enemy.x -= 4
    if enemy.y < player.y:
        enemy.y += 4
    if enemy.y > player.y:
        enemy.y -= 4
    # enemy.speedx *=0.95
    # enemy.speedy *=0.95
    camera.draw(enemy)

    for coin in coins:
        camera.draw(coin)
        if player.touches(coin):
            player.score += 1
            coins.remove(coin)

    if player.health == 0:
        gamebox.pause()
        endgame(keys)
        musicplayer.pause()
    if coins==[]:
        gamebox.pause()
        endgame_win(keys)
        musicplayer.pause()

    camera.display()



gamebox.timer_loop(30, tick)
