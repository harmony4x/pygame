import pygame
import time
import math

class Textbutton:
	def __init__ (self, text, position1, position2):
		self.text = text
		self.position1 = position1
		self.position2 = position2

	def is_mouse_on_text(self):
		mouse_x, mouse_y = pygame.mouse.get_pos()
		if self.position1[0] <= mouse_x <= self.position1[0] + self.position2[0] and position1[1] <= mouse_y <= position1[1] + position2[1]:
			return True
		else:
			return False

	def draw(self):
		font = pygame.font.SysFont('sans', 30)
		text_render = font.render(self.text, True, BLACK)
		if self.is_mouse_on_text():
			print("Hello")

		screen.blit(text_render,self.position1)

pygame.init()

screen = pygame.display.set_mode((500,600))

GREY = (150,150,150)
WHITE = (255,255,255)
RED = (255,0,0)
BLACK = (0, 0, 0)
running = True

font = pygame.font.SysFont('sans', 50)
text_1 = font.render('+', True, (BLACK))
text_2 = font.render('-', True, (BLACK))
text_3 = font.render('+', True, (BLACK))
text_4 = font.render('-', True, (BLACK))
text_5 = font.render('START', True, (BLACK))
text_6 = font.render('RESET', True, (BLACK))

start = False
total_secs = 0
total = 0

sound = pygame.mixer.Sound('chuongdongho.mp3')

clock = pygame.time.Clock()
while running:
	clock.tick(60)
	screen.fill(GREY)


	mouse_x , mouse_y = pygame.mouse.get_pos()
	pygame.draw.rect(screen, WHITE, (100,50,50,50))
	pygame.draw.rect(screen, WHITE, (100,200,50,50))
	pygame.draw.rect(screen, WHITE, (200,50,50,50))
	pygame.draw.rect(screen, WHITE, (200,200,50,50))
	pygame.draw.rect(screen, WHITE, (300,50,150,50))
	pygame.draw.rect(screen, WHITE, (300,50,150,50))
	pygame.draw.rect(screen, WHITE, (300,150,150,50))

	screen.blit(text_1, (113,45))
	screen.blit(text_2, (118,195))
	screen.blit(text_3, (213,45))
	screen.blit(text_4, (218,195))

	pygame.draw.rect(screen, BLACK, (50,520, 400,50))
	pygame.draw.rect(screen, WHITE, (60,530, 380,30))

	screen.blit(text_5, (300,50))
	screen.blit(text_6, (300,150))

	pygame.draw.circle(screen, BLACK, (250,400), 100)
	pygame.draw.circle(screen, WHITE, (250,400), 95)
	pygame.draw.circle(screen, BLACK, (250,400), 5)


	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 1:
				pygame.mixer.pause()
				if (100 <= mouse_x <= 150) and (50 <= mouse_y <= 100):
					total_secs += 60
				if (100 <= mouse_x <= 150) and (200 <= mouse_y <= 250):
					total_secs -= 60
				if (200 <= mouse_x <= 250) and (50 <= mouse_y <= 100):
					total_secs += 1
				if (200 <= mouse_x <= 250) and (200 <= mouse_y <= 250):
					total_secs -= 1
				if (300 <= mouse_x <= 450) and (50 <= mouse_y <= 100):
					start = True
					total  = total_secs
				if (300 <= mouse_x <= 450) and (150 <= mouse_y <= 200):
					total_secs = 0;

	if start:
		total_secs -= ms
		if total_secs <0:
			total_secs = 0
			pygame.mixer.Sound.play(sound)
		time.sleep(0.1)

	mins = int(total_secs/60)
	secs = int(total_secs - mins*60)
	ms = 1/10

	time_now = str(mins) +" : " + str(secs)

	text_time = font.render(time_now, True, BLACK)
	screen.blit(text_time, (120,120))
	if total !=0:
		pygame.draw.rect(screen,RED, (60,530, int(380*(total_secs/total)),30))

	x_sec = 250 + 90*math.sin(6*secs * math.pi/180)
	y_sec = 400 - 90*math.cos(6*secs * math.pi/180)
	pygame.draw.line(screen, BLACK, (250,400) , (x_sec,y_sec))

	x_min = 250 + 70*math.sin(6*mins * math.pi/180)
	y_min = 400 - 70*math.cos(6*mins * math.pi/180)
	pygame.draw.line(screen, RED, (250,400) , (x_min,y_min))

	pygame.display.flip()

pygame.quit()