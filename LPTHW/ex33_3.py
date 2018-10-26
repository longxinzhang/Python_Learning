#coding=utf-8
start_num = int(input("Please input your start number: \n --->"))
step_num = int(input("Please input your step number: \n --->"))
stop_num = int(input("When would you like the add-math stop? \n --->"))

def number_add(a,b,c,m):
	print(f"the start number is {a}, we will gradually add {b} to it ,and stop at {c}")
	
	while a < c:
		number_list.append(a)
		a += b
		m=number_list[-1]
		print(f"we have added {b} to it, now the list have:", number_list)
		print(f"now the last number in the list is {m}")
		
	print("looks like the add is finished. let's see the result")
	for num in number_list:
		print(num)
	return m
number_list = []


d= number_add(start_num,step_num,stop_num,0)

print("函数运行之后的number_list",number_list)

print("list里最后一个数是：",d)


#在def里面，之前是没有m的，没有m这个变量，就不能输出这么一个变量
#现在有这个变量了，就可以将变量的value给计算结果了。