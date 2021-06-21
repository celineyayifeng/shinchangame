import pygame
import gamebox
camera = gamebox.Camera(800,600)

# box = gamebox.from_color(200, 100, 'red', 40, 80)

box = gamebox.from_text(50, 100, "box", "Arial", 40, "red")

walls = [
    gamebox.from_color(camera.x,camera.bottom,"black",500,50),
    gamebox.from_color(400,200,"black",50,500),
    gamebox.from_color(80,120,"black",30,30)
]

goal=gamebox.from_text(100,400,"goal","Arial",20,"blue")

def tick(keys):


    camera.clear('cyan')

    if pygame.K_RIGHT in keys:
        box.x += 10
    if pygame.K_LEFT in keys:
        box.x -= 10
    if pygame.K_UP in keys:
        box.y -= 10
    if pygame.K_DOWN in keys:
        box.y += 10
    for wall in walls:
        box.move_to_stop_overlapping(wall,-30,-30)


    # if pygame.K_SPACE in keys:
    #     box.color = 'white'
    # else:
    #     box.color = 'red'

    camera.draw(box)
    for wall in walls:
        camera.draw(wall)

    camera.draw(goal)

    if box.touches(goal,-60,60):
        won=gamebox.from_text(camera.x,camera.y,"You won", "Arial", 150,"White")
        camera.draw(won)
        for wall in walls:
            wall.color='purple'

        gamebox.pause()


    # usually camera.display() should be the last line of the tick method
    camera.display()

ticks_per_second = 30

# keep this line the last one in your program
gamebox.timer_loop(ticks_per_second, tick)