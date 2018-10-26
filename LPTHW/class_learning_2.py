#coding=utf-8
class Robot:
	def __init__(self, name, color, weight):
		self.name = name
		self.color = color
		self.weight = weight
		
	def introduce_self(self):
		print(f"My name is {self.name}")
		print(f"and my color is {self.color}")
		print(f"and I have {self.weight} weight.\n")
		

r1 = Robot("Jack", "Blue", 10)
r2 = Robot("Lool", "Black", 20)

#r1.introduce_self()
#r2.introduce_self()

class Person:
	def __init__(self, name, personality, sit, rob):
		self.name = name
		self.personality = personality
		self.issitting = sit
		self.robot_owned = rob
	
	def sit_down(self):
		self.issitting = True
		
	def stand_up(self):
		self.issitting = False
		
p1 = Person("Alice", "Good", False, r2)
p2 = Person("Becky", "Bad", True, r1)

p1.robot_owned.introduce_self()
p2.robot_owned.introduce_self()