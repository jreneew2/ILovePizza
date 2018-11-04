import pygame
from utilities import load_png

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        #pygame.display.init()
        self.image, self.rect = load_png('playerr.png')

        self.isMoving = False
        self.key = pygame.K_m #can't create an empty variable or something smh

        screen = pygame.display.get_surface()


        self.velX = 0
        self.velY = 0
        self.accX = 0
        self.accY = 0
        self.posX = 100
        self.posY = 100
        self.rect.x = 100
        self.rect.y = 100
        self.speed = 500

        self.area = screen.get_rect()

    def update_bounds(self):
        self.rect.x = self.posX - self.image.get_width() / 2
        self.rect.y = self.posY - self.image.get_height() / 2

    def input(self, up, down, left, right):
        lastangle = 0
        previousRect = self.rect
        if(up):
            self.velY = -self.speed
            self.image, self.rect = load_png('playert.png')
            self.rect.x = previousRect.x
            self.rect.y = previousRect.y
        elif(down):
            self.velY = self.speed
            self.image, self.rect = load_png('playerd.png')
            self.rect.x = previousRect.x
            self.rect.y = previousRect.y
        else:
            self.velY = 0
        if(left):
            self.velX = -self.speed
            self.image, self.rect = load_png('playerl.png')
            self.rect.x = previousRect.x
            self.rect.y = previousRect.y
        elif(right):
            self.velX = self.speed
            self.image, self.rect = load_png('playerr.png')
            self.rect.x = previousRect.x
            self.rect.y = previousRect.y
        else:
            self.velX = 0

        if(up and right):
            self.image, self.rect = load_png('playertr.png')
            self.rect.x = previousRect.x
            self.rect.y = previousRect.y
        elif(up and left):
            self.image, self.rect = load_png('playertl.png')
            self.rect.x = previousRect.x
            self.rect.y = previousRect.y
        elif(down and left):
            self.image, self.rect = load_png('playerdl.png')
            self.rect.x = previousRect.x
            self.rect.y = previousRect.y
        elif(down and right):
            self.image, self.rect = load_png('playerdr.png')
            self.rect.x = previousRect.x
            self.rect.y = previousRect.y          

    def calc_pos(self, deltatime):
        if(self.rect.right > self.area.width or self.rect.left < 0):
            if(self.rect.right > self.area.width):
                if(self.velX > 0):
                    self.velX = 0
            if(self.rect.left < 0):
                if(self.velX < 0):
                    self.velX = 0
        if(self.rect.bottom > self.area.height or self.rect.top < 0):
            if(self.rect.bottom > self.area.height):
                if(self.velY > 0):
                    self.velY = 0
            if(self.rect.top < 0):
                if(self.velY < 0):
                    self.velY = 0

        self.velX = self.velX + self.accX * deltatime
        self.velY = self.velY + self.accY * deltatime

        self.posX = self.posX + self.velX * deltatime
        self.posY = self.posY + self.velY * deltatime

        self.update_bounds()

    def draw(self, screen): 
        screen.blit(self.image, (self.posX - self.image.get_width() / 2, self.posY - self.image.get_height() / 2))
        pygame.draw.rect(pygame.display.get_surface(), (0, 255, 0), self.rect, 2)

        

