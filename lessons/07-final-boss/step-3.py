import math
import random

import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Most Wanted UFO Mini")
clock = pygame.time.Clock()

background = pygame.image.load("assets/background_4.png").convert()
player_image = pygame.image.load("assets/player_1.png").convert_alpha()
bullet_image = pygame.image.load("assets/Bullet.gif").convert_alpha()
enemy_image = pygame.image.load("assets/enemy_1.png").convert_alpha()
boss_image = pygame.image.load("assets/boss.png").convert_alpha()
shoot_sound = pygame.mixer.Sound("assets/shoot.wav")
hit_sound = pygame.mixer.Sound("assets/collision.wav")
lose_sound = pygame.mixer.Sound("assets/loselife.wav")
font = pygame.font.Font(None, 36)
big_font = pygame.font.Font(None, 80)


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = enemy_image
        self.rect = self.image.get_rect()
        self.reset()

    def reset(self):
        self.rect.midbottom = (random.randint(20, 780), random.randint(-500, -40))
        self.speed = random.randint(1, 2)

    def update(self):
        self.rect.y += self.speed


class Boss(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale2x(boss_image)
        self.rect = self.image.get_rect()
        self.angle = 0
        self.health = 10

    def update(self):
        self.angle += 0.03
        self.rect.center = (400 + math.cos(self.angle) * 250,
                            150 + math.sin(self.angle) * 60)


def draw_centered(text, font, y):
    image = font.render(text, True, (255, 255, 255))
    screen.blit(image, image.get_rect(center=(400, y)))


player = player_image.get_rect(midbottom=(400, 590))
speed = 6
bullets = []
cooldown = 0
enemies = pygame.sprite.Group(Enemy() for _ in range(8))
score = 0
lives = 3
boss = None
state = "menu"

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN and state not in ("playing", "paused"):
                state = "playing"
                player.midbottom = (400, 590)
                score = 0
                lives = 3
                bullets = []
                boss = None
                for enemy in enemies:
                    enemy.reset()
            elif event.key == pygame.K_p and state == "playing":
                state = "paused"
            elif event.key == pygame.K_p and state == "paused":
                state = "playing"

    if state == "playing":
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.x -= speed
        if keys[pygame.K_RIGHT]:
            player.x += speed
        player.clamp_ip(screen.get_rect())

        if cooldown > 0:
            cooldown -= 1
        if keys[pygame.K_SPACE] and cooldown == 0:
            bullets.append(bullet_image.get_rect(midbottom=player.midtop))
            shoot_sound.play()
            cooldown = 15

        for bullet in bullets:
            bullet.y -= 10
        bullets = [b for b in bullets if b.bottom > 0]
        enemies.update()

        for enemy in enemies:
            hit = enemy.rect.collidelist(bullets)
            if hit != -1:
                bullets.pop(hit)
                enemy.reset()
                score += 10
                hit_sound.play()
            elif enemy.rect.top > 600 or enemy.rect.colliderect(player):
                enemy.reset()
                lives -= 1
                lose_sound.play()
        if boss is None and score >= 100:
            boss = Boss()
        if boss is not None:
            boss.update()
            hit = boss.rect.collidelist(bullets)
            if hit != -1:
                bullets.pop(hit)
                boss.health -= 1
                hit_sound.play()
                if boss.health <= 0:
                    score += 500
                    state = "won"
        if lives <= 0:
            state = "game_over"

    screen.blit(background, (0, 0))
    if state == "menu":
        draw_centered("Most Wanted UFO Mini", big_font, 250)
        draw_centered("Press ENTER to play", font, 340)
    else:
        enemies.draw(screen)
        for bullet in bullets:
            screen.blit(bullet_image, bullet)
        screen.blit(player_image, player)
        hud = font.render(f"Score: {score}   Lives: {lives}", True, (255, 255, 255))
        screen.blit(hud, (10, 10))
    if state == "paused":
        draw_centered("PAUSED", big_font, 300)
    if state == "game_over":
        draw_centered("GAME OVER", big_font, 250)
        draw_centered(f"Score: {score}  -  ENTER to play again", font, 340)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
