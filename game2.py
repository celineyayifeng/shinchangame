# Yayi Feng (yf7qq) and Terry Li (ml3sf)

import pygame
import gamebox
import random
show_splash=True
ticks=0
# need splash page
def splash(keys):
    global show_splash
    camera.clear('black')
    camera.draw(gamebox.from_text(camera.x,camera.y,"Welcome!","Arial",30,"white"))
    camera.draw(gamebox.from_text(camera.x,camera.y+50,"(press space to continue)","Arial",15,"white"))

    if pygame.K_SPACE in keys:
        show_splash=False
    camera.display()




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
for i in range(50):
    coins.append(gamebox.from_color(
        random.randrange(camera.left, camera.right),
        random.randrange(camera.top, camera.bottom),
        "white", 10, 10
    ))

# code for removing coins on wall
for wall in walls:
    for coin in coins:
        if wall.touches(coin):
            coins.remove(coin)
player=gamebox.from_image(20,20,'panda.png')
#player=gamebox.from_image(100, 100, "http://123emoji.com/wp-content/uploads/2016/04/Crayon-Shin-chan-stickers-640511.png")
enemy=gamebox.from_color(30,300,'blue',20,20) # need automatic movement for enemy

# walls = []
# for i in range(250):
#     walls.append(gamebox.from_color(
#         random.randrange(camera.left, camera.right),
#         random.randrange(camera.top, camera.bottom),
#         "yellow", 20, 20))
#
# for wall in walls:
#     camera.draw(wall)
# vert_walls = []
# for i in range(10):
#     vert_walls.append(gamebox.from_color(
#         random.randrange(camera.left, camera.right),
#         random.randrange(camera.top, camera.bottom),
#         "yellow", random.randrange(5, 25), random.randrange(50, 400)
#     ))
#
#
# horiz_walls = []
# for j in range(10):
#     horiz_walls.append(gamebox.from_color(
#         random.randrange(camera.left, camera.right),
#         random.randrange(camera.top, camera.bottom),
#         "yellow", random.randrange(50, 400), random.randrange(5, 25)
#     ))
#
# for vert_wall in vert_walls:
#     for horiz_wall in horiz_walls:
#         while vert_wall.touches(horiz_wall):
#             vert_walls = []
#             for i in range(10):
#                 vert_walls.append(gamebox.from_color(
#                     random.randrange(camera.left, camera.right),
#                     random.randrange(camera.top, camera.bottom),
#                     "yellow", random.randrange(5, 25), random.randrange(50, 400)
#                 ))
#
#             horiz_walls = []
#             for j in range(10):
#                 horiz_walls.append(gamebox.from_color(
#                     random.randrange(camera.left, camera.right),
#                     random.randrange(camera.top, camera.bottom),
#                     "yellow", random.randrange(50, 400), random.randrange(5, 25)
#                 ))


# for vert_wall in vert_walls:
#     for horiz_wall in horiz_walls:
#         a = random.randint(0, 2)
#         if vert_wall.touches(horiz_wall, 20, 20) and a == 0:
#             horiz_walls.remove(horiz_wall)
#         elif vert_wall.touches(horiz_wall, 20, 20) and a == 1:
#             vert_walls.remove(vert_wall)

# for wall in vert_walls:
#     camera.draw(wall)
#
# for wall in horiz_walls:
#     camera.draw(wall)

# Features to include:
# player collects coins show up at random locations
# player being chased by an enemy
# if player touches wall, game over

def tick(keys):
    global ticks
    ticks += 1

    if show_splash:
        splash(keys)
        return

    camera.clear('black')
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
        camera.draw(wall)

    camera.draw(player)

    if enemy.x<player.x:
        enemy.x += 3
    if enemy.x>player.x:
        enemy.x -= 3
    if enemy.y<player.y:
        enemy.y += 3
    if enemy.y>player.y:
        enemy.y -= 3
    enemy.speedx *=0.95
    enemy.speedy *=0.95

    camera.draw(enemy)



    for coin in coins:
        camera.draw(coin)
        if player.touches(coin):
            coins.remove(coin)


    camera.display()

ticks_per_second = 30

gamebox.timer_loop(ticks_per_second, tick)
