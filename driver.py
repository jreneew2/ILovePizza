import pygame

class Game:
    def __init__(self):
        pygame.init()
        height = 540
        width = 1080
        screen = pygame.display.set_mode((1080, 540))
        pygame.display.set_caption('Pizza Game')
        bgcolor = (0, 0, 255)

        background = pygame.Surface(screen.get_size())
        background = background.convert()
        background.fill(bgcolor)

        screen.blit(background, (0,0))
        pygame.display.flip()

        clock = pygame.time.Clock()

        myfont = pygame.font.SysFont('Times New Roman MS', 30)
        text = myfont.render("Wegman's Official Game OwO", 0, (255, 50, 20))

        done = False

        while not done:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                elif event.type == pygame.KEYDOWN:
                    passKey = event.key
                    self.getInput(passKey)
                    
            screen.blit(text, ((width/2)-60, height/2))
            pygame.display.update()
            pygame.display.flip()
            
    def getInput(self, passKey):
        print("wubbalubbadubudub")

def main():
    Game()
main()
