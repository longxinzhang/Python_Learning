#coding:utf-8

b=input()
c=input()
#a={b,c}
if not isinstance((b,c),(int,float)):
	raise TypeError('输入数字')
print('okay')