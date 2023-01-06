# Importing pygame
import pygame

# Initalizing pygame
pygame.init()

# This is how to initalize a pygame window.
# pygame.dispaly.set_mode((widith_of_window, height_of_window))
display = pygame.display.set_mode((750, 900))
pygame.display.set_caption("Tetris")

color = "red"

# Bool value which checks if game is running
running = True

events = pygame.event.get()
# Keep game running while running is true
while running:

	# Check for event if user has pushed any event in queue
	for event in events:

		# If event is of type quit then set running bool to false
		if event.type == pygame.QUIT:
			running = False
	# set background color to our display
	display.fill(color)
	# update display
	pygame.display.flip()
	# if color is red change to green and vice versa.
	#if(color == "red"):
		#color = "green"
	#else:
		#color = "red"