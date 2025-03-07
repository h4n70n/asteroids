import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

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

    #Create groups for game objects
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    space_rocks = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updateable, drawable)
    Asteroid.containers = (space_rocks, updateable, drawable)
    AsteroidField.containers = (updateable)
    Shot.containers = (shots, updateable, drawable)

    #Draw Player
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player_ship = Player(x, y)  

    #Draw Asteroids
    asteroid_field = AsteroidField()

    #Game Loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        #draw a black screen
        screen.fill((0, 0, 0))
        
        #draw 
        for item in drawable:
            item.draw(screen)
        
        #update player
        updateable.update(dt)

        #detect ship collisions
        for asteroid in space_rocks:
            if player_ship.collides_with(asteroid):
                print("Game over!")
                exit()
        
        #destory asteroids
        for asteroid in space_rocks:
            for shot in shots:
                if asteroid.collides_with(shot):
                    asteroid.kill()
                    shot.kill()

        #refresh screen
        pygame.display.flip()

        #Increment Clock
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()