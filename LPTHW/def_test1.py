#coding=utf-8
def greet_me(**kwargs):
	if kwargs is not None:
		for key, value in kwargs.items():
			print(f"{key}={value}")
greet_me(name=1, name1=2)