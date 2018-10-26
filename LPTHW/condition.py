# coding: utf-8
#age = int(input("please tell me your age:...."))

#单条件
#if age>= 18:
#	print ('your age is, ',age)
#	print ('adult')
#else:
#	printcdcdcd的 ('your age is, ',age)
#	print ('teenage')


#多条件elif
#if age>=18:
#	print('your age is,', age)
#	print('You are adult')
#elif age>=12:
#	print('your age is,', age)
#	print('you are teenage')
#else:
#	print('your age is,', age)
#	print('hi,kid!')

#多条件从上到下的判断
#if age>=6:
#	print('hi,kid')
#elif age>=12:
#	print('hi,teenage')
#else:
#	print('hi, adult')

#条件判断的练习题
name=str(input('现在我们检测身体BMI值，请告诉我你的名字'))
weight=int(input('好的%s，你的体重是多少公斤？' %name))
h=int(input('你的身高是多少厘米？'))
height=float(h/100)
bmi=float(weight/(height*height))
print('-------\n你的名字是：',name,'，\n你的体重是',weight,'公斤，\n你的身高是',h,'厘米。\n结果显示你的BMI值为：%.1f' %bmi)
#要把%f/d/x/s 放在括号里面朋友！
if bmi>=32:
	print('你属于【严重肥胖】')
elif bmi>=28 and bmi<32:
	print('你属于【肥胖】')
elif bmi>=25 and bmi<28:
	print('你属于【过重】')
elif bmi>=18.5 and bmi<25:
	print('你属于【正常】')
else:
	print('你属于【过轻】')