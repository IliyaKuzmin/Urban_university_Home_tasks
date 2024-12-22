#!/usr/bin/python3
# root-class type alive creatures
class Alive_Creatures(object):
	cause_of_death="Умерло своей смертью"
	def __init__(self, name,x,y,z=0):
		self.name=name
		self.x=x
		self.y=y
		self.z=z
	def set_cause_of_death(self,cause):
		self.cause_of_death=cause
class Plant(Alive_Creatures):
	def __init__(self,name,x,y,z=0):
		super().__init__(name,x,y,z=0)
	def __del__(self):
		message=self.cause_of_death
		print(f"Растение с именем: {self.name} {message}")
class Animal(Alive_Creatures):
	cause_of_death="Умерло своей смертью"
	def __init__(self, age, speed,name, x, y, z=0):
		super().__init__(name,x,y,z=0)
		self.stage_growth=age
		self.speed=speed
	def go_to (self,target_x,target_y,target_z=0):
		while self.x!=target_x or self.y!=target_y or self.z!=target_z:
			move_on_x=target_x-self.x
			move_on_y=target_y-self.y
			move_on_z=target_z-self.z
	def __del__(self):
		message=self.cause_of_death
		print(f"Животное с именем: {self.name} {message}")
# other - consume object
# class-type of eaters
class Herbivoros(Animal):
	def __init__(self,age, speed,name, x, y, z=0):
		super().__init__(age, speed,name, x, y, z)
	def eat(self,other):
		if isinstance(other, Plant):
			other.set_cause_of_death("Было съедено травоядным")
			del other
			print(f"Животное с именем: {self.name} наелось")
		else:
			self.set_cause_of_death("Умерло от голода")
			del self
class Predator(Animal):
	def __init__(self,age, speed,name, x, y, z=0):
		super().__init__(age, speed,name, x, y, z)
	def eat(self.other):
		if isinstance(other, Herbivoros):
			other.set_cause_of_death("Было съедено хищником")
			del other
			print(f"Животное с именем: {self.name} наелось")
		else:
			self.set_cause_of_death("Умерло от голода")
			del self
h1=Herbivoros(2,1,"Cow",2,2)
pr=Predator(2,1,"Wolf",2,2)
p1=Plant("Grass",2,2)
pr.eat("25")