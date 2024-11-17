import pygame 
from random import randint 
pygame.init()

screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()
running = True

pygame.display.set_caption("Space shooter")
background = pygame.image.load("space.jpg")
background = pygame.transform.scale(background, (1280, 720 ))
