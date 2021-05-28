import sys
import pygame
from player import Player

player = Player()


def drawScreen(screen, gamePlayer):
    screen.fill((0, 0, 0))
    if gamePlayer.getAnimCount() + 1 >= 30:
        gamePlayer.setAnimCount(0)
    if gamePlayer.left:
        screen.blit(pygame.image.load(gamePlayer.sprites["driveLeft"][gamePlayer.getAnimCount() // 5]),
                    (gamePlayer.getX(), gamePlayer.getY()))
        gamePlayer.setAnimCount(gamePlayer.getAnimCount() + 1)
    elif gamePlayer.right:
        screen.blit(pygame.image.load(gamePlayer.sprites["driveRight"][gamePlayer.getAnimCount() // 5]),
                    (gamePlayer.getX(), gamePlayer.getY()))
        gamePlayer.setAnimCount(gamePlayer.getAnimCount() + 1)
    elif gamePlayer.up:
        screen.blit(pygame.image.load(gamePlayer.sprites["driveUp"][gamePlayer.getAnimCount() // 5]),
                    (gamePlayer.getX(), gamePlayer.getY()))
        gamePlayer.setAnimCount(gamePlayer.getAnimCount() + 1)
    elif gamePlayer.down:
        screen.blit(pygame.image.load(gamePlayer.sprites["driveDown"][gamePlayer.getAnimCount() // 5]),
                    (gamePlayer.getX(), gamePlayer.getY()))
        gamePlayer.setAnimCount(gamePlayer.getAnimCount() + 1)
    else:
        if not gamePlayer.spawn():
            screen.blit(pygame.image.load(player.sprites["driveUp"][0]),
                        (player.getX(), player.getY()))
        else:
            screen.blit(pygame.image.load(player.getDriveWay()),(player.getX(), player.getY()))

    for bullet in gamePlayer.bullets:
        bullet.draw(screen)
    pygame.display.flip()


def run_game():
    global player
    pygame.init()
    clock = pygame.time.Clock()
    gamemode = {'width': 800, 'height': 800}
    screen = pygame.display.set_mode((gamemode['width'], gamemode['height']))
    pygame.display.set_caption("Tanks Game")
    while True:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_f:
                    if len(player.bullets) < 2:
                        player.newBullet()

        for bullet in player.bullets:
            if bullet.plane == 0:
                if bullet.x < gamemode['width'] and bullet.x > 0:
                    bullet.x += bullet.vel
                else:
                    player.bullets.pop(player.bullets.index(bullet))
            else:
                if bullet.y < gamemode['height'] and bullet.y > 0:
                    bullet.y += bullet.vel
                else:
                    player.bullets.pop(player.bullets.index(bullet))

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and player.getX() > 5:
            player.setX(player.getX() - player.getSpeed())
            player.markDrive('LEFT')
        elif keys[pygame.K_RIGHT] and player.getX() < gamemode['width'] - player.getWidth() - 5:
            player.setX(player.getX() + player.getSpeed())
            player.markDrive('RIGHT')
        elif keys[pygame.K_UP] and player.getY() > 5:
            player.setY(player.getY() - player.getSpeed())
            player.markDrive('UP')
        elif keys[pygame.K_DOWN] and player.getY() < gamemode['height'] - player.getHeight() - 5:
            player.setY(player.getY() + player.getSpeed())
            player.markDrive('DOWN')
        else:
            player.setAnimCount(0)
        drawScreen(screen, player)


run_game()