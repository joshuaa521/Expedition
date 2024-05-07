import pygame
import time
import random


# set up pygame modules
pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Arial', 15)
large_font = pygame.font.SysFont('Arial', 30)
med_font = pygame.font.SysFont('Arial', 20)
pygame.display.set_caption("Expedition!")


# set up variables for the display
SCREEN_HEIGHT = 370
SCREEN_WIDTH = 530
size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)


title1 = "Welcome to Expedition!"
title5 = "Click to start!"
controls = "Hold C for Controls Screen!"
restart = "Press space to restart!"
controls2 = "Controls added later"

name = "Collect coins as fast as you can!"
message = "Collision not detected"
win_message = "Congratulations! You Win!"
loss_message = "You lost! Try Again!"
r = 50
g = 0
b = 100
score = 0


# render the text for later
display_name = my_font.render(name, True, (255, 255, 255))
display_message = my_font.render(message, True, (255, 255, 255))
score_display = my_font.render("Score: " + str(score), True, (255, 255, 255))
loss_display = large_font.render(loss_message, True, (255,255,255))
win_display = large_font.render(win_message, True, (255,255,255))
title1_display = large_font.render(title1, True, (255,255,255))
title5_display = large_font.render(title5, True, (255,255,255))
restart_display = large_font.render(restart, True, (255,255,255))
controls_display = large_font.render(controls,True, (255,255,255))
controls2_display = large_font.render(controls2, True, (255,255,255))


win = False
lose = False
title = True
control_screen = False
# The loop will carry on until the user exits the game (e.g. clicks the close button).
run = True
end_time = time.time() + 20
current_time = time.time()
# -------- Main Program Loop -----------
while run:
 current_time = end_time - time.time()
 current_time = round(current_time, 2)


 if current_time < 0:
     lose = True


 keys = pygame.key.get_pressed()  # checking key pressed

 if keys[pygame.K_SPACE]:
     if win is True:
         score = 0
         win = False
         end_time = time.time() + 20
         current_time = time.time()
         score_display = my_font.render("Score: " + str(score), True, (255, 255, 255))


     elif lose is True:
         score = 0
         lose = False
         end_time = time.time() + 20
         current_time = time.time()
         score_display = my_font.render("Score: " + str(score), True, (255, 255, 255))





 else:
     message = "Collision not detected"
     display_message = my_font.render(message, True, (255, 255, 255))


 # --- Main event loop
 for event in pygame.event.get():  # User did something
     if event.type == pygame.QUIT:  # If user clicked close
         run = False




 if win is True:
     screen.fill((r, g, b))
     screen.blit(win_display, (90,125))
     screen.blit(restart_display, (125, 170))
     pygame.display.update()


 if lose is True:
     screen.fill((r, g, b))
     screen.blit(loss_display, (125, 125))
     screen.blit(restart_display, (125,170))
     pygame.display.update()


 if title is True:
     if keys[pygame.K_c]:
         screen.fill((r, g, b))
         screen.blit(controls2_display, (125, 10))
         screen.blit(title5_display, (150, 200))
         pygame.display.update()
     elif event.type == pygame.MOUSEBUTTONUP:
         screen.fill((r, g, b))
         pygame.display.update()
     else:
        screen.fill((r, g, b))
        screen.blit(title1_display, (125, 10))
        screen.blit(title5_display, (150, 200))
        screen.blit(controls_display, (100,100))
        pygame.display.update()




#event.type == pygame.MOUSEBUTTONUP:



# Once we have exited the main program loop we can stop the game engine:
pygame.quit()

