import pygame
import random

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

class Block(pygame.sprite.Sprite):
	def __init__(self, width, height, colour):
		super().__init__()
		self.image = pygame.Surface([width, height])
		self.image.fill(colour)
		self.rect = self.image.get_rect()
	def update(self):
		self.rect.y += 1
		if self.rect.y > screen_height:
			self.rect.y = 0


pygame.init()
screen_width = 700
screen_height = 400
screen = pygame.display.set_mode([screen_width, screen_height])
clock = pygame.time.Clock()
score = 0

block_list = pygame.sprite.Group()
all_sprites_list = pygame.sprite.Group()

for i in range(50):
	block = Block(20, 15, BLACK)
	block.rect.x = random.randrange(screen_width)
	block.rect.y = random.randrange(screen_height)
	block_list.add(block)
	all_sprites_list.add(block)

player = Block(20, 20, RED)
all_sprites_list.add(player)
player.rect.y = 350


font = pygame.font.SysFont('Arial', 24, bold=True)    

playing = True
while playing:
	clock.tick(60)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			playing = False
	
	keys = pygame.key.get_pressed()
	if keys[pygame.K_LEFT] and player.rect.x > 0:
			player.rect.x -= 10
	if keys[pygame.K_RIGHT] and player.rect.x < screen_width - player.rect.width :
			player.rect.x += 10
	
	block_list.update()

	screen.fill(WHITE)

	# pos = pygame.mouse.get_pos()
	# player.rect.x = pos[0]

	blocks_hit_list = pygame.sprite.spritecollide(player, block_list, True)
	if blocks_hit_list:
		score += len(blocks_hit_list)
		print(score)
	text = font.render(str(score), True, WHITE, BLACK)
	screen.blit(text, (10,10))

	all_sprites_list.draw(screen)

	if score > 10:
		img=pygame.image.load("images/background.jpg")
		screen.blit(img,(0,0))

	pygame.display.update()

pygame.quit()