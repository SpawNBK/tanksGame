from playeranimation import PlayerAnimation
from bullet import Bullet


class Player:

    def __init__(self):
        self.x = 50
        self.y = 50
        self.width = 42
        self.height = 42
        self.speed = 5
        self.left = False
        self.right = False
        self.up = False
        self.down = False
        self.animCount = 0
        self.stageGrown = 1
        self.sprites = {}
        self.loadSprites()
        self.spawned = False
        self.bullets = []
        self.lastMove = 'UP'


    def markDrive(self, position):
        if position == 'LEFT':
            self.left = True
            self.right = False
            self.up = False
            self.down = False
            self.lastMove = 'LEFT'
        elif position == 'RIGHT':
            self.left = False
            self.right = True
            self.up = False
            self.down = False
            self.lastMove = 'RIGHT'
        elif position == 'UP':
            self.left = False
            self.right = False
            self.up = True
            self.down = False
            self.lastMove = 'UP'
        elif position == 'DOWN':
            self.left = False
            self.right = False
            self.up = False
            self.down = True
            self.lastMove = 'DOWN'

    def getDriveWay(self):
        way = 'driveUp'
        if self.left:
            way = 'driveLeft'
        elif self.right:
            way = 'driveRight'
        elif self.up:
            way = 'driveUp'
        elif self.down:
            way = 'driveDown'
        return self.sprites[way][self.animCount // 5]

    def loadSprites(self):
        self.sprites = PlayerAnimation.getSprites(self.stageGrown)

    def spawn(self):
        if self.spawned:
            return True
        else:
            self.spawned = True
            return False

    def newBullet(self):
        bullet = None
        if self.lastMove == 'UP':
            bullet = Bullet(round(self.x + self.width // 2), self.y, 5, (255, 0, 0),
                            self.lastMove)
        elif self.lastMove == 'DOWN':
            bullet = Bullet(round(self.x + self.width // 2), (self.y + self.height), 5, (255, 0, 0),
                            self.lastMove)
        elif self.lastMove == 'RIGHT':
            bullet = Bullet((self.x + self.width), round(self.y + self.height // 2), 5, (255, 0, 0),
                            self.lastMove)
        else:
            bullet = Bullet(self.x, round(self.y + self.height // 2), 5, (255, 0, 0), self.lastMove)
        self.bullets.append(bullet)

    def getX(self):
        return int(self.x)

    def getY(self):
        return int(self.y)

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height

    def getSpeed(self):
        return int(self.speed)

    def getAnimCount(self):
        return self.animCount

    def getStageGrown(self):
        return self.stageGrown

    def setStageGrown(self, stagegrown):
        self.stageGrown = stagegrown

    def setX(self, x):
        self.x = x

    def setY(self, y):
        self.y = y

    def setWidth(self, width):
        self.width = width

    def setHeight(self, height):
        self.height = height

    def setSpeed(self, speed):
        self.speed = speed

    def setAnimCount(self, count):
        self.animCount = count
