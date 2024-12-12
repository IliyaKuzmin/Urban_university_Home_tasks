#!/usr/bin/python3
class Person(object):
	def __init__(self, name, age):
		self.name=name
		self.age=age
	def greeting(self):
		return f"Привет, меня зовут {self.name}, мне {self.age} лет"
class Student(Person):
	def __init__(self, name, age):
		super().__init__(name, age)
	def student_greeting(self):
		print (self.greeting()+" и я-студент")
class Teacher(Person):
	def __init__(self, name, age):
		super().__init__(name, age)
	def teacher_greeting(self):
		print (self.greeting()+" и я-учитель")
h1=Student("Alisa",12)
h1.student_greeting()
h2=Teacher("Anton",38)
h2.teacher_greeting()
