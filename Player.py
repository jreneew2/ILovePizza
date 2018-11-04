import pygame
from utilities import load_png

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        #pygame.display.init()
        self.image, self.rect = load_png('kang.png')

        self.isMoving = False
        self.key = pygame.K_m #can't create an empty variable or something smh

        self.velX = 0
        self.velY = 0
        self.accX = 0
        self.accY = 0
        self.posX = 100
        self.posY = 100
        self.rect.x = 100
        self.rect.y = 100
        self.speed = 500

        screen = pygame.display.get_surface()
        self.area = screen.get_rect()

    def update_bounds(self):
        self.rect.x = self.posX - self.image.get_width() / 2
        self.rect.y = self.posY - self.image.get_height() / 2

    def input(self, up, down, left, right):
        if(up):
            self.velY = -self.speed
        elif(down):
            self.velY = self.speed
        else:
            self.velY = 0
        if(left):
            self.velX = -self.speed
        elif(right):
            self.velX = self.speed
        else:
            self.velX = 0

    def calc_pos(self, deltatime):
        if(self.rect.right >= self.area.width or self.rect.left <= 0):
            self.velX = self.velX * -1
        if(self.rect.bottom >= self.area.height or self.rect.top <= 0):
            self.velY = self.velY * -1

        self.velX = self.velX + self.accX * deltatime
        self.velY = self.velY + self.accY * deltatime

        self.posX = self.posX + self.velX * deltatime
        self.posY = self.posY + self.velY * deltatime

        self.update_bounds()

        print("velX: " + str(self.velX))
        print("velY: " + str(self.velY))
        print("posX: " + str(self.posX))
        print("posY: " + str(self.posY))

    def draw(self, screen): 
        screen.blit(self.image, (self.posX - self.image.get_width() / 2, self.posY - self.image.get_height() / 2))

        

