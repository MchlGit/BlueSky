import pygame

class Bumblebee: 
	def __init__(self, blue_sky):
		self.screen = blue_sky.screen
		self.screen_rect = blue_sky.screen.get_rect()

		self.image = pygame.image.load('images/bee.bmp')
		self.rect = self.image.get_rect()

		self.image_2 = pygame.image.load('images/poo.bmp')
		self.rect_2 = self.image_2.get_rect()

		self.rect.center = self.screen_rect.center
		self.rect_2 = self.screen_rect.midbottom

	def blitme(self): 
		self.screen.blit(self.image, self.rect)
		self.screen.blit(self.image_2, self.rect_2)