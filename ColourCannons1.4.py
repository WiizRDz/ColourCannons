import pygame, random, math
screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
pygame.display.set_caption("Colours")
pygame.font.init()
pygame.init()
s = []
h = .85
clock = pygame.time.Clock()

pygame.mouse.set_visible(0)

while (True):
	clock.tick(60)
	screen.fill((0,0,0))
	xa, ya = pygame.mouse.get_pos()
	
	if (pygame.key.get_pressed()[pygame.K_w]):
		h -= .005
	
	if (pygame.key.get_pressed()[pygame.K_s]):
		h += .005
	
	def FindSpeed(p1,p2,s,xd=0,yd=0,a=0,xs=0,ys=0):
		x1,y1 = p1
		x2,y2 = p2
		xd = x1-x2
		if xd == 0:
			xd = (10**(-200))
		yd = y1-y2
		a = math.atan2(yd,xd)
		xs = s*math.cos(a)
		ys = s*math.sin(a)
		return xs,ys
	
	class Shot():			
		def Assign(self,xloc):
			self.ID = shot
			
			self.x = xloc*(screen.get_width())
			self.y = screen.get_height()*h
			
			self.des = 0
			self.c = (140,255,220)
		
		def Shoot(self):
			if (self.x < -7*2) or (self.x > screen.get_width()+7) or (self.y < -7-10) or (self.y > screen.get_height()+7):
				del s[s.index(self.ID)]
			if self.des == 0:
				self.velox,self.veloy = FindSpeed((xa,ya),(self.x,self.y),10)
			if (xa+(25) > self.x > xa-(25)) and (ya-(25) < self.y < ya+(25)):
				self.des = 1
			self.x += self.velox
			self.y += self.veloy
			pygame.draw.rect(screen, self.c, (self.x-7/2,self.y-7/2,7,7),0)
	
	if pygame.mouse.get_pressed()[0]:
		for i in range(0,2):
			shot = Shot()
			shot.Assign(i)
			s.append(shot)
		
	for i in range(0,len(s)):
		try:
			s[i].Shoot()
		except IndexError:
			pass
			
	pygame.draw.rect(screen, (255,255,255), (xa-4.5,ya-4.5,10,10), 2)
	
	pygame.display.flip()
	event = pygame.event.poll()
		
	if pygame.key.get_pressed()[pygame.K_ESCAPE]:
		break
