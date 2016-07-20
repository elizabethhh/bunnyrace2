"""
 Pygame base template for opening a window

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

 Explanation video: http://youtu.be/vRB_983kUMc
"""

import pygame
import random
import time

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREY = (127, 127, 127)

pygame.init()

# Set the width and height of the screen [width, height]
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Bunny Race")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()


possible_ball_colors = [BLACK, WHITE, GREEN, RED, BLUE, GREY]

rand_x_speed1 = random.randint(2,20)
rand_x_speed2 = random.randint(2,20)
rand_x_speed3 = random.randint(2,20)
rand_x_speed4 = random.randint(2,20)
rand_x_speed5 = random.randint(2,20)
rand_x_speed6 = random.randint(2,20)
rand_x_speed7 = random.randint(2,20)



# BOUNCING BALL CLASS CODE  

class Bunny(): 

    # CONSTRUCTOR METHOD 
    def __init__(self, x_location, y_location, x_speed, ball_size):  
    # Attributes of the circle 
        self.x_location = x_location
        self.y_location = y_location  
        self.x_speed = x_speed 
        self.ball_size = ball_size 

    # GAME METHODS  
    bet = input("Which bunny do you think will win? Choose a bunny from numbers 1-7. ")
    
    def race(self, screen, colors, screen_width, screen_height):

        ball_color = random.choice(colors)
        if self.x_location >= screen_width - self.ball_size or self.x_location < self.ball_size:
            self.x_speed = self.x_speed * 0
            
        self.x_location += self.x_speed 

        pygame.draw.circle(screen, ball_color, [self.x_location, self.y_location], self.ball_size)

    


# -------- Main Program Loop -----------
bunny = Bunny(30,100,rand_x_speed1,30)
bunny2 = Bunny(30,200,rand_x_speed2,30)
bunny3 = Bunny(30,300,rand_x_speed3,30)
bunny4 = Bunny(30,400,rand_x_speed4,30)
bunny5 = Bunny(30,500,rand_x_speed5,30)
bunny6 = Bunny(30,600,rand_x_speed6,30)
bunny7 = Bunny(30,700,rand_x_speed7,30)
time.sleep(5)
print("Congratulations! You guessed the right number! That bunny number was the fastest.")
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Game logic should go here
    screen.fill(BLACK)

    bunny.race(screen,possible_ball_colors,SCREEN_WIDTH,SCREEN_HEIGHT)
    bunny2.race(screen,possible_ball_colors,SCREEN_WIDTH,SCREEN_HEIGHT)
    bunny3.race(screen,possible_ball_colors,SCREEN_WIDTH,SCREEN_HEIGHT)
    bunny4.race(screen,possible_ball_colors,SCREEN_WIDTH,SCREEN_HEIGHT)
    bunny5.race(screen,possible_ball_colors,SCREEN_WIDTH,SCREEN_HEIGHT)
    bunny6.race(screen,possible_ball_colors,SCREEN_WIDTH,SCREEN_HEIGHT)
    bunny7.race(screen,possible_ball_colors,SCREEN_WIDTH,SCREEN_HEIGHT)


    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.

    
    # --- Drawing code should go here

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
exit() # Needed when using IDLE


