import pygame 
from random import randint 
pygame.init()

screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()
running = True

pygame.display.set_caption("Space shooter")
background = pygame.image.load("space.jpg")
background = pygame.transform.scale(background, (1280, 720 ))

#pygame.mixer.init()
#pygame.mixer.music.load("201745.mp3") 
# Set the music volume:
#pygame.mixer.music.set_volume(0.1)
#pygame.mixer.music.play()




class GameSprite(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, filename):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(filename), (width,height))
        self.rect = pygame.Rect(x,y,width,height)
        self.rect.x = x
        self.rect.y = y  
    def render(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))


class Enemy(GameSprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y,):
        super().__init__(player_x, player_y, size_x, size_y, player_image)
        self.direction = "down"
        self.speed = 1
    def respawn (self):
        self.rect.y = -100
        self.rect.x = randint(10,720)
                
    def update(self):
        self.rect.y += self.speed
        if self.rect.y > 500:
            self.respawn()

class Projectile(GameSprite):
    def __init__(self, x, y,):
        super().__init__(x, y, 25, 25, "bullet.png")
        self.speed = 10
        bullets.add(self)
    def update(self):
        self.rect.y -= self.speed 
        if self.rect.y < -10:
            bullets.remove(self)


pygame.font.init()
my_font = pygame.font.Font(None, 60)
end_text = my_font.render("Game Over!", True, "purple")

hud_font = pygame.font.Font(None, 30)
enemies_missed = 0
enemies_missed_text = hud_font.render("Enemies Missed: 0", True, "white")
score = 0 
score_text = hud_font.render("Score: 0", True, "white")


class Player():
    def __init__ (self, x, y, width, height, filename, speed=3, left=pygame.K_a, right=pygame.K_d, up=pygame.K_w, down=pygame.K_s): 

        print(filename)
        self.image = pygame.transform.scale(pygame.image.load(filename), (width, height))
        self.speed = speed
        self.left = left
        self.right = right
        self.up = up
        self.down = down
        self.rect = pygame.Rect(x, y, width, height)  
        self.canshoot = True
    def update(self):
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[self.left]:
            self.rect.x -= self.speed
        if keys_pressed[self.right]:
            self.rect.x += self.speed
        if keys_pressed[self.up]:
            self.rect.y -= self.speed
        if keys_pressed[self.down]:
            self.rect.y += self.speed
        if keys_pressed[pygame.K_SPACE]:
            if self.canshoot:
                self.canshoot = False    
                Projectile(self.rect.x+62, self.rect.y+30)

        else:
            self.canshoot = True

    def render(self):     
         #pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)
         screen.blit (self.image, (self.rect.x, self.rect.y)) 

player = Player(200, 400, 150, 150, "rocket.png")
enemies = pygame.sprite.Group()
for i in range(5):
    enemies.add(Enemy("ufo.png", 100, -50, 120, 100))
bullets = pygame.sprite.Group()

    
    
player_image = pygame.transform.scale(pygame.image.load("rocket.png"), (100,100))

enemy = Enemy("ufo.png", 500, 10, 150, 170) 

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.blit(background,(0, 0))
    screen.blit(score_text, (20, 50))

    #UPDATE
    player.update()
    enemies.update()
    bullets.update()
 

    collided = pygame.sprite.groupcollide(enemies, bullets, False, True)
    for enemy in list(collided.keys()): 
        score += 1
        score_text = hud_font.render("Score:" +str(score), True, "white")
        enemy.respawn()

    collided = pygame.sprite.spritecollide(player, enemies, False)
    for enemy in collided:
        gameover = True
        enemy.respawn()

    #RENDER
    player.render()
    enemies.draw(screen)
    bullets.draw(screen)
    




    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()



