'''
Block captions

'''

import pygame, sys
from pygame.locals import *
from gameclock import *

pygame.init()

FPS = 0 # 0 = Unlimited
COLOR_BLACK = (0, 0, 0)


def main():
  # Set up the window
  displaysurf = pygame.display.set_mode((1280, 720), pygame.DOUBLEBUF)
  pygame.display.set_caption("First App")
  clock = GameClock(60, FPS) # Updates per second, frames per second
  
  # Image example
  w_img = pygame.image.load("images/warrior.png")
  w_x = 0
  w_y = 0
  
  # Font example
  font_freesansbold = pygame.font.Font("freesansbold.ttf", 32)
  get_rect = font_freesansbold.render("get_rect(\"m8\")", True, (0, 255, 0)) # Next parameter is background color, left off = transparent
  get_rect_rect = get_rect.get_rect()
  get_rect_rect.topleft = (100, 200)
  
  running = True
  
  while running: # Main game loop
    clock.tick()
    if clock.update_ready:
      w_x = (w_x + 4) % 400
      w_y = (w_y + 4) % 400
    if clock.frame_ready:
      displaysurf.fill(COLOR_BLACK) # Clears the old draws
      displaysurf.blit(w_img, (w_x, w_y))
      displaysurf.blit(get_rect, get_rect_rect)
    
    for event in pygame.event.get():
      if event.type == QUIT:
        running = False
    
    pygame.display.update()
    # End of main()

main()
pygame.quit()

