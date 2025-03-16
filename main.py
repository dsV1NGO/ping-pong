from pygame import *

window = display.set_mode((700,700))
display.set_caption('pingPong')
background = transform.scale(image.load('bg.jpg'), (700,700))

game = True
clock = time.Clock()
fps = 60
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    window.blit(background, (0,0))
    clock.tick(fps)
    display.update()