# Import pygmae
import pygame

# Import pygame.locals for easier access to key cordiantes
# Updated to conform to flake8 and black standards.
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

# Initailize pygame
pygame.init()

screen = pygame.display.set_mode((800, 600))

# Varaiable to determine if the main loop should run.
running = True

# Main loop
while running:
    #Look at every event in the event queue
    for event in pygame.event.get():
        # Did the user press a key?
        if event.type == KEYDOWN:
            # Was the event the Escape key? if so, stop the loop.
            if event.key == K_ESCAPE:
                running = False
        # Did the user click the window close button? If so, stop the loop.
        elif event.type == QUIT:
            running = False
screen.fill((255, 255, 255))