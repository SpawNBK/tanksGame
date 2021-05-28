import pygame


class Bullet:

    def __init__(self, x, y, radius, color, facing):
        self.x = int(x)
        self.y = int(y)
        self.raduis = radius
        self.color = color
        if facing == 'LEFT' or facing == 'UP':
            self.facing = -1
        else:
            self.facing = 1
        self.vel = 8 * self.facing
        if facing == 'LEFT' or facing == 'RIGHT':
            #x ord
            self.plane = 0
        else:
            #y ord
            self.plane = 1


    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.raduis)
