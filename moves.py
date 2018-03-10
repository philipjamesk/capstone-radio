
##########
# Create a class for logo with rect, scale, image, etc.
#
# Make an array of logos and pass that around...
#########



import pygame
import sys

from logo import Logo


logos = []

###
#   pngs array is a place holder that will be replaced with stations list
###

pngs = ['../Capstone/img/logos/eclectic24_logo.png',
         '../Capstone/img/logos/triplej_logo.png',
         '../Capstone/img/logos/wumb_logo.png',
         '../Capstone/img/logos/tsfjazz_logo.png',
         '../Capstone/img/logos/doublej_logo.png']

def main_loop():
    # Put all the initial settings here
    pygame.init()
    screen = pygame.display.set_mode((320,240))
    screen_rect = screen.get_rect()
    bg_color = (232, 222, 199)
    screen.fill(bg_color)
    logos = make_logos(screen)
    logos = place_logos(logos, screen)

    while True:
        # This is where pygame will listen for keypresses, update the logos
        # and flip the screen
        # draw_logos(logos, screen)
        check_events(logos, screen)
        draw_screen(screen, screen_rect)
        pygame.display.flip()

def check_events(logos, screen):
    # Determine is a key event is a left or right arrow and pass it to the
    # correct movement function
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                move_right(logos, screen)
            if event.key == pygame.K_LEFT:
                move_left(logos, screen)

def move_right(logos, screen):
    for logo in logos:
        logo.changex(10)

def move_left(logos, screen):
    for logo in logos:
        logo.changex(-10)

def draw_logos(logos, screen):
    for logo in logos:
        logo_rect = logo.get_rect()
        screen.blit(logo, logo_rect)



def place_logos(logos, screen):
    ###
    #   Will need to figure out currently playing station and adjust
    #   this is it only places the necessary logos
    ###
    screen_rect = screen.get_rect()
    x = 0
    for logo in logos:
        logo.changex(x)
        x += 100
    return logos


def draw_screen(screen, screen_rect):
    bg_color = (232, 222, 199)
    screen.fill(bg_color)
    #
    # Add the rest to the display
    dial_marks = pygame.image.load('../Capstone/img/display/radio-marks.png')
    red_line = pygame.image.load('../Capstone/img/display/red-line.png')

    dial_marks_rect = dial_marks.get_rect()
    red_line_rect = red_line.get_rect()

    dial_marks_rect.centerx = screen_rect.centerx
    dial_marks_rect.centery = screen_rect.centery
    red_line_rect.centerx = screen_rect.centerx
    red_line_rect.centery = screen_rect.centery

    for logo in logos:
        logo.blitme()

    screen.blit(dial_marks, dial_marks_rect)
    screen.blit(red_line, red_line_rect)

def make_logos(screen):
    # Put the five logos and their rects in an array
    for image in pngs:
        logo = Logo(screen, image)
        logos.append(logo)
    return logos

# run the main loop
main_loop()
