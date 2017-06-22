import sys, pygame
 
BLACK = 0, 0, 0
WHITE = 255, 255, 255
 
pygame.init()
screen = pygame.display.set_mode((640,480))
pygame.display.set_caption("Moving Box")
 
box_x = 300
box_dir = 10

while True:
 
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      sys.exit()

  if box_x >= 620:
    box_dir = -10
  if box_x <= 20:
    box_dir = 10

  box_x = box_x + box_dir

  screen.fill(BLACK)
  pygame.draw.rect(screen, WHITE, (box_x, 200, 20, 20))
  pygame.display.update()

pygame.quit()