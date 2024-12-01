#author Namitha
import pygame 
from random import randint 
pygame.init()

screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()
running = True

pygame.display.set_caption("Ping Pong Game")
background = pygame.image.load("Sky.jpg")
background = pygame.transform.scale(background, (1280, 720 ))


class GameSprite(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, filename):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(filename), (width,height))
        self.rect = pygame.Rect(x,y,width,height)
        self.rect.x = x
        self.rect.y = y  
    def render(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))

class Ball():
    pass

class Paddle(): 
      def __init__ (self, x, y, width, height, filename, speed=3, up=pygame.K_w, down=pygame.K_s): 

        print(filename)
        self.image = pygame.transform.scale(pygame.image.load(filename), (width, height))
        self.speed = speed
        self.up = up
        self.down = down
        self.rect = pygame.Rect(x, y, width, height)  
        self.canshoot = True
      def update(self):
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[self.up]:
            self.rect.y -= self.speed
        if keys_pressed[self.down]:
            self.rect.y += self.speed

        
      def render(self):     
         #pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)
         screen.blit (self.image, (self.rect.x, self.rect.y)) 


paddle = Paddle(200, 400, 150, 150, "Paddle.png",)


paddle_image = pygame.transform.scale(pygame.image.load("Paddle.png"), (100,100))




while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(background,(0, 0))

    #UPDATE
    paddle.update()    
     


    #RENDER
    paddle.render()   
  

             # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()



