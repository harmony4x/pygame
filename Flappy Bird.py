import pygame 
from random import randint

pygame.init()
WIDTH , HEIGHT = 400 , 600
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Flappy Bird')


running = True
GREEN = (0,255,0)
BLUE = (0,0,255)
BLACK = (0,0,0)
WHITE = (255,255,255)
GREY = (155,155,155)
RED = (255,0,0)
YELLO = (255,255,0)

clock = pygame.time.Clock()
font = pygame.font.SysFont('sans', 20)

TUBE_WIDTH = 50
TUBE_VELOCITY = 3
TUBE_GAP = 150

tube1_x = 600
tube2_x = 800
tube3_x = 1000

tube1_height = randint(100,300)
tube2_height = randint(100,300)
tube3_height = randint(100,300)

BIRD_X = 50
bird_y = 400

bird_drop_velocity = 2
GRAVITY = 0.5

tube1_pass = False
tube2_pass = False
tube3_pass = False
score = 0

pauseing = False
background_image = pygame.image.load("background.png")
background_image = pygame.transform.scale(background_image, (WIDTH,HEIGHT))
bird_image = pygame.image.load("bird.png")

while running:
	clock.tick(60)
	screen.fill(GREY)
	screen.blit(background_image, (0,0))
	# Draw tube
	tube1_rect = pygame.draw.rect(screen, BLUE, (tube1_x, 0, TUBE_WIDTH,tube1_height))

	tube2_rect = pygame.draw.rect(screen, BLUE, (tube2_x, 0, TUBE_WIDTH,tube2_height))

	tube3_rect = pygame.draw.rect(screen, BLUE, (tube3_x, 0, TUBE_WIDTH,tube3_height))

	# Draw tube inverse
	tube1_rect_inv = pygame.draw.rect(screen, BLUE, (tube1_x, tube1_height + TUBE_GAP, TUBE_WIDTH ,(HEIGHT - tube1_height - TUBE_GAP)))

	tube2_rect_inv = pygame.draw.rect(screen, BLUE, (tube2_x, tube2_height + TUBE_GAP, TUBE_WIDTH ,(HEIGHT - tube2_height - TUBE_GAP)))

	tube3_rect_inv = pygame.draw.rect(screen, BLUE, (tube3_x, tube3_height + TUBE_GAP, TUBE_WIDTH ,(HEIGHT - tube3_height - TUBE_GAP)))

	# Draw sand 
	sand_rect = pygame.draw.rect(screen, YELLO, (0, 550, 400, 50))

	# move tube
	tube1_x -= TUBE_VELOCITY
	tube2_x -= TUBE_VELOCITY
	tube3_x -= TUBE_VELOCITY

	# draw bird 
	# bird_rect = pygame.draw.rect(screen, RED, (BIRD_X, bird_y, 35,35))
	bird_rect = screen.blit(bird_image, (BIRD_X,bird_y))

	#bird falls
	bird_y += bird_drop_velocity
	bird_drop_velocity += GRAVITY

	#new tube
	if tube1_x < -50:
		tube1_x = 550
		tube1_height = randint(100,400)
		tube1_pass = False
	if tube2_x < -50:
		tube2_x = 550
		tube2_height = randint(100,400)
		tube2_pass = False
	if tube3_x < -50:
		tube3_x = 550
		tube3_height = randint(100,400)
		tube3_pass = False


	# match score

	if tube1_x + TUBE_WIDTH <= BIRD_X and tube1_pass == False:
		score += 1
		tube1_pass = True
	if tube2_x + TUBE_WIDTH <= BIRD_X and tube2_pass == False:
		score += 1
		tube2_pass = True
	if tube3_x + TUBE_WIDTH <= BIRD_X and tube3_pass == False:
		score += 1
		tube3_pass = True

	#check collistion 
	for tube in [tube1_rect, tube2_rect, tube3_rect, tube1_rect_inv, tube2_rect_inv, tube3_rect_inv, sand_rect]:
		if bird_rect.colliderect(tube): #colliderect ham check 2 hinh chu nhat khi va cham
			TUBE_VELOCITY = 0
			bird_drop_velocity = 0
			score_txt = font.render("Score: " +str(score), True, BLACK)
			screen.blit(score_txt,(150,300))
			pygame.display.flip()
			pauseing = True
	if bird_y<=0 :
		TUBE_VELOCITY = 0
		bird_drop_velocity = 0
		score_txt = font.render("Score: " +str(score), True, BLACK)
		screen.blit(score_txt,(150,300))
		pygame.display.flip()
		pauseing = True

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				#test pause
				if pauseing:
					TUBE_VELOCITY = 3
					bird_y = 400
					tube1_x = 600
					tube2_x = 800
					tube3_x = 1000
					score = 0
					pauseing = False

				bird_drop_velocity = 0
				bird_drop_velocity -= 10


	score_txt = font.render("Score: " +str(score), True, BLACK)
	screen.blit(score_txt,(5,5))
	pygame.display.flip()

pygame.quit()