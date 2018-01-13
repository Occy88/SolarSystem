import pygame


class Planet(object):
    def __init__(self, RADIUS, MASS, location, velocity):
        self.RADIUS=RADIUS
        self.MASS=MASS
        self.location=location
        self.velocity=velocity

    def __repr__(self):
        return "Ball at "+str(self.location)

p=Planet(5, 10, (3,5), (1, 1))
p.location=(10, 10)
print(p)

print(p.RADIUS)

def updateScreen(planets, screen):
    screen.fill((255,255,255))
    for p in planets:
        pygame.draw.circle(screen, (0,0,0), p.location, p.RADIUS, 1)
        
    pygame.display.flip()




def main():


    
    # create a window
    pygame.init()
    screen = pygame.display.set_mode((500, 500))
    pygame.display.set_caption('Basic Pygame program')
##    # Fill background
##    background = pygame.Surface(screen.get_size())
##    background = background.convert()
##    background.fill((250, 250, 250))

    planets=[Planet(5+5*i, 1, (10*i, 100), (1,1)) for i in range(5)]

    updateScreen(planets, screen)
    

    
main()
