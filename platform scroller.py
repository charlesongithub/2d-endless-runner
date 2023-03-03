import pygame, sys
pygame.init()

screen = pygame.display.set_mode((1400,700))
pygame.display.set_caption('platform scroller')
bg_image = pygame.image.load('sky background.png')

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)
GREEN = ('#34d960')

screen.blit(bg_image, (0, 0))
pygame.display.flip()

class Platform:
    def __init__(self, x, colour):
        self.x = x
        self.y = 400
        self.colour = colour
        self.rect = pygame.Rect(self.x, self.y, 1400, 300)
    def update(self):
        self.x -= 2
        pygame.draw.rect(screen, self.colour, (self.x, self.y, 1400, 300))
    def check(self):
        if self.x == -1400:
            self.x = 1400

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.x = 100
        self.y = 100
        self.w = 20
        self.h = 20
        self.momentum = 0
        self.dir = 0
        self.colour = BLACK
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
    def update(self):
        self.dir = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] and self.x < 1380:
            self.dir = 10
        if keys[pygame.K_LEFT] and self.x > 0:
            self.dir = -10
        if self.dir == 10 and self.rect.right + self.dir > obstacle.x and self.rect.bottom > obstacle.rect.top and self.rect.right < obstacle.x:
            self.dir = obstacle.x - self.rect.right
        if self.dir == -10 and self.rect.right + self.dir < obstacle.x and self.rect.bottom > obstacle.rect.top and self.x > obstacle.rect.right:
            self.dir = obstacle.rect.right - self.x
        self.x += self.dir
        if keys[pygame.K_UP] and self.y > 5 and player.momentum == 0:
            if player.rect.bottom == red.rect.top or player.rect.bottom == yellow.rect.top or player.rect.bottom == obstacle.rect.top:
                player.momentum = -30
        pygame.draw.rect(screen, self.colour, (self.x, self.y, self.w, self.h))
        
class Obstacle:
    def __init__(self):
        self.x = 800
        self.y = 300
        self.w, self.h = 300, 100
        self.colour = GREEN
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
    def update(self):
        if self.rect.left > -300:
            if player.rect.right != self.x:
                self.x -= 2
            if player.rect.right == self.x and player.rect.bottom > obstacle.rect.top:
                self.x -= 2
                player.x -= 2
        elif self.rect.left <= -300:
            self.x += 1700
        if player.x < 0:
            player.x = 100
            player.y = 100
        pygame.draw.rect(screen, self.colour, (self.x, self.y, self.w, self.h))

def collisions_check():
    player.y += player.momentum
    if player.momentum < 0:
        player.momentum += 1.5
    grav = 10
    red.rect = pygame.Rect(red.x, red.y, 1400, 300)
    yellow.rect = pygame.Rect(yellow.x, yellow.y, 1400, 300)
    obstacle.rect = pygame.Rect(obstacle.x, obstacle.y, obstacle.w, obstacle.h)
    player.rect = pygame.Rect(player.x, player.y, player.w, player.h)
    if player.y + player.momentum <= 0:
        player.momentum = 0 - player.rect.top
    if red.rect.colliderect(player.rect.x, player.rect.y + grav, player.w, player.h) or yellow.rect.colliderect(player.rect.x, player.rect.y + grav, player.w, player.h):
        grav = player.rect.bottom - red.rect.top
        player.momentum = 0
    if obstacle.rect.colliderect(player.rect.x, player.rect.y + player.momentum + grav, player.w, player.h):
        grav = player.rect.bottom - obstacle.rect.top
        player.momentum = 0
    player.y += grav

player = Player()
red = Platform(0, RED)
yellow = Platform(1400, YELLOW)
obstacle = Obstacle()

clock = pygame.time.Clock()
while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.blit(bg_image, (0, 0))
    obstacle.update()
    collisions_check()
    player.update()
    if player.y > red.y:
        player.x, player.y = 100, 100
    red.update()
    yellow.update()
    red.check()
    yellow.check()
    pygame.display.flip()
