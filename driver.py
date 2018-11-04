import pygame
from Player import Player
from Shelf import Shelf
import json
import random

class Game:
    done = False
    height = 720
    width = 1280
    recipes = list()
    def __init__(self):
        pygame.init()
        screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Pizza Game')

        recipeName, ingredients = self.genRecipe()
        print(recipeName)
        print(ingredients)

        bgcolor = (255, 255, 255)
        background = pygame.image.load("bg_image.png")
        background = pygame.transform.scale(background, (self.width, self.height))

        screen.blit(background, (0,0))
        pygame.display.flip()

        self.p = Player()
        playerSprite = pygame.sprite.RenderPlain(self.p)
        self.p.draw(screen)

        self.s1 = Shelf(0)
        self.s2 = Shelf(1)
        self.s3 = Shelf(2)
        self.s4 = Shelf(3)
        shelfSprite1 = pygame.sprite.RenderPlain(self.s1)
        shelfSprite2 = pygame.sprite.RenderPlain(self.s2)
        shelfSprite3 = pygame.sprite.RenderPlain(self.s3)
        shelfSprite4 = pygame.sprite.RenderPlain(self.s4)
        self.s1.draw(screen)
        self.s2.draw(screen)
        self.s3.draw(screen)
        self.s4.draw(screen)
        
        myfont = pygame.font.SysFont('Times New Roman MS', 30)
        text = myfont.render(recipeName, 0, (255, 50, 20))
        ingredientsText = list()
        for k, v in ingredients.items():
            ingredientsText.append(myfont.render(k + ": $" + str(v), 0, (255, 50, 20)))

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

            self.s1.draw(screen)
            self.s2.draw(screen)
            self.s3.draw(screen)
            self.s4.draw(screen)       
            screen.blit(text, (10, 10))
            x = 30
            for text in ingredientsText:
                screen.blit(text, (10, x))
                x = x + 30
            pygame.display.update()
            screen.blit(background, (0,0))

    def getInput(self, passKey):
        if passKey == pygame.K_q:
            self.done = True
        if passKey == pygame.K_UP or passKey == pygame.K_DOWN or passKey == pygame.K_LEFT or passKey == pygame.K_RIGHT:
            print("key")
            #self.p.move(passKey)

    def loadRecipes(self):
        recipes = list()
        with open('data.json') as data:
            recipe = json.load(data)
            data.close()
        return recipe

    def genRecipe(self):
        recipes = self.loadRecipes()
        randomPick = random.randint(0, len(recipes) - 1)
        randomRecipeName = list(recipes.keys())[randomPick]
        randomRecipeIngredients = list(recipes.values())[randomPick]
        del recipes[randomRecipeName]
        return (randomRecipeName, randomRecipeIngredients)
            

            

def main():
    Game()
main()
