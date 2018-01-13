"""
 This example shows having multiple planets bouncing around the screen at the
 same time. You can hit the space bar to spawn more planets.
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
"""

import pygame
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
 
SCREEN_WIDTH = 1500
SCREEN_HEIGHT = 800
planet_SIZE = 25
G_CONST=6.67408*10**-11

print (G_CONST)
 
class Planet:
    """
    Class to keep track of a planet's location and vector.
    """
    def __init__(self):
        self.x = 0.0
        self.y = 0.0
        self.change_x = 0.0
        self.change_y = 0.0
        self.radius=0
        self.mass=0
 
def make_Planet():
    """
    Function to make a new, random planet.
    """
    planet = Planet()
    # Starting position of the planet. 
    planet.radius=random.randrange(20,100)
    # Take into account the planet size so we don't spawn on the edge.
    planet.x = random.randrange(planet.radius, SCREEN_WIDTH - planet.radius)
    planet.y = random.randrange(planet.radius, SCREEN_HEIGHT -planet.radius)
   
    # Speed and direction of rectangle
    planet.change_x = random.randrange(-5.0, 5.0)
    planet.change_y = random.randrange(-5.0, 5.0)
 
    return planet
 
def calcPos(planet):
    
    return (200,200)
def main():
    """
    This is our main program.
    """
    pygame.init()
 
    # Set the height and width of the screen
    size = [SCREEN_WIDTH, SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)
 
    pygame.display.set_caption("Bouncing planets")
 
    # Loop until the user clicks the close button.
    done = False
 
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
 
    planet_list = []
 
    planet = make_planet()
    planet_list.append(planet)
 
    # -------- Main Program Loop -----------
    while not done:
        # --- Event Processing
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                # Space bar! Spawn a new planet.
                if event.key == pygame.K_SPACE:
                    planet = make_planet()
                    planet_list.append(planet)
 
        # --- Logic
        for planet in planet_list:
            # Move the planet's center
            xy=calcPos(planet)
            planet.x =xy[0]
            planet.y =xy[1]
            #planet.change_x+=0.1;
          
 
            # Bounce the planet if needed
            if planet.y > SCREEN_HEIGHT - planet.radius or planet.y < planet.radius:
                planet.change_y *= -1.0
            if planet.x > SCREEN_WIDTH - planet.radius or planet.x < planet.radius:
                planet.change_x *= -1.0
 
        # --- Drawing
        # Set the screen background
        screen.fill(BLACK)
 
        # Draw the planets
        for planet in planet_list:
            pygame.draw.circle(screen, WHITE, [int(planet.x), int(planet.y)], planet.radius)
 
        # --- Wrap-up
        # Limit to 60 frames per second
        clock.tick(60)
 
        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
 
    # Close everything down
    pygame.quit()
 
if __name__ == "__main__":
    main()
