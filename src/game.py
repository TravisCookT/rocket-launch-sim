import pygame
import math
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600


# Create screen
WIDTH, HEIGHT = 800, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

# Set window title
pygame.display.set_caption("Rocket Launch Simulator")

# Colors
YELLOW = (255, 255, 0)

class Rocket:
    GRAVITY = 9.8
    #SCALE ??
    TIMESTEP = 1 # 1 second


    def __init__(self, x, y, sides, color, mass):
        self.x = x
        self.y = y
        self.sides = sides
        self.mass = mass
        self.color = color
        # self.img = pygame.image.load('rocket.png')
        # self.width = self.img.get_width()
        # self.height = self.img.get_height()

        self.x_vel = 0
        self.y_vel = 0
    def draw(self, win):
        x = self.x * 1 + WIDTH/2
        y = self.y * 5 + HEIGHT/2
        pygame.draw.rect(win, self.color, pygame.Rect(390,748,20,50),2) # rocket FIX ME

def main():
    run = True
    clock = pygame.time.Clock()

    rocket = Rocket(0, 10, 10, YELLOW, 100)

    while run:
        clock.tick(60)
        # WIN.fill((255, 255, 255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        rocket.draw(WIN) # draw rocket
        pygame.display.update()
    pygame.quit()

if __name__ == "__main__":
    main()