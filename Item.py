import pygame
from utilities import load_png
import random

class Item(pygame.sprite.Sprite):
    def __init__(self, shelf1, shelf2, shelf3, shelf4): 
        pygame.sprite.Sprite.__init__(self)
        foodchoices = ['Apple', 'Avocado', 'Bacon', 'Beer', 'Bread', 'Brownie', 'Cheese', 'Cherry', 'Chicken', 'Cookie', 'Eggs', 'Fish', 'Honey', 'Jam', 'Lemon', 'MelonHoneydew', 'Onion', 'Pickle', 'Sushi']
        self.image, self.rect = load_png('food/' + random.choice(foodchoices) + '.png')
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect()
        self.shelf1 = shelf1
        self.shelf2 = shelf2
        self.shelf3 = shelf3
        self.shelf4 = shelf4
        self.posX = 0
        self.posY = 0

    def findValidPos(self):
        rand = random.randint(1, 4)
        randX = 0
        randY = 0
        if(rand == 1):
            randX = random.randint(self.shelf1.left, self.shelf1.right)
            randY = random.randint(self.shelf1.top, self.shelf1.bottom)
        if(rand == 2):
            randX = random.randint(self.shelf2.left, self.shelf2.right)
            randY = random.randint(self.shelf2.top, self.shelf2.bottom)
        if(rand == 3):
            randX = random.randint(self.shelf3.left, self.shelf3.right)
            randY = random.randint(self.shelf3.top, self.shelf3.bottom)
        if(rand == 4):
            randX = random.randint(self.shelf4.left, self.shelf4.right)
            randY = random.randint(self.shelf4.top, self.shelf4.bottom)
        self.posX = randX
        self.posY = randY
        self.rect.x = randX
        self.rect.y = randY
        print('X: ' + str(self.posX))
        print('Y: ' + str(self.posY))

    def draw(self, screen, pos):
        screen.blit(self.image, (self.posX, self.posY))
        #pygame.draw.rect(screen, (0, 0, 255), self.rect, 2)

