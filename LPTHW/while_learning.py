#coding=utf-8
from sys import exit
d = {"user":"666"}
count = 5
while True:
	name = input("请输入您的用户名")
	if name in d:
		break
	else:
		count -= 1
		print("您输入的用户名不存在，请重新输入")
		print(f"用户名错误或者不存在，本次登陆还剩{count}次机会。")
		
		if count == 0:
			print("超过尝试次数，系统自动退出。")
			exit()
			
		continue
		
while True:
	password = input("请输入您的密码")
	if d[name] == password:
		print("进入系统")
		break
	else:
		count -= 1
		print("您输入的密码不正确，请重新输入")
		print(f"密码错误，本次登陆还剩{count}次机会。")
		
		if count == 0:
			print("超过尝试次数，系统自动退出。")
			exit()
			
		continue

