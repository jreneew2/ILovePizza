import pygame
from Player import Player

class Game:
    done = False
    height = 540
    width = 1080
    def __init__(self):
        pygame.init()
        screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Pizza Game')

        bgcolor = (255, 255, 255)
        background = pygame.Surface(screen.get_size())
        background = background.convert()
        background.fill(bgcolor)

        screen.blit(background, (0,0))
        pygame.display.flip()

        self.p = Player()
        playerSprite = pygame.sprite.RenderPlain(self.p)
        self.p.draw(screen)
        myfont = pygame.font.SysFont('Times New Roman MS', 30)
        text = myfont.render("Wegman's Official Game OwO", 0, (255, 50, 20))
        clock = pygame.time.Clock()
        while not self.done:
            timedelta = clock.tick(60)
            timedelta = timedelta / 1000
            keystate = pygame.key.get_pressed()
            self.p.input(keystate[pygame.K_w], keystate[pygame.K_s], keystate[pygame.K_a], keystate[pygame.K_d])
            self.p.calc_pos(timedelta)
            self.p.draw(screen)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.done = True
                elif event.type == pygame.KEYDOWN:
                    passKey = event.key
                    self.getInput(passKey)
                    
            screen.blit(text, ((self.width/2)-60, self.height/2))
            pygame.display.update()
            screen.blit(background, (0,0))

    def getInput(self, passKey):
        if passKey == pygame.K_q:
            self.done = True
        if passKey == pygame.K_UP or passKey == pygame.K_DOWN or passKey == pygame.K_LEFT or passKey == pygame.K_RIGHT:
            print("key")
            #self.p.move(passKey)
            

            

def main():
    Game()
main()
