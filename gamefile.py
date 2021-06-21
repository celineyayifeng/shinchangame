import pygame
import gamebox

camera = gamebox.Camera(800,600)

# box = gamebox.from_color(200, 100, 'red', 40, 80)
# box = gamebox.from_image(10, 30, "https://upload.wikimedia.org/wikipedia/en/0/0f/Pygame_logo.png")

box = gamebox.from_text(50, 100, "box", "Arial", 40, "red")
walls = [
    gamebox.from_color(camera.x, camera.bottom, 'purple', 400, 50),
    gamebox.from_color(0, 400, 'purple', 40, 150),
    gamebox.from_color(100, 200, 'purple', 20, 250),
]

box.wait_before_flap = 0

def tick(keys):
    camera.clear('cyan')

    # thrust
    if pygame.K_RIGHT in keys:
        box.speedx = 10
    if pygame.K_LEFT in keys:
        box.speedx = -10
    if pygame.K_UP in keys and box.wait_before_flap <= 0:
        box.speedy = -15
        box.wait_before_flap = 15
    if pygame.K_DOWN in keys:
        box.speedy = 10

    box.wait_before_flap -= 1

    # drag
    box.speedx *= 0.95
    box.speedy *= 0.95

    # gravity
    box.speedy += 1

    box.move_speed()

    # if box.touches(wall):
    #     wall.color = 'black'
    # else:
    #     wall.color = 'purple'

    for wall in walls:
        if box.bottom_touches(wall):
            box.speedx = 0
        box.move_to_stop_overlapping(wall)




    for wall in walls:
        camera.draw(wall)
