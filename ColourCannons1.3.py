import pygame, random, math
screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
pygame.display.set_caption("Colours")
pygame.font.init()
pygame.init()
r = 50
g = 100
b = 130
s = []
new = 0
up = 0
down = 0
ss = 10 #size 10
SS = 10 #speed 10
ro = 8 #rows-1
side = 0
clock = pygame.time.Clock()

pygame.mouse.set_visible(0)

while (True):
	clock.tick(60)
	screen.fill((0,0,0))
	xa, ya = pygame.mouse.get_pos()
	
	for e in pygame.event.get():
		if e.type == pygame.MOUSEBUTTONDOWN:
			if pygame.mouse.get_pressed()[2]:
				if e.button == 4:
					SS += 2
					if SS > 20:
						SS = 20
				if e.button == 5:
					SS -= 2
					if SS < 5:
						SS = 5
			else:
				if e.button == 4:
					ss += 2
					if ss > 50:
						ss = 50
				if e.button == 5:
					ss -= 2
					if ss < 5:
						ss = 5
						
	if up == 1 and (pygame.key.get_pressed()[pygame.K_UP] != 1):
		ro += 1
		if ro > 50:
			ro = 50
		up = 0
		
	if down == 1 and (pygame.key.get_pressed()[pygame.K_DOWN] != 1):
		ro -= 1
		if ro < 3:
			ro = 3
		down = 0
	
	if pygame.key.get_pressed()[pygame.K_DOWN] and down == 0:
		down = 1
	
	if pygame.key.get_pressed()[pygame.K_UP] and up == 0:
		up = 1
					
	if pygame.key.get_pressed()[pygame.K_d]:
		ss = 10
		SS = 10
		ro = 8
	
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
		def Assign(self,xloc,r,g,b):
			self.ID = shot
			
			if side == 0:
				self.x = xloc*(screen.get_width()/ro)
				self.y = screen.get_height()
			
			if side == 1:
				self.x = 0
				self.y = xloc*(screen.get_height()/ro)
			
			if side == 2:
				self.x = xloc*(screen.get_width()/ro)
				self.y = 0
			
			if side == 3:
				self.x = screen.get_width()
				self.y = xloc*(screen.get_height()/ro)
			
			self.des = 0
			self.c = (r,g,b)
		
		def Shoot(self):
			if (self.x < -ss*2) or (self.x > screen.get_width()+ss) or (self.y < -ss-10) or (self.y > screen.get_height()+ss):
				del s[s.index(self.ID)]
			if self.des == 0:
				self.velox,self.veloy = FindSpeed((xa,ya),(self.x,self.y),SS)
			if (xa+(25) > self.x > xa-(25)) and (ya-(25) < self.y < ya+(25)):
				self.des = 1
			self.x += self.velox
			self.y += self.veloy
			pygame.draw.rect(screen, self.c, (self.x-ss/2,self.y-ss/2,ss,ss),0)
	
	if pygame.mouse.get_pressed()[0]:
		#cr, cg, cb = random.randint(0,75),random.randint(100,200),random.randint(175,255)
		if (r > 250):
			r1 = -1
		if (r < 140):
			r1 = 1	
		r += r1
		if (g > 250):
			g1 = -2	
		if (g < 140):
			g1 = 2
		g += g1
		if (b > 250):
			b1 = -4
		if (b < 140):
			b1 = 4
		b += b1
			
		for i in range(0,ro+1):
			shot = Shot()
			shot.Assign(i,r,g,b)
			s.append(shot)
		
	for i in range(0,len(s)):
		try:
			s[i].Shoot()
		except IndexError:
			pass
			
	pygame.draw.rect(screen, (255,255,255), (xa-4.5,ya-4.5,10,10), 2)
	
	pygame.display.flip()
	event = pygame.event.poll()
	
	if pygame.key.get_pressed()[pygame.K_3]:
		side = 2
		
	if pygame.key.get_pressed()[pygame.K_4]:
		side = 3
		
	if pygame.key.get_pressed()[pygame.K_1]:
		side = 0
		
	if pygame.key.get_pressed()[pygame.K_2]:
		side = 1
		
	if pygame.key.get_pressed()[pygame.K_ESCAPE]:
		break
