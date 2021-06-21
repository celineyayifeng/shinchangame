import pygame
import gamebox
import random
camera = gamebox.Camera(800,600)

box = gamebox.from_text(50, 100, "box", "Arial", 40, "red")
walls = [
    gamebox.from_color(camera.x, camera.bottom, 'purple', 400, 50),
    gamebox.from_color(0, 400, 'purple', 40, 150),
    gamebox.from_color(100, 200, 'purple', 20, 250),
]
collectables = []
for i in range(50):
    collectables.append(
        gamebox.from_color(
            random.randrange(0, 800),
            random.randrange(0, 600),
            'yellow',
            10, 10
        )
    )

goal = gamebox.from_text(700, 400, "Goal!", "Arial", 30, "black")
win_text = gamebox.from_text(camera.x, camera.y, "You won!", "Arial", 100, "darkgreen")

coins_got = 0
def tick(keys):
    global coins_got
    camera.clear('cyan')

    if pygame.K_RIGHT in keys:
        box.x += 10
        box.speedx = +10
    if pygame.K_LEFT in keys:
        box.x -= 10
    if pygame.K_UP in keys:
        box.y -= 10
    if pygame.K_DOWN in keys:
        box.y += 10

    # if box.touches(wall):
    #     wall.color = 'black'
    # else:
    #     wall.color = 'purple'

    for wall in walls:
        box.move_to_stop_overlapping(wall)

    for coin in collectables:
        if coin.touches(box):
            collectables.remove(coin)
            coins_got += 1

    for wall in walls:
        camera.draw(wall)
    for coin in collectables:
        camera.draw(coin)

    if box.touches(goal):
        win_text = gamebox.from_text(camera.x, camera.y, "You won with "+str(coins_got)+"!", "Arial", 100, "darkgreen")
        camera.draw(win_text)
        gamebox.pause()  # stop running the game loop

    camera.draw(box)
    camera.draw(goal)

    # usually camera.display() should be the last line of the tick method
    camera.display()

ticks_per_second = 30

# keep this line the last one in your program
gamebox.timer_loop(ticks_per_second, tick)