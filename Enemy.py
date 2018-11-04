import pygame
from utilities import load_png
import random

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        #pygame.display.init()
        self.image, self.rect = load_png('playerr.png')

        self.isMoving = False
        self.key = pygame.K_m #can't create an empty variable or something smh

        screen = pygame.display.get_surface()


        self.velX = 500
        self.velY = 0
        self.accX = 0
        self.accY = 0
        self.posX = random.randint(1,11)*100
        self.posY = 50
        self.rect.x = 700
        self.rect.y = 100
        self.speed = 500
        self.diagspeed = 354

        self.area = screen.get_rect()

    def update_bounds(self):
        self.rect.x = self.posX - self.image.get_width() / 2
        self.rect.y = self.posY - self.image.get_height() / 2      

    def calc_pos(self, deltatime):
        if(self.rect.right > self.area.width or self.rect.left < 0):
            if(self.rect.right > self.area.width):
                self.velY = 500
                self.velX = 0
                self.image, self.rect = load_png('playerd.png')
            elif(self.rect.left < 0):
                self.velY = -500
                self.velX = 0
                self.image, self.rect = load_png('playert.png')
        if(self.rect.bottom > self.area.height - 200 or self.rect.top < 0):
            if(self.rect.bottom > self.area.height - 200):
                self.velX = -500
                self.velY = 0
                self.image, self.rect = load_png('playerl.png')
            elif(self.rect.top < 0):
                self.velX = 500
                self.velY = 0
                self.image, self.rect = load_png('playerr.png')

        self.velX = self.velX + self.accX * deltatime
        self.velY = self.velY + self.accY * deltatime

        self.posX = self.posX + self.velX * deltatime
        self.posY = self.posY + self.velY * deltatime

        self.update_bounds()

    def draw(self, screen): 
        screen.blit(self.image, (self.posX - self.image.get_width() / 2, self.posY - self.image.get_height() / 2))
        #pygame.draw.rect(pygame.display.get_surface(), (0, 255, 0), self.rect, 2)
