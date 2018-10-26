#coding=utf-8
#check this out!https://www.youtube.com/watch?v=RSl87lqOXDE
class Employee:
	raise_amt  = 1.04
	
	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.email = first + "." + last + "@email.com"
		self.pay = pay
	
	def fullname(self):
		return f"{self.first} {self.last}"
		
	def apply_raise(self):
#		self.pay = int(self.pay * 10)
		self.pay = int(self.pay * self.raise_amt)
		return self.pay
		
		
class Developer(Employee):
	raise_amt = 1.1
	
	def __init__(self, first, last, pay, prog_lang):
		super().__init__(first, last, pay)
		self.prog_lang = prog_lang
		
class Manager(Employee):
	
	def __init__(self, first, last, pay, employees=None):
		super().__init__(first, last, pay)
		if employees is None:
			self.employees = []
		else:
			self.employees = employees
			
	def add_emp(self, emp):
		if emp not in self.employees:
			self.employees.append(emp)

	def remove_emp(self, emp):
		if emp in self.employees:
			self.employees.remove(emp)			

	def print_emps(self):
		for emp in self.employees:
			print("-->", emp.fullname())

			
dev_1 = Developer("Long", "Xin", 10000, "python")
dev_2 = Employee("Rowson", "Chang", 20000)
#注意看，最后一个argument是个list，list里的不是string，是variable！
mgr_1 = Manager("Sue", "Smith", 90000, [dev_1])

print(mgr_1.email)
mgr_1.print_emps()
#print(dev_1.email)
#print(dev_1.prog_lang)
#print(dev_1.apply_raise())
#print(dev_1.pay)