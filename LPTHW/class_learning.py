#coding=utf-8
class Employee:
	"所有员工的类基"
	empCount = 0
	
	def __init__(self, name, salary):
		self.name = name
		self.salary = salary
		Employee.empCount += 1
		
	
	def displayCount(self):
		print(f"员工数量：{Employee.empCount}")
		
	
	def displayEmployee(self):
		print(f"名字：{self.name}, 工资：{self.salary}")
		
emp1 = Employee("zara",2000)
emp2 = Employee("mami",4000)
emp1.displayEmployee()
emp2.displayEmployee()
print(f"全部员工： {Employee.empCount}")

