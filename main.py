import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from player import Player
from asteroidfield import AsteroidField
from asteroid import Asteroid
from logger import log_event
import sys
from shot import Shot

def main():
    pygame.init()
    Clock=pygame.time.Clock()
    dt=0
    shots=pygame.sprite.Group()
    asteroids=pygame.sprite.Group()
    updatable=pygame.sprite.Group()
    drawable=pygame.sprite.Group()
    
    Shot.containers=(shots,updatable,drawable)
    Asteroid.containers=(asteroids,updatable,drawable)
    AsteroidField.containers=updatable
    asteroid_field=AsteroidField()
    
    Player.containers=(updatable,drawable)
    player=Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    
    screen=pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.collides_with(player):
               log_event("player_hit")
               print("Game over!")
               sys.exit(1)
               return
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collides_with(shot):
                    log_event("asteroid_shot")
                    asteroid.split()
                    pygame.sprite.Sprite.kill(shot)

        screen.fill("black")
        for item in drawable:
            item.draw(screen)
        pygame.display.flip()
        dt=Clock.tick(60) /1000


    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print("Screen width: 1280, Screen height: 720")
    

if __name__ == "__main__":
    main()
