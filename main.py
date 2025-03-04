import pygame
from constants import *
from player import *

def main():
    pygame.init()
    
    #Create game window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids")
    
    #Console messages
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    #initialize clock
    clock = pygame.time.Clock()
    dt = 0

    #Draw Player
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player_ship = Player(x, y)

    #Game Loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        #draw a black screen
        screen.fill((0, 0, 0))
        
        #draw player
        player_ship.draw(screen)
        
        #refresh screen
        pygame.display.flip()


        #Increment Clock
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()