import pygame
import time
from fox import Fox
from bullet import Bullet
from monster import Monster
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
title2 = "Your goal is to defeat the monster!"
title3 = "Use your gun to take it down!"
title4 = "Hold C for Controls Screen!"
title5 = "Click to start!"
restart = "Press space to restart!"
controls2 = "Expedition Controls"
controls = "Hold C for Controls Screen!"

controls3 = "Hold B while moving as monster for a speed boost"
controls4 = "Tap F to shoot"
controls5 = "WASD for scientist Movement"
controls6 = "Arrow Keys for monster movement"

message = "Defeat the Monster!"
message_2 = "Collision not detected"
win_message = "Congratulations! You Win!"
loss_message = "You lost! Try Again!"

r = 93
g = 93
b = 93
score = 0

# render the text for later
display_message = my_font.render(message, True, (255, 255, 255))
display_message_2 = my_font.render(message_2, True, (255, 255, 255))
score_display = my_font.render("Score: " + str(score), True, (255, 255, 255))
loss_display = large_font.render(loss_message, True, (255,255,255))
win_display = large_font.render(win_message, True, (255,255,255))
title1_display = large_font.render(title1, True, (255,255,255))
title2_display = med_font.render(title2, True, (255,255,255))
title3_display = med_font.render(title3, True, (255,255,255))
title4_display = med_font.render(title4, True, (255,255,255))
title5_display = large_font.render(title5, True, (255,255,255))
restart_display = large_font.render(restart, True, (255,255,255))
controls_display = large_font.render(controls,True, (255,255,255))
controls2_display = large_font.render(controls2, True, (255,255,255))
controls3_display = large_font.render(controls3, True, (255,255,255))
controls4_display = large_font.render(controls4, True, (255,255,255))
controls5_display = large_font.render(controls5, True, (255,255,255))
controls6_display = large_font.render(controls6, True, (255,255,255))

#health_display = large_font.render(monster_health, True, (255,255,255))

f = Fox(40, 60)
s = Bullet(40,60)
m = Monster(400,60)


win = False
lose = False
title = True
shoot_bullet = False

# The loop will carry on until the user exits the game (e.g. clicks the close button).
run = True
start_time = time.time()
monster_healthnumber = 600
scientist_healthnumber = 200
# -------- Main Program Loop -----------
while run:
 current_time = time.time() - start_time
 current_time = round(current_time, 2)

 healthx, healthy = m.give_location()

 healthx = healthx + 10
 healthy = healthy - 10

 science_x, science_y = f.give_location()
 science_x = science_x + 10
 science_y = science_y - 10


 x, y = f.give_location()
 if shoot_bullet == False:
     s.find_player(x, y)

 if shoot_bullet == True:
     s.shoot_move()


 x,y = s.give_location()

 if x > 500:
     shoot_bullet = False

 if current_time < 0:
     lose = True

 if m.rect.colliderect(s.rect) and m.rect.colliderect(f.rect):
     message_2 = "Collision detected"
     display_message_2 = my_font.render(message_2, True, (255, 255, 255))
     score_display = my_font.render("Score: " + str(score), True, (255, 255, 255))
     scientist_healthnumber = scientist_healthnumber - 50
     m = Monster(400, 60)
     shoot_bullet = False
 elif m.rect.colliderect(s.rect):
     monster_healthnumber = monster_healthnumber - 20
     shoot_bullet = False



 keys = pygame.key.get_pressed()  # checking pressed keys
 if keys[pygame.K_b]:
     if keys[pygame.K_UP]:
         m.speed_move("up")
     if keys[pygame.K_LEFT]:
         m.speed_move("left")
     if keys[pygame.K_RIGHT]:
         m.speed_move("right")
     if keys[pygame.K_DOWN]:
         m.speed_move("down")
 else:
     if keys[pygame.K_UP]:
         m.move_direction("up")
     if keys[pygame.K_LEFT]:
         m.move_direction("left")
     if keys[pygame.K_RIGHT]:
         m.move_direction("right")
     if keys[pygame.K_DOWN]:
         m.move_direction("down")


 if keys[pygame.K_d]:
     f.move_direction("right")
 if keys[pygame.K_a]:
     f.move_direction("left")
 if keys[pygame.K_w]:
     f.move_direction("up")
 if keys[pygame.K_s]:
     f.move_direction("down")
 if keys[pygame.K_f]:
     shoot_bullet = s.shoot(shoot_bullet)

 if monster_healthnumber == 0:
     win = True

 if scientist_healthnumber == 0:
     lose = True


 if keys[pygame.K_SPACE]:
     if win is True:
         score = 0
         monster_healthnumber = 600
         scientist_healthnumber = 200

         f = Fox(40, 60)
         s = Bullet(40, 60)
         m = Monster(400, 60)

         win = False
         end_time = time.time() + 20
         current_time = time.time()
         score_display = my_font.render("Score: " + str(score), True, (255, 255, 255))


     elif lose is True:
         score = 0
         monster_healthnumber = 600
         scientist_healthnumber = 200

         f = Fox(40, 60)
         s = Bullet(40, 60)
         m = Monster(400, 60)

         lose = False
         end_time = time.time() + 20
         current_time = time.time()
         score_display = my_font.render("Score: " + str(score), True, (255, 255, 255))



 # --- Main event loop
 for event in pygame.event.get():  # User did something
     if event.type == pygame.QUIT:  # If user clicked close
         run = False


     if event.type == pygame.MOUSEBUTTONUP:
         if event.button == 1:
             if title is True:
                 end_time = time.time() + 20
                 current_time = time.time()
                 score = 0
                 title = False
                 score_display = my_font.render("Score: " + str(score), True, (255, 255, 255))



 if win is False and lose is False and title is False:
   screen.fill((r, g, b))
   screen.blit(display_message_2, (0, 0))
   screen.blit(display_message, (0, 15))
   screen.blit(m.image, m.rect)
   screen.blit(s.image, s.rect)
   screen.blit(f.image, f.rect)
   screen.blit(score_display, (0,30))

   monster_health = str(monster_healthnumber)
   monster_health = str(monster_health)
   health_display = large_font.render(monster_health, True, (255, 255, 255))

   screen.blit(health_display, (healthx,healthy))

   format_currenttime = (str(current_time) + "s elapsed")
   format_currenttime = str(format_currenttime)

   scientist_healthnumber = str(scientist_healthnumber)
   sciencehealth_display = large_font.render(scientist_healthnumber, True, (255,255,255))
   screen.blit(sciencehealth_display, (science_x, science_y))

   display_time = my_font.render(format_currenttime, True, (255, 255, 255))
   screen.blit(display_time, (0, 50))
   pygame.display.update()




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
         screen.blit(controls2_display, (125, 0))
         screen.blit(controls3_display, (25, 50))
         screen.blit(controls4_display, (125, 80))
         screen.blit(controls5_display, (125, 110))
         screen.blit(controls6_display, (125, 140))

         screen.blit(title5_display, (150, 200))
         pygame.display.update()
     else:
         screen.fill((r, g, b))
         screen.blit(title1_display, (100, 15))
         screen.blit(title2_display, (100, 85))
         screen.blit(title3_display, (100, 120))
         screen.blit(title4_display, (100, 150))
         screen.blit(title5_display, (150, 200))
         pygame.display.update()



# Once we have exited the main program loop we can stop the game engine:
pygame.quit()