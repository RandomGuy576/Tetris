import pygame

pygame.init()

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

clock = pygame.time.Clock()
fps = 60

font = pygame.font.SysFont('Arial', 40)

objects = []

width, height = 750, 950

screen = pygame.display.set_mode((width, height))

class button():
    def __init__(self, x, y, width, height, buttonText='Button', onclickFunction=None, onePress=False):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.onclickFunction = onclickFunction
        self.onePress = onePress
        self.alreadyPressed = False

        self.fillColors = {
            'normal': '#ffffff',
            'hover': '#666666',
            'pressed': '#333333',
        }

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