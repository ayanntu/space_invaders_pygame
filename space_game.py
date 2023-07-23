import pygame
import sys
import controls  # Add the import statement for the 'controls' module
from gun import Gun
from alien import Alien
from pygame.sprite import Group


# Import statements and class definitions go here (unchanged)

def run():
    pygame.init()
    screen = pygame.display.set_mode((700, 750))
    pygame.display.set_caption("Cosmic defenders")
    bg_color = (0, 0, 0)
    gun = Gun(screen)
    bullets = Group()
    alien = Alien(screen)
    aliens = Group()
    controls.create_army(screen, aliens)

    clock = pygame.time.Clock()  # Create a Clock object for frame rate control

    while True:
        clock.tick(60)  # Limit the frame rate to 60 FPS

        controls.events(screen, gun, bullets)
        gun.update_gun()
        bullets.update()
        controls.update(bg_color, screen, gun, bullets, aliens)
        controls.update_bullets(aliens, bullets)
        controls.create_army(screen, aliens)
        controls.update_aliens(aliens)

run()



