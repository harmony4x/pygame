import pygame
from time import sleep
from random import randint

pygame.init ()
screen = pygame.display.set_mode ((601, 601))
pygame.display.set_caption('Snake')
running = True
GREEN = (0,255,0)
GREY = (155,155,155)
BLACK = (0, 0 , 0)
WHITE = (255,255,255)
RED = (255,0,0)
BLUE = (0,0,255)
clock = pygame.time.Clock()

snakes = [[5,10]]
apple = [randint(0,19) , randint(0,19)]

direction = "Right"
score = 0
pauseing = False

font_small = pygame.font.SysFont('sans', 20)
font_big = pygame.font.SysFont('sans', 60)

while running:
	clock.tick(60)
	screen.fill(BLACK)

	tail_x = snakes[0][0]
	tail_y = snakes[0][1]

	#Draw grid
	# for i in range(21):
	# 	pygame.draw.line(screen, WHITE, (0, i*30), (600, i*30))
	# 	pygame.draw.line(screen, WHITE, (i*30, 0), (i*30, 600))

	#Draw apple
	apple_rect = pygame.draw.rect(screen,RED,(apple[0]*30,apple[1]*30, 30,30))


	#Draw snake
	for snake in snakes:
		snake_rect = pygame.draw.rect(screen,GREEN,(snake[0]*30,snake[1]*30, 30,30))

	# snake move
	if pauseing == False:
		if direction == "Right":
			snakes.append([snakes[-1][0]+1,snakes[-1][1]])
			snakes.pop(0)
		if direction == "Left":
			snakes.append([snakes[-1][0]-1,snakes[-1][1]])
			snakes.pop(0)
		if direction == "Up":
			snakes.append([snakes[-1][0],snakes[-1][1]-1])
			snakes.pop(0)
		if direction == "Down":
			snakes.append([snakes[-1][0],snakes[-1][1]+1])
			snakes.pop(0)

	#match score 
	if snakes[-1][0] == apple[0] and snakes[-1][1] == apple[1]:
		snakes.insert(0,[tail_x,tail_y])
		score += 1
		apple = [randint(0,19) , randint(0,19)]

	#check 4 canh 
	if snakes[-1][0] <0 or snakes[-1][0] > 19 or snakes[-1][1] < 0 or snakes[-1][1] > 19:
		score_txt = font_big.render("Game over, score: " +str(score), True, WHITE)
		message_txt = font_big.render("Press \"space\" to continue.", True, WHITE)
		screen.blit(score_txt, (100,200))
		screen.blit(message_txt, (20,300))
		apple = [-1,-1]
		pygame.display.flip()
		pauseing = True

	#check body
	for i in range(len(snakes)-1):
		if snakes[-1][0] == snakes[i][0] and snakes[-1][1] == snakes[i][1] and len(snakes)>1:
			score_txt = font_big.render("Game over, score: " +str(score), True, WHITE)
			message_txt = font_big.render("Press \"space\" to continue.", True, WHITE)
			screen.blit(score_txt, (100,200))
			screen.blit(message_txt, (20,300))
			apple = [-1,-1]
			pygame.display.flip()
			pauseing = True


	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP and direction != "Down":
				direction = "Up"
			if event.key == pygame.K_DOWN and direction != "Up":
				direction = "Down"
			if event.key == pygame.K_LEFT and direction != "Right":
				direction = "Left"
			if event.key == pygame.K_RIGHT and direction != "Left":
				direction = "Right"
			if event.key == pygame.K_SPACE and pauseing==True:
				if pauseing:
					pauseing = False
					snakes = [[5,10]]
					apple = [randint(0,19) , randint(0,19)]
					score = 0
					



	score_txt = font_small.render("Score: " +str(score), True, WHITE)
	screen.blit(score_txt,(5,5))

	sleep(0.04)
	pygame.display.flip()

pygame.quit()