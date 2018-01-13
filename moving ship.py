import sys, pygame, math

SCREEN_WIDTH = 1300
SCREEN_HEIGHT = 700
BLACK = (0, 0, 0)
class Ship:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.velocityX = 0.0
        self.velocityY = 0.0
        self.velocityTotal = 0.0
        self.angleFromNormal = 0.0

def calcVel(x,y):
    return math.sqrt(x**2+y**2)
def main():
    pygame.init()
    size = [SCREEN_WIDTH, SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("Moving Ship")
    done = False
    clock = pygame.time.Clock()
    ship = Ship()
    ship.x = 10
    ship.y = 10
    ship = Ship()
    shipS = pygame.transform.scale(pygame.image.load("C:\\Users\Sorrin\Desktop\ship.png"), (20, 20))
    tempShip = shipS
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    #ship.velocityTotal = calcVel(ship.velocityX,ship.velocityY)+5
                    #ship.velocityTotal = ship.velocityY * math.sin(math.pi/4)/math.sin(math.pi/4 - ship.angleFromNormal)
                    ship.velocityTotal +=1
                    ship.velocityX = ship.velocityTotal * math.cos(ship.angleFromNormal)
                    ship.velocityY = ship.velocityTotal * math.sin(ship.angleFromNormal)
                    print("Vel total: ", ship.velocityTotal)
                    print("Velocity x: ", ship.velocityX)
                    print("Velocity y: ", ship.velocityY)
                    print("coordinates:", ship.x, ship.y)
#                    ship.velocityY -= 1
                if event.key == pygame.K_LEFT:
                    ship.angleFromNormal-= math.pi/12
                    tempShip = pygame.transform.rotozoom(shipS,ship.angleFromNormal,1)
                    print("Angle from normal: ", ship.angleFromNormal)
#                    ship.velocityX -=1
                if event.key == pygame.K_RIGHT:
                    ship.angleFromNormal+= math.pi/12
                    print("Angle from normal: ", ship.angleFromNormal)
                    tempShip = pygame.transform.rotozoom(shipS,ship.angleFromNormal,1)
#                    ship.velocityX +=1
                if event.key == pygame.K_DOWN:
                    #ship.velocityTotal = calcVel(ship.velocityX,ship.velocityY)-5
                    ship.velocityTotal -=1
                    ship.velocityX = ship.velocityTotal * math.cos(ship.angleFromNormal)
                    ship.velocityY = ship.velocityTotal * math.sin(ship.angleFromNormal)
                    print("Vel total: ", ship.velocityTotal)
                    print("Velocity x: ", ship.velocityX)
                    print("Velocity y: ", ship.velocityY)
#                    ship.velocityY +=1
        clock.tick(60)
        screen.fill(BLACK)
        ship.x+=ship.velocityX
        ship.y+=ship.velocityY
        tempShip = pygame.transform.rotozoom(shipS, ship.angleFromNormal, 1)
        screen.blit(tempShip,(ship.x,ship.y))
        pygame.display.flip()
    pygame.quit()
if __name__ == "__main__":
    main()


