#!/usr/bin/python3
import math
class Figure(object):
	"""docstring for """
	def __init__(self, x, y, background_color="0xffffff"):
		self.x=x
		self.y=y
		self.__border_color="0x000000"
		self.__background_color=background_color
	def set_background_color(self, red, green, blue):
		*colors,=red,green,blue
		is_int=[]
		is_correct_value=[]
		for el in colors:
			is_int.append(isinstance(el,int))
		if all(is_int):
			for al in colors:
				is_correct_value.append(0<=al<256)
			if all(is_correct_value) and all(is_int):
				color=hex(colors[0])+hex(colors[1])+hex(colors[2])
				self.__background_color="0x"+color.replace("0x","")
			else: self.__output_error("in range 0-255")
		elif red=="tr" or green=="tr" or blue=="tr":
			self.__background_color=None
		else: self.__output_error("integers")
	def get_background_color(self):
		if self.__background_color!=None:
			red=self.__background_color[2:4]
			green=self.__background_color[4:6]
			blue=self.__background_color[6:8]
			print(f"Red:{int(red,16)}\nGreen:{int(green,16)}\nBlue:{int(blue,16)}")
		else: print("Background is transparent")
	def __output_error(self, message):
		print(f"All values must be {message}")

#		if 0<red<256 and 0<green<256 and 0<blue<256:
#			print("All color is correct")
class Valume_Figure(Figure):
	def __init__(self, x, y, z):
		super().__init__(x, y)
		self.z=z
class Triangle(Figure):
	def __init__(self, x, y, angle):
		super().__init__(x, y)
		self.angle=radians(angle)
	def get_area(self):
		sqrt(x**2+y**2-(2*x*y)*cos(self.angle))
d=Figure(25,8)
d.set_background_color(222,"tr",222)
d.get_background_color()