import pygame
import sys
from pygame.locals import *
import random
import time

pygame.init()
vec = pygame.math.Vector2 #2D vector 

HEIGHT = 450
WIDTH = 400
ACC = 0.5
FRIC = -0.12
FPS = 60
JUMP = -15
HARD = 6

FramePerSec = pygame.time.Clock()

displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("GAME")

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((30,30))
        self.surf.fill((255,128,255))
        self.rect = self.surf.get_rect(center = (100,420))

        self.pos = vec(100, 420)
        self.vel = vec(0, 0) 
        self.acc = vec(0, 0)

        self.jumping = False
        self.score = 0

    def move(self):
        self.acc = vec(0, 0.5)
        pressed_keys = pygame.key.get_pressed()

        if pressed_keys[K_LEFT]:
            self.acc.x = -ACC
        if pressed_keys[K_RIGHT]:
            self.acc.x = ACC
        
        self.acc.x += self.vel.x * FRIC
        self.acc.y += self.vel.y * -0.01
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        # Check screen bounderies
        if self.pos.x > WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = WIDTH

        # Set position
        self.rect.midbottom = self.pos

    def update(self):
        # self.move(self)
        hits = pygame.sprite.spritecollide(self, platforms, False)
        if self.vel.y > 0:
            if hits:
                if self.pos.y < hits[0].rect.bottom:
                    if hits[0].point == True:
                        hits[0].point = False
                        self.score += 1
                    self.pos.y = hits[0].rect.top + 1
                    self.vel.y = 0
                    self.jumping = False

    def jump(self):
        hits = pygame.sprite.spritecollide(P1, platforms, False)
        if hits and not self.jumping:
            self.jumping = True
            self.vel.y = JUMP

    def cancel_jump(self):
        if self.jumping:
            if self.vel.y < -3:
                self.vel.y = -3

class platform(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((random.randint(50,100), 12))
        self.surf.fill((0,255,0))
        self.rect = self.surf.get_rect(center = (random.randint(0, WIDTH-10), random.randint(0,HEIGHT-30)))
        self.speed = random.randint(-1,1)
        self.moving = True
        self.point = True

    def move(self):
        if self.moving == True:
            self.rect.move_ip(self.speed,0)
            if self.speed > 0 and self.rect.left > WIDTH:
                self.rect.right = 0
            if self.speed < 0 and self.rect.right < 0:
                self.rect.left = WIDTH



def gen_plat():
    while len(platforms) < HARD:
        width = random.randrange(50, 200)
        C = True
        
        while C:
            p = platform()
            p.rect.center = (random.randrange(0, WIDTH - width), random.randrange(-50, 0))
            C = check(p, platforms)

        platforms.add(p)
        all_sprites.add(p)

def check(platform, groupies):
    if pygame.sprite.spritecollideany(platform, groupies):
        return True
    else:
        for entity in groupies:
            if entity == platform:
                continue
            if (abs(platform.rect.top - entity.rect.bottom) < 35) and (abs(platform.rect.bottom - entity.rect.top) < 35):
                return True
        return False


# Create player
P1 = Player()

# Base platform
PT1 = platform()
PT1.surf = pygame.Surface((WIDTH, 20))
PT1.surf.fill((255,0,0))
PT1.rect = PT1.surf.get_rect(center = (WIDTH/2, HEIGHT - 10))
PT1.moving = False
PT1.point = False

# Group all sprites
all_sprites = pygame.sprite.Group()
all_sprites.add(PT1)
all_sprites.add(P1)

# Platforms
platforms = pygame.sprite.Group()
platforms.add(PT1)
for y in range(random.randint(5, 6)):
    pl = platform()
    pl.rect.center = (pl.rect.center[0], HEIGHT - (y+1)*75)
    platforms.add(pl)
    all_sprites.add(pl)


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                P1.jump()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                P1.cancel_jump()
            
    if P1.rect.top > HEIGHT:
        for entity in all_sprites:
            entity.kill()
        displaysurface.fill((255, 0, 0))
        f = pygame.font.SysFont("Verdana", 64)
        g = f.render(str(P1.score), True, (255,255,255))
        g_rect = g.get_rect(center=(WIDTH/2, HEIGHT/2))
        displaysurface.blit(g,g_rect)
        pygame.display.update()
        time.sleep(2)
        pygame.quit()
        sys.exit()

    # Background
    displaysurface.fill((0,0,0))
    f = pygame.font.SysFont("Verdana", 32)
    g = f.render(str(P1.score), True, (123,255,0))
    g_rect = g.get_rect(center=(WIDTH/2, 20))
    displaysurface.blit(g,g_rect)

    # Move and update player
    P1.update()

    # Scrolling
    if P1.rect.top <= HEIGHT/3:
        P1.pos.y += abs(P1.vel.y)
        for plat in platforms:
            plat.rect.y += abs(P1.vel.y)
            if plat.rect.top >= HEIGHT:
                plat.kill()

    gen_plat()

    # Display sprites
    for entity in all_sprites:
        displaysurface.blit(entity.surf, entity.rect)
        entity.move()

    pygame.display.update()
    FramePerSec.tick(FPS)