import pygame
from random import randint
import time
import math

pygame.init()

FPS = 60

WIDTH , HEIGHT = 800, 800
NO_ROWS :int = 4
NO_COLS = 4

RECT_WIDTH = WIDTH // NO_COLS
RECT_HEIGHT = HEIGHT // NO_ROWS

OUTLINE_COLOR = (187, 173, 160) #gray
OUTLINE_THICKNESS = 10
BACKGROUND_COLOR = (205, 192, 180)#diff shade of grade

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2048")

FONT = pygame.font.SysFont("comicsans", 60, bold = True)
MOVE_VEL = 20

def main():
    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break


if __name__ == "__main__":
    main()
    pygame.quit()







