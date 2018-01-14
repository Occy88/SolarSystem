"""
 This example shows having multiple planets bouncing around the screen at the
 same time. You can hit the space bar to spawn more planets.
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
"""
import scrapPlanetPositions as scrap
import pygame
import random
import math
from pygame.locals import *
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
 
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 750
planet_SIZE = 25

SPEED=60*60*24*12
G_CONST=6.67408*10**-11




 
def make_planet():
    """
    Function to make a new, random planet.
    """
    planet = Planet()
    # Starting position of the planet. 
    planet.radius=random.randrange(5,7)
    # Take into account the planet size so we don't spawn on the edge.
    planet.x = random.randrange(planet.radius, SCREEN_WIDTH - planet.radius)
    planet.y = random.randrange(planet.radius, SCREEN_HEIGHT -planet.radius)
   
 
    return planet
 
def calcVelVect(planetA, planetB):
    if planetA==planetB or planetA.x-planetB.x==0 or planetB.y-planetA.y==0:
        pass
    else:
        x=planetB.x-planetA.x
        y=planetB.y-planetA.y
        r2=((x**2)+(y**2))/2
        F=G_CONST*planetB.MASS/(r2*10**27)
       
        velX=(x/r2**0.5)*F
        
        velY=(y/r2**0.5)*F
        planetA.velocityX+=velX*(1/60)
        planetA.velocityY+=velY*(1/60)

def calcVelVectBullet(ship,planetB):
        if planetB.x-ship.x==0:
            pass
        else:
            x=planetB.x-ship.x
            y=planetB.y-ship.y
            r2=((x**2)+(y**2))/2
            F=G_CONST*planetB.MASS/(r2*10**27)
       
            velX=(x/r2**0.5)*F
        
            velY=(y/r2**0.5)*F
            ship.velocityX+=velX*(1/60)*1000000
            ship.velocityY+=velY*(1/60)*1000000
    

def calcVelVectShip(ship,planetB):
        if planetB.x-ship.x==0:
            pass
        else:
            x=planetB.x-ship.x
            y=planetB.y-ship.y
            r2=((x**2)+(y**2))/2
            F=G_CONST*planetB.MASS/(r2*10**27)
       
            velX=(x/r2**0.5)*F
        
            velY=(y/r2**0.5)*F
            ship.velocityX+=velX*(1/60)*10000
            ship.velocityY+=velY*(1/60)*10000
    

    


class Ship:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.MASS=10
        self.velocityX = 0.0
        self.velocityY = 0.0
        self.angleFromNormal = 0.0
        self.radius=10



def main():
    """
    This is our main program.
    """
    pygame.init()
 
    # Set the height and width of the screen
    size = [SCREEN_WIDTH, SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)    
    
    
    pygame.display.set_caption("Bouncing planets")

    while True:
        # Fill background
        background = pygame.Surface(screen.get_size())
        background = background.convert()
        background.fill((0,0,0))
        screen.blit(background, (0, 0))

        # Display image
        img_beginning = pygame.transform.scale(pygame.image.load("img/begin.jpg"), (1000, 600))
        screen.blit(img_beginning, (0,0))
        
        # Display some text
        font=pygame.font.Font(None,50)
        text=font.render("< Press space to see how to play >", 1,(255,255,255))
        textpos=text.get_rect()
        textpos.centerx=int(SCREEN_WIDTH/2)
        textpos.centery=635
        screen.blit(text,textpos)
        
        font=pygame.font.Font(None,60)
        text=font.render("<   T y p e   a n y   k e y   t o   s t a r t   >", 1,(255,255,255))
        textpos=text.get_rect()
        textpos.centerx=int(SCREEN_WIDTH/2)
        textpos.centery=700
        screen.blit(text,textpos)
        
        pygame.display.flip()
        
        done=False
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        done=1
                    else:
                        done=2
        if done==1:
            # Fill background
            background = pygame.Surface(screen.get_size())
            background = background.convert()
            background.fill((0,0,0))
            screen.blit(background, (0, 0))

            # Display image
            img_beginning = pygame.transform.scale(pygame.image.load("img/keyboardExpl.png"), (800, 400))
            screen.blit(img_beginning, (100, 100))
            
            # Display some text
            font=pygame.font.Font(None,25)
            text=font.render("The goal is to win ;)", 1,(255,255,255))
            textpos=text.get_rect()
            textpos.centerx=int(SCREEN_WIDTH/2)
            textpos.centery=550
            screen.blit(text,textpos)
            
            font=pygame.font.Font(None,45)
            text=font.render("<   T y p e   a n y   k e y   t o   g o   b a c k   t o   m e n u   >", 1,(255,255,255))
            textpos=text.get_rect()
            textpos.centerx=int(SCREEN_WIDTH/2)
            textpos.centery=700
            screen.blit(text,textpos)
            
            pygame.display.flip()
            
            done=False
            while not done:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                    elif event.type == pygame.KEYDOWN:
                        done=True

        
        else:
            
            # Loop
            done = False
         
            # Used to manage how fast the screen updates
            clock = pygame.time.Clock()
         
            planet_list = scrap.create_planet_list(False)
            for planet in planet_list:
                planet.image=pygame.transform.scale(pygame.image.load(planet.file), (int(planet.radius*4), int(planet.radius*4)))

                
            bullet_list =[]

            shipA=Ship()
            shipA.x=700
            shipA.y=700
            ship=Ship()
            ship.x=50
            ship.y=50
            
            shipS = pygame.transform.scale(pygame.image.load("img\ship.png"), (20, 20))
            shipS2 = pygame.transform.scale(pygame.image.load("img\ship2.png"), (20, 20))
            COUNTER_A=0
            COUNTER_B=0
            start=pygame.time.get_ticks()
            # -------- Main Program Loop -----------
            while not done:
                if int((pygame.time.get_ticks()-start)/1000)>=60:
                    done=True
               # x=ship.x+12
               # y=ship.y+12
               # radar = (ship.x,ship.y)
                #radar_len = 12
                #x = radar[0] + math.cos(ship.angleFromNormal) * radar_len
                #y = radar[1] + math.sin(ship.angleFromNormal) * radar_len
                # --- Event Processing
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_UP:
                            #ship.velocityTotal = calcVel(ship.velocityX,ship.velocityY)+5
                            #ship.velocityTotal = ship.velocityY * math.sin(math.pi/4)/math.sin(math.pi/4 - ship.angleFromNormal)
                         
                            ship.velocityX += 0.2 * math.cos(ship.angleFromNormal)
                            ship.velocityY += 0.2 * math.sin(ship.angleFromNormal)
                          
        #                    ship.velocityY -= 1
                        if event.key== pygame.K_r:
                            shipA.velocityX += 0.2 * math.cos(shipA.angleFromNormal)
                            shipA.velocityY += 0.2 * math.sin(shipA.angleFromNormal)


                        if event.key == pygame.K_LEFT:
                            ship.angleFromNormal-= math.pi/6
                            
        #                    ship.velocityX -=1
                        if event.key==pygame.K_d:
                            shipA.angleFromNormal-= math.pi/6

                            
                        if event.key == pygame.K_RIGHT:
                            ship.angleFromNormal+= math.pi/6

                        if event.key== pygame.K_g:
                            shipA.angleFromNormal+= math.pi/6 
                        
                        if event.key== pygame.K_DOWN   :
                            
                            #ship.velocityTotal = calcVel(ship.velocityX,ship.velocityY)-5
                            ship.velocityX -= 0.1 * math.cos(ship.angleFromNormal)
                            ship.velocityY -= 0.1 * math.sin(ship.angleFromNormal)

                        if event.key==pygame.K_f:
                            shipA.velocityX -= 0.1 * math.cos(shipA.angleFromNormal)
                            shipA.velocityY -= 0.1 * math.sin(shipA.angleFromNormal)

                            
                        if event.key== pygame.K_SPACE:
                            bullet=Ship()
                            bullet.x=ship.x+ship.radius*2*math.cos(ship.angleFromNormal)
                            bullet.y=ship.y+ship.radius*2*math.sin(ship.angleFromNormal)
                            bullet.velocityX=ship.velocityX*1.5
                            bullet.velocityY=ship.velocityY*1.5
                            bullet.velocityX += 5 * math.cos(ship.angleFromNormal)
                            bullet.velocityY += 5 * math.sin(ship.angleFromNormal)
                            bullet_list.append(bullet)                
                         
                        if event.key==pygame.K_q:
                            bullet=Ship()
                            bullet.x=shipA.x+shipA.radius*2*math.cos(shipA.angleFromNormal)
                            bullet.y=shipA.y+shipA.radius*2*math.sin(shipA.angleFromNormal)
                            bullet.velocityX=shipA.velocityX*1.5
                            bullet.velocityY=shipA.velocityY*1.5
                            bullet.velocityX += 5 * math.cos(shipA.angleFromNormal)
                            bullet.velocityY += 5 * math.sin(shipA.angleFromNormal)
                            bullet_list.append(bullet)                
                        
                           
                          
                  
                  
         
                # --- Logic
                for bullet in bullet_list:
                    if bullet.x<0 or bullet.x> SCREEN_WIDTH or bullet.y<0 or bullet.y>SCREEN_HEIGHT:
                        bullet_list.remove(bullet)
                        continue
                    else:
                        for planetA in planet_list:
                            if (((bullet.x-planetA.x)**2)+((bullet.y-planetA.y)**2))<planetA.radius**2:
                                bullet_list.remove(bullet)
                              
                                break
                            else:     
                             calcVelVectBullet(bullet,planetA)

                    bullet.x+=bullet.velocityX
                    bullet.y+=bullet.velocityY

                for planetA in planet_list:
                    for bullet in bullet_list:
                        if (((bullet.x-ship.x)**2)+((bullet.y-ship.y)**2))<ship.radius**2:
                            COUNTER_A+=1
                            bullet_list.remove(bullet)
                            if COUNTER_A%10==0:
                                ship.x=50
                                ship.y=50
                                ship.velocityX=0
                                ship.velocityY=0
                               
                            break
                        if (((bullet.x-shipA.x)**2)+((bullet.y-shipA.y)**2))<shipA.radius**2:
                            bullet_list.remove(bullet)
                            COUNTER_B+=1
                            if COUNTER_B%10==0:
                                shipA.x=700
                                shipA.y=700
                                shipA.velocityX=0
                                shipA.velocityY=0
                                
                            break
                        calcVelVectShip(ship,planetA)
                        calcVelVectShip(shipA,planetA)
                    
                for planetA in planet_list:
                    for planetB in planet_list:
                        calcVelVect(planetA,planetB)
                    # Move the planet's center
                    fps=clock.get_fps()
                    if fps<=40:
                        fps=60
                    planetA.x += planetA.velocityX*10000
                    planetA.y += planetA.velocityY*10000
                    
                    #planet.change_x+=0.1;
                if ship.x<0 or ship.x> SCREEN_WIDTH or ship.y<0 or ship.y>SCREEN_HEIGHT:
                     COUNTER_A+=1
                     ship.x=50
                     ship.y=50
                     ship.velocityX=0
                     ship.velocityY=0

                if shipA.x<0 or shipA.x> SCREEN_WIDTH or shipA.y<0 or shipA.y>SCREEN_HEIGHT:
                     COUNTER_B+=1
                     shipA.x=700
                     shipA.y=700
                     shipA.velocityX=0
                     shipA.velocityY=0
                     
                ship.x+=ship.velocityX
                ship.y+=ship.velocityY
                
                shipA.x+=shipA.velocityX
                shipA.y+=shipA.velocityY          
         
                    
                # --- Drawing
                # Set the screen background
                screen.fill(BLACK)
         
                # Draw the planets        
               # pygame.draw.line(screen,WHITE,(ship.x,ship.y),(x,y),2)
                tempShip2= pygame.transform.rotozoom(shipS2, -shipA.angleFromNormal*180/math.pi, 1)
                tempShip = pygame.transform.rotozoom(shipS, -ship.angleFromNormal*180/math.pi, 1)
                screen.blit(tempShip2,(shipA.x,shipA.y))
                screen.blit(tempShip,(ship.x,ship.y))
                
                font=pygame.font.Font(None,36)
                text=font.render(str(COUNTER_B)+"   -   "+str(int((pygame.time.get_ticks()-start)/1000))+"   -   "+str(COUNTER_A), 1,(255,255,255))
                textpos=text.get_rect()
                textpos.centerx=500
                screen.blit(text,textpos)
                
                for bullet in bullet_list: 
                    pygame.draw.line(screen,WHITE,(bullet.x,bullet.y),(bullet.x+3,bullet.y+3),4)
                for planet in planet_list:
                    screen.blit(planet.image, (int(planet.x), int(planet.y)))
                  
         
                # --- Wrap-up
                # Limit to 60 frames per second
                clock.tick(60)
         
                # Go ahead and update the screen with what we've drawn.
                pygame.display.flip()



            font=pygame.font.Font(None,70)
            text=font.render("Score player 'a-dfgr': "+str(COUNTER_A), 1,(255,255,255))
            textpos=text.get_rect()
            textpos.centerx=int(SCREEN_WIDTH/2)
            textpos.centery=int(SCREEN_HEIGHT*1/6)
            screen.blit(text,textpos)
            pygame.display.flip()

            font=pygame.font.Font(None,70)
            text=font.render("Score player 'space-arrows': "+str(COUNTER_B), 1,(255,255,255))
            textpos=text.get_rect()
            textpos.centerx=int(SCREEN_WIDTH/2)
            textpos.centery=int(SCREEN_HEIGHT*2/6)
            screen.blit(text,textpos)
            pygame.display.flip()
            
            
            
            done=False
            while not done:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            done=True

         
    # Close everything down
    pygame.quit()
     
if __name__ == "__main__":
    main()
