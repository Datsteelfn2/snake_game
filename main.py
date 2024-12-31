import pygame,random
from pygame.math import Vector2


class SNAKE:
    def __init__(self):
        self.body=[Vector2(5,10),Vector2(6,10),Vector2(7,10)]
    def draw_snake(self):
        for block in self.body:
            blcok_rect=pygame.Rect((block.x*cell_size),(block.y*cell_size),cell_size,cell_size)
            pygame.draw.rect(window,(183,111,122),blcok_rect)
class FRUIT:
    def __init__(self):
        #x and y position
        #draw a square(fruit)
        self.x=random.randint(0,cell_number-1)
        self.y=random.randint(0,cell_number-1)
        self.position=Vector2(self.x,self.y)
    def draw_fruit(self):
        fruit_rect=pygame.Rect(self.position.x*cell_size,self.position.y*cell_size,cell_size,cell_size)
        pygame.draw.rect(window,(126,166,114),fruit_rect)

pygame.init()
window_width,window_height=400,500
cell_size=40
cell_number=20
window=pygame.display.set_mode((cell_size*cell_number,cell_size*cell_number))

fruit=FRUIT()
snake=SNAKE()
clock=pygame.time.Clock()

run=True
while run:
    for events in pygame.event.get():
        if events.type==pygame.QUIT:
            run=False

    window.fill((175,215,70))
    fruit.draw_fruit()
    snake.draw_snake()
    clock.tick(60)
    pygame.display.update()