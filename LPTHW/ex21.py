#coding=utf-8
def add(a,b):
	print(f"ADDING {a} + {b}")
	return a + b

def subtract(a,b):
	print(f"SUBTRACT {a} - {b}")
	return a - b
	
def multiply(a,b):
	print(f"MULTIPLY {a} * {b}")
	return a * b
	
def devide(a,b):
	print(f"DEVIDE {a} / {b}")
	return a / b
	
print("让我们来点数学题吧！")

a = int(input("第一个数字是： "))
b = int(input("第二个数字是： "))

age = add(a,b)
height = subtract(a,b)
weight = multiply(a,b)
iq = devide(a,b)

print(f"你的年龄是{age}，身高是{height}，体重是{weight}，智商是{iq}!")

#A puzzle for the extra credit, type it in anyway.
print("Here is a puzzle.")

what = add(age, subtract(height,multiply(weight,devide(iq,2))))

print("That becomes:", what, "Can you do it by hand?")
