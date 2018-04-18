import pygame
from Color import Color
from itertools import repeat

class Level:
	def __init__(self,filename):
		self.block_size = (self.w,self.h) = (80,80)
		self.level = []
		self.screen_player_offset = (100,300)
		self.player_position = (0,0)
		self.enemies = []
		self.floor = []
		self.screen_shake = False
		self.default_y = 0
		f = open(filename,'r')
		for l in f:
			self.level.append(l)
		if len(self.level):
			self.screen = pygame.Surface((len(self.level[0])*self.w,len(self.level)*self.h))
			self.screen.fill(Color.white)
			j = 0
			for r in self.level:
				i = 0
				for c in r:
					pos = (i*self.w,j*self.h)
					if c == 'P':
						self.player_position = pos
					if c == 'E':
						self.enemies.append(pos)
					if c == '1':
						self.floor.append(pos)
					i += 1
				j += 1
		self.rect = self.screen.get_rect()
		self.master = pygame.Surface((self.rect.width,self.rect.height))
		self.master.blit(self.screen,(0,0),self.rect)

	def get_full_screen(self):
		self.screen.blit(self.master,(0,0),self.rect)
		return self.screen

	def get_player_starting_position(self):
		return self.player_position

	def get_enemies(self):
		return self.enemies

	def get_floor(self):
		return self.floor

	def get_screen(self):
		return self.screen

	def get_rect(self,dim,player):
		'''
		Return the portion of the level where the player is currently visible

		'''

		(dx,dy) = dim
		rx = 0
		'''
		if rx < 0:
			rx = 0
		if rx + dx > self.rect.width:
			rx = self.rect.width - dx
		'''

		'''
		if ry < 0:
			ry = 0
		if ry + dy > self.rect.height:
			ry = self.rect.height - dy
			'''
		rx = 0
		self.default_y += 1
		self.default_y *= 1.0005
		ry = self.default_y
		rect = pygame.Rect(rx,ry,dx,dy)
		return rect

	def shake(self):
		s = -1
		for _ in range(0, 3):
			for x in range(0, 30, 10):
				yield (x*s, 0)
			for x in range(30, 0, 10):
				yield (x*s, 0)
			s *= -1
		while True:
			yield (0, 0)

	def set_default_y(self):
		self.default_y = 0
		rect = pygame.Rect(0, 0, 800, 800)
		return rect


class Floor(pygame.sprite.Sprite):
	def __init__(self,gravity,position,size):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface(size)
		self.image.fill(Color.gray_9)
		self.rect = self.image.get_rect()
		(self.rect.x,self.rect.y) = position
		self.gravity = gravity

	def get_position(self):
		return (self.rect.x,self.rect.y)

	def update(self):
		'''
		update behavior
		'''
