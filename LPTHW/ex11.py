#coding=utf-8
print("how old are you?", end="waiting")
age = input()
print("how tall are you?", end="waiting")
height = input()
print("how much do you weigh?", end="waiting")
weight = input()

print(f"so, you are {age} old, {height} tall, and {weight} heavy")
print("so, you are {age} old, {height} tall and {weight} heavy".format(age=age,height=height,weight=weight))
#错误用法
#print("so, you are {age} old, {height} tall and {weight} heavy".format(age,heightt,weight))