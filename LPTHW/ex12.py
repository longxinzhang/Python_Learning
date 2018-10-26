#coding=utf-8
age = input("How old are you?")
height = input("How tall are you?")
weight = input("How much do you weigh?")

print(f"So, you are {age} old, your height is {height} and your weight is {weight}. right?")
print("So, you are {age} old, your height is {height} and your weight is {weight}.right?".format(age=age,weight=weight,height=height))
