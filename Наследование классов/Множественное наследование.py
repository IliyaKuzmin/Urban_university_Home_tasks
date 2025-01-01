#!/usr/bin/python3
class Alive_Creatures(object):
	cause_of_death="Умерло своей смертью"
	def __init__(self, name,x,y,z=0):
		self.name=name
		self.x=x
		self.y=y
		self.z=z
	def set_cause_of_death(self,cause):
		self.cause_of_death=cause
class Animal(Alive_Creatures):
	def __init__(self, age, speed,name, x, y, z=0):
		super().__init__(name,x,y,z=0)
		self.stage_growth=age
		self.speed=speed
	def go_to (self,target_x,target_y):
		while self.x!=target_x or self.y!=target_y:
			move_on_x=target_x-self.x
			move_on_y=target_y-self.y
			self.x+=move_on_x
			self.y+=move_on_y
	def __del__(self):
		message=self.cause_of_death
		print(f"Животное с именем: {self.name} {message}")
class Mammals(Animal):
	def __init__(self, age, speed, name, x, y, z=0):
		super().__init__(age, speed, name, x, y, z=0)
	def feed_the_child(self):
		print("I'm feeding the child")
class Poisonous(Alive_Creatures):
	DANGEROUS_DEGREE=0
	def try_to_toch(self):
		self.DANGEROUS_DEGREE+=2
		if self.DANGEROUS_DEGREE <=5:
			print("Don't touch me, I'm poisonous")
		elif self.DANGEROUS_DEGREE > 5 and self.DANGEROUS_DEGREE < 10:
			print("Be careful,I'm atacking you 0_0")
		else: self.DANGEROUS_DEGREE=0
class Floating(Animal):
	def to_dive(self,deep):
		self.z-=abs(deep)
	def to_float(self,deep):
		if self.z < 0:
			if (self.z + abs(deep))<=0:
				self.z+=abs(deep)
			else: self.z=0
class platypus(Mammals,Poisonous,Floating):
	sound="Click-click-click"
	def __init__(self, age, speed, name, x, y, z=0):
		super().__init__(age, speed, name, x, y, z=0)
	def lay_egg(self):
		print("Here are 2 eggs")
	def get_coord(self):
		print(f"X:{self.x} Y:{self.y} Z:{self.z}")
	def is_alive(self):
		print ("True")
	def speak(self):
		print(self.sound)
plat=platypus(2,4,"platypus",5,5)
plat.try_to_toch()
plat.try_to_toch()
plat.try_to_toch()
plat.is_alive()
plat.get_coord()
plat.to_dive(10)
plat.get_coord()
plat.go_to(10,10)
plat.lay_egg()
plat.speak()
plat.feed_the_child()
plat.get_coord()