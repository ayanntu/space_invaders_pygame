import pygame
import sys
from bullet import Bullet
from alien import Alien

def events(screen, gun, bullets):
    """event processing"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            #right
            if event.key == pygame.K_d:
                gun.mright = True
            if event.key == pygame.K_a:
                gun.mleft = True
        elif event.type == pygame.KEYUP:
            #right
            if event.key == pygame.K_d:
                gun.mright = False
            if event.key == pygame.K_d:
                gun.mleft = False
            elif event.key == pygame.K_SPACE:
                new_bullet = Bullet(screen, gun)
                bullets.add(new_bullet)

def update(bg_color, screen, gun, bullets, aliens):  # Add 'alien' as an argument
    """update display"""
    screen.fill(bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    gun.output()
    aliens.draw(screen)  # Call the 'draw()' method of the 'alien' object without any arguments
    pygame.display.flip()



def update_bullets(aliens, bullets):
    "обновлять позиции пуль"
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)


def update_aliens(aliens):
    """обновляют позицию пришельцев"""
    aliens.update()


def create_army(screen, aliens):
    """создание армии пришельцев"""
    alien = Alien(screen)
    alien_width = alien.rect.width
    number_alien_x = int((700 - 2 * alien_width) / alien_width)
    alien_height = alien.rect.height
    number_alien_y = int((800 - 100 - 2 * alien_height) / alien_height)

    for row_number in range(number_alien_y - 1):
        for alien_number in range(number_alien_x):
            alien = Alien(screen)
            alien.x = alien_width + (alien_width * alien_number)
            alien.y = alien_height + (alien_height * row_number)
            alien.rect.x = alien.x
            alien.rect.y = alien.y
            aliens.add(alien)








