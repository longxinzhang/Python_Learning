#coding=utf-8
#def my_abs(x):
#	if not isinstance(x,(int,float)):
#		raise TypeError('嘿！只能输入数字！')
#	if x>=0:
#		return x
#	else:
#		return -x
#a=my_abs(int(input('your absolute number: ')))
#print('the absolute number of it is: ',a)

#制作一个求长方形面积的函数
import math

def square(x,y,s):


	if x==y and x>0:
		s=math.pow(x,2)
		return('这是一个正方形，它的面积为%f' % s)
	elif x!=y and x>0 and y>0:
		s=x*y
		return s
	else:
		return ('计算错误！边长必须大于0')
x=int(input('请输入一个边长：'))
y=int(input('请输入另一个边长'))
s=set([x,y])
print (square(x,y,s))