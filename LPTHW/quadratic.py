#coding:utf-8
import math

def quadratic(a,b,c):
#	if not isinstance(n[1],(int,float)):
#		raise TypeError('嘿！只能输入数字！')
	delta = math.pow(b,2)-4*a*c
	if delta>=0 and a != 0:
		x1=(-b + math.sqrt(delta))/(2*a)
		x2=(-b - math.sqrt(delta))/(2*a)
		return('这个等式有两个不相等的实数根,它们分别是\n%.1f, %.1f' %(x1,x2))
	elif a==0 and b != 0:
		x1=x2=-c/b
		return('这个等式只有一个实数根，它是：%.1f' % x1)
	else:
		return ('无解')

aa=float(input('请输入a='))
bb=float(input('请输入b='))
cc=float(input('请输入c='))

print(quadratic(aa,bb,cc))
