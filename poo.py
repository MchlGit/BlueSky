import pygame

class Poo: 
	def __init__(self, blue_sky):
		self.screen = blue_sky.screen
		self.screen_rect = blue_sky.screen.get_rect()

		self.image = pygame.image.load('images/poo.bmp')
		self.rect = self.image.get_rect()

		self.rect.midbottom = self.screen_rect.midbottom

	def blitme(self): 
		self.screen.blit(self.image, self.rect)
