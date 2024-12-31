import pygame
from pygame.math import Vector2
class FRUIT:
    def __init__(self):
        #x and y position
        #draw a square(fruit)
        self.x=5
        self.y=4
        self.position=pygame.math.Vector2(self.x,self.y)
    def draw_fruit(self):
        fruit_rect=pygame.Rect(self.position.x,self.position.y,cell_size,cell_size)
        pygame.draw.rect(window,(126,166,114),fruit_rect)

pygame.init()
window_width,window_height=400,500
cell_size=40
cell_number=20
window=pygame.display.set_mode((cell_size*cell_number,cell_size*cell_number))

fruit=FRUIT()

clock=pygame.time.Clock()

run=True
while run:
    for events in pygame.event.get():
        if events.type==pygame.QUIT:
            run=False

    window.fill((175,215,70))
    fruit.draw_fruit()
    clock.tick(60)
    pygame.display.update()