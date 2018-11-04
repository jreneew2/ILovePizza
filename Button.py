import pygame
from utilities import load_png

class Button(pygame.sprite.Sprite):
    """Class used to create a button, use setCords to set 
        position of topleft corner. Method pressed() returns
        a boolean and should be called inside the input loop."""
    def __init__(self, yesno):
        pygame.sprite.Sprite.__init__(self)
        if(yesno):
            self.image, self.rect = load_png('buttony.png')
        else:
            self.image, self.rect = load_png('buttonn.png')


    def setCords(self,x,y):
        self.rect.x = x
        self.rect.y = y

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
        pygame.draw.rect(pygame.display.get_surface(), (0, 255, 0), self.rect, 2)

    def pressed(self,mouse):
        return self.rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]